"""
Solución - Ejercicio para corregir 02 - Buscador desfasado

CORRECCIÓN 1 (no encontraba nada): self.filtro.get sin paréntesis es el
método; dentro del f-string se convierte en un texto como
"<bound method Entry.get ...>", y ningún cliente se llama así.

CORRECCIÓN 2 (la etiqueta mostraba la cantidad anterior): el contador se
actualizaba ANTES de llenar la tabla, cuando estaba vacía. Se actualiza al
final.
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


class BuscadorClientes(tk.Frame):
    def __init__(self, master, con):
        super().__init__(master)
        self.con = con
        self.filtro = tk.Entry(self)
        self.filtro.pack()
        self.boton = tk.Button(self, text="Buscar", command=self.buscar)
        self.boton.pack()
        self.tabla = ttk.Treeview(self, columns=("nombre", "pais"), show="headings")
        self.tabla.pack()
        self.resultado = tk.Label(self, text="")
        self.resultado.pack()

    def buscar(self):
        self.tabla.delete(*self.tabla.get_children())
        with closing(self.con.cursor()) as cursor:
            cursor.execute(
                "SELECT CustomerName, Country FROM Customers WHERE CustomerName LIKE %s ORDER BY CustomerName",
                (f"%{self.filtro.get()}%",),  # CORRECCIÓN 1
            )
            for fila in cursor.fetchall():
                self.tabla.insert("", tk.END, values=fila)
        self.resultado.config(text=f"{len(self.tabla.get_children())} resultados")  # CORRECCIÓN 2


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    ref = con.cursor(buffered=True)
    ref.execute("SELECT COUNT(*) FROM Customers WHERE CustomerName LIKE '%Bon%'")
    esperado = ref.fetchone()[0]
    ref.close()

    raiz = tk.Tk()
    raiz.withdraw()
    app = BuscadorClientes(raiz, con)
    app.filtro.insert(0, "Bon")
    app.boton.invoke()
    assert len(app.tabla.get_children()) == esperado, f"La tabla tiene {len(app.tabla.get_children())} filas"
    assert app.resultado.cget("text") == f"{esperado} resultados", app.resultado.cget("text")
    raiz.destroy()
    con.close()
    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        con = mysql.connector.connect(**CONFIG)
        raiz = tk.Tk()
        BuscadorClientes(raiz, con).pack(fill="both", expand=True)
        raiz.mainloop()
        con.close()
