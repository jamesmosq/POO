"""
Ejercicio propuesto 04 - CRUD de transportadoras
Nivel: avanzado

Es el CRUD con Treeview del tema 04_interfaces_graficas, pero ahora los
datos viven en la tabla Shippers de Northwind.

Requisitos. Crea la clase GestorTransportadoras(tk.Frame) que recibe
(master, con):
1. self.nombre y self.telefono: Entry.
2. Botones self.boton_agregar, self.boton_actualizar y self.boton_eliminar.
3. self.tabla: Treeview con columnas ("nombre", "telefono"). Usa el
   ShipperID como id de cada fila (parámetro iid de insert), así sabes a
   qué registro corresponde cada fila:
       self.tabla.insert("", tk.END, iid=str(shipper_id), values=(...))
4. cargar(): llena la tabla desde la base de datos (ordenada por id).
5. agregar(), actualizar() y eliminar(): modifican la BASE DE DATOS (con
   commit) y después llaman a cargar() para que la tabla muestre lo real.
   actualizar y eliminar trabajan sobre la fila seleccionada; sin
   selección no hacen nada. agregar ignora campos vacíos.
6. al_seleccionar(): copia los datos de la fila seleccionada a los Entry.

Las pruebas crean transportadoras con nombres que empiezan por PRUEBA_EJ_
y las borran al terminar.

Conceptos: CRUD con interfaz y base de datos, la base de datos como
fuente de verdad.
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

# Escribe tu solución aquí



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
