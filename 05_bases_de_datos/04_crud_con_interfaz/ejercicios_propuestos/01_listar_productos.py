"""
Ejercicio propuesto 01 - Listar productos
Nivel: básico

Requisitos. Crea la clase VistaProductos(tk.Frame) que recibe
(master, con):
1. self.tabla: ttk.Treeview con columnas ("id", "nombre", "precio") y
   show="headings". Pon títulos a las columnas con heading().
2. self.estado: Label que muestra "77 productos" (la cantidad real).
3. self.boton_recargar: Button "Recargar" que llama a cargar().
4. cargar(): BORRA las filas actuales de la tabla y vuelve a llenarla con
   ProductID, ProductName y Price de todos los productos, ordenados por
   nombre. Actualiza self.estado.
5. Llama a cargar() al final de __init__.

Para borrar todas las filas de un Treeview:
    self.tabla.delete(*self.tabla.get_children())

Conceptos: llenar un Treeview desde la base de datos, recargar datos.
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
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    ref = con.cursor(buffered=True)
    ref.execute("SELECT ProductName FROM Products ORDER BY ProductName")
    nombres = [fila[0] for fila in ref.fetchall()]
    ref.close()

    raiz = tk.Tk()
    raiz.withdraw()
    vista = VistaProductos(raiz, con)

    filas = [vista.tabla.item(i, "values") for i in vista.tabla.get_children()]
    assert [fila[1] for fila in filas] == nombres
    assert vista.estado.cget("text") == f"{len(nombres)} productos"

    vista.boton_recargar.invoke()
    vista.boton_recargar.invoke()
    assert len(vista.tabla.get_children()) == len(nombres), "Recargar no debe duplicar las filas"
    raiz.destroy()
    con.close()
    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        con = mysql.connector.connect(**CONFIG)
        raiz = tk.Tk()
        raiz.title("Productos")
        VistaProductos(raiz, con).pack(fill="both", expand=True)
        raiz.mainloop()
        con.close()
