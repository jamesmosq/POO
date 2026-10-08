"""
Solución - Ejercicio para corregir 01 - Tabla que se duplica

CORRECCIÓN 1 (AttributeError: 'VistaCategorias' object has no attribute
'tabla'): cargar() se llamaba en __init__ ANTES de crear la tabla. Los
widgets deben existir antes de llenarlos: cargar() va al final.

CORRECCIÓN 2 (filas repetidas al recargar): cargar() agregaba filas sobre
las que ya había. Antes de llenar la tabla hay que vaciarla.
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


class VistaCategorias(tk.Frame):
    def __init__(self, master, con):
        super().__init__(master)
        self.con = con
        self.tabla = ttk.Treeview(self, columns=("id", "nombre"), show="headings")
        self.tabla.heading("id", text="Id")
        self.tabla.heading("nombre", text="Categoría")
        self.tabla.pack(fill="both", expand=True)
        self.boton_recargar = tk.Button(self, text="Recargar", command=self.cargar)
        self.boton_recargar.pack()
        self.cargar()  # CORRECCIÓN 1

    def cargar(self):
        self.tabla.delete(*self.tabla.get_children())  # CORRECCIÓN 2
        with closing(self.con.cursor()) as cursor:
            cursor.execute("SELECT CategoryID, CategoryName FROM Categories ORDER BY CategoryName")
            for fila in cursor.fetchall():
                self.tabla.insert("", tk.END, values=fila)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    ref = con.cursor(buffered=True)
    ref.execute("SELECT COUNT(*) FROM Categories")
    total = ref.fetchone()[0]
    ref.close()

    raiz = tk.Tk()
    raiz.withdraw()
    vista = VistaCategorias(raiz, con)
    assert len(vista.tabla.get_children()) == total
    vista.boton_recargar.invoke()
    assert len(vista.tabla.get_children()) == total, f"Después de recargar hay {len(vista.tabla.get_children())} filas"
    raiz.destroy()
    con.close()
    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        con = mysql.connector.connect(**CONFIG)
        raiz = tk.Tk()
        VistaCategorias(raiz, con).pack(fill="both", expand=True)
        raiz.mainloop()
        con.close()
