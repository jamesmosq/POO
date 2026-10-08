"""
Solución - Ejercicio para corregir 03 - Combobox con ids

CORRECCIÓN 1 (el Combobox mostraba "1 Exotic Liquids"): values recibía la
lista de tuplas (id, nombre) completa. El Combobox debe recibir solo los
nombres; el id se busca después en el diccionario self.ids.

CORRECCIÓN 2 (se acumulaban productos de varios proveedores): antes de
mostrar los productos del proveedor elegido hay que vaciar el Listbox.
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


class ProductosPorProveedor(tk.Frame):
    def __init__(self, master, con):
        super().__init__(master)
        self.con = con
        with closing(con.cursor()) as cursor:
            cursor.execute("SELECT SupplierID, SupplierName FROM Suppliers ORDER BY SupplierName")
            filas = cursor.fetchall()
        self.ids = {nombre: id_proveedor for id_proveedor, nombre in filas}
        self.proveedores = ttk.Combobox(self, values=[nombre for _, nombre in filas], state="readonly")  # CORRECCIÓN 1
        self.proveedores.pack()
        self.proveedores.bind("<<ComboboxSelected>>", lambda evento: self.al_elegir())
        self.productos = tk.Listbox(self, width=40)
        self.productos.pack()

    def al_elegir(self):
        id_proveedor = self.ids[self.proveedores.get()]
        self.productos.delete(0, tk.END)  # CORRECCIÓN 2
        with closing(self.con.cursor()) as cursor:
            cursor.execute("SELECT ProductName FROM Products WHERE SupplierID = %s ORDER BY ProductName", (id_proveedor,))
            for (nombre,) in cursor.fetchall():
                self.productos.insert(tk.END, nombre)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    ref = con.cursor(buffered=True)
    ref.execute("""
        SELECT s.SupplierID, s.SupplierName FROM Suppliers s
        WHERE EXISTS (SELECT 1 FROM Products p WHERE p.SupplierID = s.SupplierID)
        ORDER BY s.SupplierName LIMIT 2
    """)
    proveedores = ref.fetchall()

    raiz = tk.Tk()
    raiz.withdraw()
    app = ProductosPorProveedor(raiz, con)
    ref.execute("SELECT SupplierName FROM Suppliers ORDER BY SupplierName")
    nombres = [fila[0] for fila in ref.fetchall()]
    assert list(app.proveedores.cget("values")) == nombres, (
        f"El Combobox muestra {list(app.proveedores.cget('values'))[:2]}..."
    )
    for id_proveedor, nombre in proveedores:
        app.proveedores.set(nombre)
        app.al_elegir()
        ref.execute("SELECT ProductName FROM Products WHERE SupplierID = %s ORDER BY ProductName", (id_proveedor,))
        esperado = tuple(fila[0] for fila in ref.fetchall())
        assert app.productos.get(0, tk.END) == esperado, f"{nombre}: {app.productos.get(0, tk.END)}"
    ref.close()
    raiz.destroy()
    con.close()
    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        con = mysql.connector.connect(**CONFIG)
        raiz = tk.Tk()
        ProductosPorProveedor(raiz, con).pack(fill="both", expand=True)
        raiz.mainloop()
        con.close()
