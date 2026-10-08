"""
Ejercicio propuesto 02 - Buscar con filtro
Nivel: intermedio

Requisitos. Crea la clase BuscadorProductos(tk.Frame) que recibe
(master, con):
1. self.filtro: Entry donde se escribe el texto a buscar.
2. self.boton_buscar: Button "Buscar" que llama a buscar(). La tecla
   Enter dentro del Entry también busca.
3. self.tabla: Treeview con columnas ("nombre", "categoria", "precio"):
   nombre del producto, nombre de su categoría (JOIN con Categories) y
   precio.
4. self.resultado: Label "N resultados".
5. buscar(): muestra en la tabla los productos cuyo nombre contiene el
   texto (parámetro %s con LIKE), ordenados por nombre. Con el filtro
   vacío muestra todos. Borra la tabla antes de llenarla.
6. Al iniciar, ejecuta buscar() para mostrar todos los productos.

Conceptos: filtros desde la interfaz, LIKE con parámetros, JOIN.
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
