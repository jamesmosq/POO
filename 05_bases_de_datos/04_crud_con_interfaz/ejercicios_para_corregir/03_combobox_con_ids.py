"""
Ejercicio para corregir 03 - Combobox con ids
Nivel: intermedio
Errores a encontrar: 2

Qué debería hacer el programa:
    El Combobox muestra los NOMBRES de los proveedores. Al elegir uno, el
    Listbox muestra los productos de ese proveedor (y solo esos).

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
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


class ProductosPorProveedor(tk.Frame):
    def __init__(self, master, con):
        super().__init__(master)
        self.con = con
        with closing(con.cursor()) as cursor:
            cursor.execute("SELECT SupplierID, SupplierName FROM Suppliers ORDER BY SupplierName")
            filas = cursor.fetchall()
        self.ids = {nombre: id_proveedor for id_proveedor, nombre in filas}
        self.proveedores = ttk.Combobox(self, values=filas, state="readonly")
        self.proveedores.pack()
        self.proveedores.bind("<<ComboboxSelected>>", lambda evento: self.al_elegir())
        self.productos = tk.Listbox(self, width=40)
        self.productos.pack()

    def al_elegir(self):
        id_proveedor = self.ids[self.proveedores.get()]
        with closing(self.con.cursor()) as cursor:
            cursor.execute("SELECT ProductName FROM Products WHERE SupplierID = %s ORDER BY ProductName", (id_proveedor,))
            for (nombre,) in cursor.fetchall():
                self.productos.insert(tk.END, nombre)


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
