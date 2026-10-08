"""
Solución - Ejercicio propuesto 03 - Combobox de categorías
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


class ProductosPorCategoria(tk.Frame):
    def __init__(self, master, con):
        super().__init__(master)
        self.con = con
        with closing(con.cursor()) as cursor:
            cursor.execute("SELECT CategoryID, CategoryName FROM Categories ORDER BY CategoryName")
            filas = cursor.fetchall()
        # El Combobox muestra nombres; el diccionario traduce el nombre al id.
        self.ids = {nombre: id_categoria for id_categoria, nombre in filas}
        self.categorias = ttk.Combobox(self, values=[nombre for _, nombre in filas], state="readonly")
        self.categorias.pack(fill="x")
        self.categorias.bind("<<ComboboxSelected>>", lambda evento: self.al_elegir())
        self.productos = tk.Listbox(self, width=40, height=12)
        self.productos.pack(fill="both", expand=True, pady=5)
        self.contador = tk.Label(self, text="")
        self.contador.pack(anchor="w")

    def al_elegir(self):
        id_categoria = self.ids[self.categorias.get()]
        with closing(self.con.cursor()) as cursor:
            cursor.execute(
                "SELECT ProductName FROM Products WHERE CategoryID = %s ORDER BY ProductName",
                (id_categoria,),
            )
            nombres = [fila[0] for fila in cursor.fetchall()]
        self.productos.delete(0, tk.END)
        for nombre in nombres:
            self.productos.insert(tk.END, nombre)
        self.contador.config(text=f"{len(nombres)} productos")


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    ref = con.cursor(buffered=True)
    ref.execute("SELECT CategoryID, CategoryName FROM Categories ORDER BY CategoryName")
    categorias = ref.fetchall()

    raiz = tk.Tk()
    raiz.withdraw()
    app = ProductosPorCategoria(raiz, con)
    assert list(app.categorias.cget("values")) == [nombre for _, nombre in categorias]
    assert str(app.categorias.cget("state")) == "readonly"
    assert app.ids == {nombre: id_categoria for id_categoria, nombre in categorias}

    for id_categoria, nombre in categorias[:2]:
        app.categorias.set(nombre)
        app.al_elegir()
        ref.execute("SELECT ProductName FROM Products WHERE CategoryID = %s ORDER BY ProductName", (id_categoria,))
        esperado = tuple(fila[0] for fila in ref.fetchall())
        assert app.productos.get(0, tk.END) == esperado, nombre
        assert app.contador.cget("text") == f"{len(esperado)} productos"

    assert app.categorias.bind("<<ComboboxSelected>>"), "Conecta al_elegir al evento <<ComboboxSelected>>"
    ref.close()
    raiz.destroy()
    con.close()
    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        con = mysql.connector.connect(**CONFIG)
        raiz = tk.Tk()
        raiz.title("Productos por categoría")
        ProductosPorCategoria(raiz, con).pack(fill="both", expand=True, padx=10, pady=10)
        raiz.mainloop()
        con.close()
