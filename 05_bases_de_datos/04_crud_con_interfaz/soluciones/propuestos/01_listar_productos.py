"""
Solución - Ejercicio propuesto 01 - Listar productos
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


class VistaProductos(tk.Frame):
    def __init__(self, master, con):
        super().__init__(master)
        self.con = con
        self.tabla = ttk.Treeview(self, columns=("id", "nombre", "precio"), show="headings", height=15)
        for columna, titulo, ancho in (("id", "Id", 50), ("nombre", "Producto", 250), ("precio", "Precio", 80)):
            self.tabla.heading(columna, text=titulo)
            self.tabla.column(columna, width=ancho)
        self.tabla.pack(fill="both", expand=True)
        self.estado = tk.Label(self, text="")
        self.estado.pack(side="left", padx=5)
        self.boton_recargar = tk.Button(self, text="Recargar", command=self.cargar)
        self.boton_recargar.pack(side="right", padx=5, pady=5)
        self.cargar()

    def cargar(self):
        self.tabla.delete(*self.tabla.get_children())
        with closing(self.con.cursor()) as cursor:
            cursor.execute("SELECT ProductID, ProductName, Price FROM Products ORDER BY ProductName")
            filas = cursor.fetchall()
        for fila in filas:
            self.tabla.insert("", tk.END, values=fila)
        self.estado.config(text=f"{len(filas)} productos")


# ----------------------------------------------------------------------
# Pruebas
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
