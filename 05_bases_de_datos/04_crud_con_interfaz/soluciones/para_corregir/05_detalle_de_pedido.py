"""
Solución - Ejercicio para corregir 05 - Detalle de pedido

CORRECCIÓN 1 (la fecha salía con la hora): OrderDate es DATETIME y llega
como un objeto datetime; el Treeview lo convierte a texto con la hora
incluida. Se formatea con strftime("%Y-%m-%d").

CORRECCIÓN 2 (el total era la suma de cantidades): el valor del pedido es
la suma de cantidad * precio de cada producto.

CORRECCIÓN 3 (quedaba el detalle de otro cliente): al mostrar los pedidos
de un cliente nuevo, el detalle anterior ya no corresponde y se limpia.
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


class PedidosPorCliente(tk.Frame):
    def __init__(self, master, con):
        super().__init__(master)
        self.con = con
        self.pedidos = ttk.Treeview(self, columns=("pedido", "fecha"), show="headings")
        self.pedidos.pack()
        self.detalle = ttk.Treeview(self, columns=("producto", "cantidad"), show="headings")
        self.detalle.pack()
        self.total = tk.Label(self, text="")
        self.total.pack()

    def _consultar(self, sql, parametros):
        with closing(self.con.cursor()) as cursor:
            cursor.execute(sql, parametros)
            return cursor.fetchall()

    def mostrar_pedidos(self, id_cliente):
        self.pedidos.delete(*self.pedidos.get_children())
        self.detalle.delete(*self.detalle.get_children())  # CORRECCIÓN 3
        self.total.config(text="")
        filas = self._consultar(
            "SELECT OrderID, OrderDate FROM Orders WHERE CustomerID = %s ORDER BY OrderDate, OrderID",
            (id_cliente,),
        )
        for id_pedido, fecha in filas:
            self.pedidos.insert("", tk.END, iid=str(id_pedido),
                                values=(id_pedido, fecha.strftime("%Y-%m-%d")))  # CORRECCIÓN 1

    def mostrar_detalle(self, id_pedido):
        filas = self._consultar("""
            SELECT p.ProductName, d.Quantity, p.Price
            FROM OrderDetails d JOIN Products p ON p.ProductID = d.ProductID
            WHERE d.OrderID = %s
        """, (id_pedido,))
        self.detalle.delete(*self.detalle.get_children())
        total = 0
        for nombre, cantidad, precio in filas:
            self.detalle.insert("", tk.END, values=(nombre, cantidad))
            total += cantidad * float(precio)  # CORRECCIÓN 2
        self.total.config(text=f"Total: ${total:,.2f}")


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    ref = con.cursor(buffered=True)
    ref.execute("""
        SELECT o.CustomerID, o.OrderID, DATE_FORMAT(o.OrderDate, '%Y-%m-%d'), SUM(d.Quantity * p.Price)
        FROM Orders o JOIN OrderDetails d ON d.OrderID = o.OrderID JOIN Products p ON p.ProductID = d.ProductID
        GROUP BY o.OrderID ORDER BY o.OrderID LIMIT 2
    """)
    (cliente1, pedido1, fecha1, total1), (cliente2, _, _, _) = ref.fetchall()
    ref.close()

    raiz = tk.Tk()
    raiz.withdraw()
    app = PedidosPorCliente(raiz, con)
    app.mostrar_pedidos(cliente1)
    assert app.pedidos.item(str(pedido1), "values")[1] == fecha1, app.pedidos.item(str(pedido1), "values")

    app.mostrar_detalle(pedido1)
    assert app.total.cget("text") == f"Total: ${float(total1):,.2f}", app.total.cget("text")

    app.mostrar_pedidos(cliente2)
    assert app.detalle.get_children() == (), "Al cambiar de cliente, el detalle anterior debe limpiarse"
    raiz.destroy()
    con.close()
    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        con = mysql.connector.connect(**CONFIG)
        raiz = tk.Tk()
        app = PedidosPorCliente(raiz, con)
        app.pack(fill="both", expand=True)
        app.mostrar_pedidos(cliente1)
        raiz.mainloop()
        con.close()
