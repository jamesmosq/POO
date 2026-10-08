"""
Ejercicio para corregir 04 - CRUD que no guarda
Nivel: intermedio
Errores a encontrar: 3

Qué debería hacer el programa:
    GestorTransportadoras agrega, actualiza y elimina transportadoras en la
    BASE DE DATOS. La tabla de la interfaz siempre refleja lo que hay en la
    base de datos. Cada fila del Treeview usa el ShipperID como iid.

Ojo: la interfaz puede "verse bien" aunque la base de datos no haya
cambiado. Las pruebas revisan la base de datos con otra conexión.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""
import os
import tkinter as tk
from contextlib import closing
from tkinter import ttk

import mysql.connector

CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "northwind"),
}


class GestorTransportadoras(tk.Frame):
    def __init__(self, master, con):
        super().__init__(master)
        self.con = con
        self.nombre = tk.Entry(self)
        self.nombre.pack()
        self.telefono = tk.Entry(self)
        self.telefono.pack()
        self.tabla = ttk.Treeview(self, columns=("nombre", "telefono"), show="headings")
        self.tabla.pack()
        self.cargar()

    def cargar(self):
        self.tabla.delete(*self.tabla.get_children())
        with closing(self.con.cursor()) as cursor:
            cursor.execute("SELECT ShipperID, ShipperName, Phone FROM Shippers ORDER BY ShipperID")
            for id_shipper, nombre, telefono in cursor.fetchall():
                self.tabla.insert("", tk.END, iid=str(id_shipper), values=(nombre, telefono))

    def _ejecutar(self, sql, parametros):
        with closing(self.con.cursor()) as cursor:
            cursor.execute(sql, parametros)
            self.con.commit()

    def agregar(self):
        self._ejecutar("INSERT INTO Shippers (ShipperName, Phone) VALUES (%s, %s)",
                       (self.nombre.get(), self.telefono.get()))

    def actualizar(self):
        seleccion = self.tabla.selection()
        if seleccion:
            self._ejecutar("UPDATE Shippers SET ShipperName = %s, Phone = %s WHERE ShipperID = %s",
                           (self.nombre.get(), self.telefono.get(), seleccion))
            self.cargar()

    def eliminar(self):
        seleccion = self.tabla.selection()
        if seleccion:
            self.tabla.delete(seleccion[0])


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
def en_base_de_datos(nombre):
    otra = mysql.connector.connect(**CONFIG)
    cursor = otra.cursor(buffered=True)
    cursor.execute("SELECT ShipperID, Phone FROM Shippers WHERE ShipperName = %s", (nombre,))
    fila = cursor.fetchone()
    cursor.close()
    otra.close()
    return fila


if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    raiz = tk.Tk()
    raiz.withdraw()
    try:
        app = GestorTransportadoras(raiz, con)
        app.nombre.insert(0, "PRUEBA_EJ_Corrige")
        app.telefono.insert(0, "100")
        app.agregar()
        id_nuevo = str(en_base_de_datos("PRUEBA_EJ_Corrige")[0])
        assert app.tabla.exists(id_nuevo), "Después de agregar, la tabla debe mostrar la nueva transportadora"

        app.tabla.selection_set(id_nuevo)
        app.telefono.delete(0, tk.END)
        app.telefono.insert(0, "200")
        app.actualizar()
        assert en_base_de_datos("PRUEBA_EJ_Corrige")[1] == "200"

        app.tabla.selection_set(id_nuevo)
        app.eliminar()
        assert en_base_de_datos("PRUEBA_EJ_Corrige") is None, "eliminar() debe borrar de la base de datos"
        assert not app.tabla.exists(id_nuevo)
    finally:
        raiz.destroy()
        cursor = con.cursor()
        cursor.execute("DELETE FROM Shippers WHERE ShipperName LIKE 'PRUEBA_EJ_%'")
        con.commit()
        cursor.close()
        con.close()
    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        con = mysql.connector.connect(**CONFIG)
        raiz = tk.Tk()
        GestorTransportadoras(raiz, con).pack(fill="both", expand=True)
        raiz.mainloop()
        con.close()
