"""
Solución - Ejercicio propuesto 02 - Buscar con filtro
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


class BuscadorProductos(tk.Frame):
    SQL = """
        SELECT p.ProductName, c.CategoryName, p.Price
        FROM Products p JOIN Categories c ON c.CategoryID = p.CategoryID
        WHERE p.ProductName LIKE %s
        ORDER BY p.ProductName
    """

    def __init__(self, master, con):
        super().__init__(master)
        self.con = con
        barra = tk.Frame(self)
        barra.pack(fill="x", pady=5)
        self.filtro = tk.Entry(barra, width=30)
        self.filtro.pack(side="left", padx=5)
        self.filtro.bind("<Return>", lambda evento: self.buscar())
        self.boton_buscar = tk.Button(barra, text="Buscar", command=self.buscar)
        self.boton_buscar.pack(side="left")

        self.tabla = ttk.Treeview(self, columns=("nombre", "categoria", "precio"), show="headings", height=15)
        for columna, titulo in (("nombre", "Producto"), ("categoria", "Categoría"), ("precio", "Precio")):
            self.tabla.heading(columna, text=titulo)
        self.tabla.pack(fill="both", expand=True)
        self.resultado = tk.Label(self, text="")
        self.resultado.pack(anchor="w", padx=5)
        self.buscar()

    def buscar(self):
        texto = self.filtro.get().strip()
        with closing(self.con.cursor()) as cursor:
            cursor.execute(self.SQL, (f"%{texto}%",))
            filas = cursor.fetchall()
        self.tabla.delete(*self.tabla.get_children())
        for fila in filas:
            self.tabla.insert("", tk.END, values=fila)
        self.resultado.config(text=f"{len(filas)} resultados")


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    ref = con.cursor(buffered=True)
    ref.execute("SELECT COUNT(*) FROM Products")
    total = ref.fetchone()[0]
    ref.execute("""
        SELECT p.ProductName, c.CategoryName FROM Products p
        JOIN Categories c ON c.CategoryID = p.CategoryID
        WHERE p.ProductName LIKE '%Chef%' ORDER BY p.ProductName
    """)
    chef = ref.fetchall()
    ref.close()

    raiz = tk.Tk()
    raiz.withdraw()
    app = BuscadorProductos(raiz, con)
    assert len(app.tabla.get_children()) == total
    assert app.resultado.cget("text") == f"{total} resultados"

    app.filtro.insert(0, "Chef")
    app.boton_buscar.invoke()
    filas = [app.tabla.item(i, "values") for i in app.tabla.get_children()]
    assert [(f[0], f[1]) for f in filas] == chef, filas
    assert app.resultado.cget("text") == f"{len(chef)} resultados"

    app.filtro.delete(0, tk.END)
    app.filtro.insert(0, "' OR '1'='1")
    app.boton_buscar.invoke()
    assert app.resultado.cget("text") == "0 resultados", "La búsqueda debe usar parámetros"
    assert app.filtro.bind("<Return>"), "La tecla Enter también debe buscar"
    raiz.destroy()
    con.close()
    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        con = mysql.connector.connect(**CONFIG)
        raiz = tk.Tk()
        raiz.title("Buscar productos")
        BuscadorProductos(raiz, con).pack(fill="both", expand=True)
        raiz.mainloop()
        con.close()
