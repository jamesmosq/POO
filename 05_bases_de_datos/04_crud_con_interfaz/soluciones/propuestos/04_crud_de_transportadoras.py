"""
Solución - Ejercicio propuesto 04 - CRUD de transportadoras
"""

import os
import tkinter as tk
from contextlib import closing
from tkinter import ttk

import mysql.connector

CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "base1234"),
    "database": os.getenv("DB_NAME", "northwind"),
}


class GestorTransportadoras(tk.Frame):
    def __init__(self, master, con):
        super().__init__(master)
        self.con = con

        formulario = tk.Frame(self)
        formulario.pack(fill="x")
        tk.Label(formulario, text="Nombre").grid(row=0, column=0, sticky="e")
        self.nombre = tk.Entry(formulario, width=30)
        self.nombre.grid(row=0, column=1, pady=2)
        tk.Label(formulario, text="Teléfono").grid(row=1, column=0, sticky="e")
        self.telefono = tk.Entry(formulario, width=30)
        self.telefono.grid(row=1, column=1, pady=2)

        botones = tk.Frame(self)
        botones.pack(pady=5)
        self.boton_agregar = tk.Button(botones, text="Agregar", command=self.agregar)
        self.boton_actualizar = tk.Button(botones, text="Actualizar", command=self.actualizar)
        self.boton_eliminar = tk.Button(botones, text="Eliminar", command=self.eliminar)
        for boton in (self.boton_agregar, self.boton_actualizar, self.boton_eliminar):
            boton.pack(side="left", padx=2)

        self.tabla = ttk.Treeview(self, columns=("nombre", "telefono"), show="headings", height=8)
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("telefono", text="Teléfono")
        self.tabla.pack(fill="both", expand=True)
        self.tabla.bind("<<TreeviewSelect>>", lambda evento: self.al_seleccionar())
        self.cargar()

    def _ejecutar(self, sql, parametros):
        with closing(self.con.cursor()) as cursor:
            cursor.execute(sql, parametros)
            self.con.commit()

    def _seleccionado(self):
        seleccion = self.tabla.selection()
        return int(seleccion[0]) if seleccion else None

    def _datos_formulario(self):
        nombre = self.nombre.get().strip()
        telefono = self.telefono.get().strip()
        return (nombre, telefono) if nombre and telefono else None

    def cargar(self):
        self.tabla.delete(*self.tabla.get_children())
        with closing(self.con.cursor()) as cursor:
            cursor.execute("SELECT ShipperID, ShipperName, Phone FROM Shippers ORDER BY ShipperID")
            for id_shipper, nombre, telefono in cursor.fetchall():
                self.tabla.insert("", tk.END, iid=str(id_shipper), values=(nombre, telefono))

    def al_seleccionar(self):
        id_shipper = self._seleccionado()
        if id_shipper is None:
            return
        nombre, telefono = self.tabla.item(str(id_shipper), "values")
        self.nombre.delete(0, tk.END)
        self.nombre.insert(0, nombre)
        self.telefono.delete(0, tk.END)
        self.telefono.insert(0, telefono)

    def agregar(self):
        datos = self._datos_formulario()
        if datos is None:
            return
        self._ejecutar("INSERT INTO Shippers (ShipperName, Phone) VALUES (%s, %s)", datos)
        self.cargar()

    def actualizar(self):
        id_shipper = self._seleccionado()
        datos = self._datos_formulario()
        if id_shipper is None or datos is None:
            return
        self._ejecutar("UPDATE Shippers SET ShipperName = %s, Phone = %s WHERE ShipperID = %s", (*datos, id_shipper))
        self.cargar()

    def eliminar(self):
        id_shipper = self._seleccionado()
        if id_shipper is None:
            return
        self._ejecutar("DELETE FROM Shippers WHERE ShipperID = %s", (id_shipper,))
        self.cargar()


# ----------------------------------------------------------------------
# Pruebas
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

        def escribir(nombre, telefono):
            for entrada, valor in ((app.nombre, nombre), (app.telefono, telefono)):
                entrada.delete(0, tk.END)
                entrada.insert(0, valor)

        escribir("PRUEBA_EJ_Flash", "300")
        app.boton_agregar.invoke()
        fila = en_base_de_datos("PRUEBA_EJ_Flash")
        assert fila is not None, "agregar() debe guardar en la base de datos"
        id_nuevo = str(fila[0])
        assert app.tabla.exists(id_nuevo), "La fila debe usar el ShipperID como iid"

        app.tabla.selection_set(id_nuevo)
        app.al_seleccionar()
        assert app.nombre.get() == "PRUEBA_EJ_Flash"

        escribir("PRUEBA_EJ_Flash", "311 222 3344")
        app.boton_actualizar.invoke()
        assert en_base_de_datos("PRUEBA_EJ_Flash")[1] == "311 222 3344"
        assert app.tabla.item(id_nuevo, "values")[1] == "311 222 3344"

        app.tabla.selection_set(id_nuevo)
        app.boton_eliminar.invoke()
        assert en_base_de_datos("PRUEBA_EJ_Flash") is None
        assert not app.tabla.exists(id_nuevo)

        cantidad = len(app.tabla.get_children())
        escribir("", "")
        app.boton_agregar.invoke()
        app.tabla.selection_remove(app.tabla.selection())
        app.boton_eliminar.invoke()
        assert len(app.tabla.get_children()) == cantidad
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
        raiz.title("Transportadoras")
        GestorTransportadoras(raiz, con).pack(fill="both", expand=True, padx=10, pady=10)
        raiz.mainloop()
        con.close()
