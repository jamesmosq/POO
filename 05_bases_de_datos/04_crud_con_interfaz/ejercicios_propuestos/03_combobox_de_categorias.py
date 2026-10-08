"""
Ejercicio propuesto 03 - Combobox de categorías
Nivel: intermedio

Un Combobox muestra textos, pero la base de datos trabaja con ids. Hay que
guardar la relación entre el texto que ve el usuario y el id que usa la
consulta.

Requisitos. Crea la clase ProductosPorCategoria(tk.Frame) que recibe
(master, con):
1. self.categorias: ttk.Combobox de solo lectura, con los nombres de las
   categorías en orden alfabético.
2. self.ids: diccionario nombre_de_categoria -> CategoryID.
3. self.productos: Listbox con los nombres de los productos de la
   categoría elegida, en orden alfabético.
4. self.contador: Label "N productos".
5. al_elegir(): lee la categoría elegida, busca sus productos (con el id,
   no con el nombre) y llena el Listbox, borrando lo anterior.
   Conéctalo al evento "<<ComboboxSelected>>".

Conceptos: Combobox, eventos virtuales, separar lo que se muestra del id.
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

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
