"""
Solución - Ejercicio propuesto 05 - Maestro y detalle
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
        clientes = self._consultar("""
            SELECT c.CustomerID, c.CustomerName FROM Customers c
            WHERE EXISTS (SELECT 1 FROM Orders o WHERE o.CustomerID = c.CustomerID)
            ORDER BY c.CustomerName
        """)
        self.ids_clientes = {nombre: id_cliente for id_cliente, nombre in clientes}
        self.clientes = ttk.Combobox(self, values=[n for _, n in clientes], state="readonly", width=40)
        self.clientes.pack(fill="x")
        self.clientes.bind("<<ComboboxSelected>>", lambda evento: self.al_elegir_cliente())

        self.pedidos = self._crear_tabla(("pedido", "fecha", "total"), ("Pedido", "Fecha", "Total"))
        self.pedidos.bind("<<TreeviewSelect>>", lambda evento: self.al_elegir_pedido())
        self.detalle = self._crear_tabla(("producto", "cantidad", "subtotal"), ("Producto", "Cantidad", "Subtotal"))
        self.total = tk.Label(self, text="", font=("Arial", 11, "bold"))
        self.total.pack(anchor="e")

    def _crear_tabla(self, columnas, titulos):
        tabla = ttk.Treeview(self, columns=columnas, show="headings", height=6)
        for columna, titulo in zip(columnas, titulos):
            tabla.heading(columna, text=titulo)
        tabla.pack(fill="both", expand=True, pady=5)
        return tabla

    def _consultar(self, sql, parametros=()):
        with closing(self.con.cursor()) as cursor:
            cursor.execute(sql, parametros)
            return cursor.fetchall()

    def al_elegir_cliente(self):
        id_cliente = self.ids_clientes[self.clientes.get()]
        filas = self._consultar("""
            SELECT o.OrderID, o.OrderDate, SUM(d.Quantity * p.Price)
            FROM Orders o
            JOIN OrderDetails d ON d.OrderID = o.OrderID
            JOIN Products p ON p.ProductID = d.ProductID
            WHERE o.CustomerID = %s
            GROUP BY o.OrderID, o.OrderDate
            ORDER BY o.OrderDate, o.OrderID
        """, (id_cliente,))
        self.pedidos.delete(*self.pedidos.get_children())
        for id_pedido, fecha, total in filas:
            self.pedidos.insert("", tk.END, iid=str(id_pedido),
                                values=(id_pedido, fecha.strftime("%Y-%m-%d"), f"{float(total):.2f}"))
        # El detalle mostrado era de otro cliente: se limpia.
        self.detalle.delete(*self.detalle.get_children())
        self.total.config(text="")

    def al_elegir_pedido(self):
        seleccion = self.pedidos.selection()
        if not seleccion:
            return
        filas = self._consultar("""
            SELECT p.ProductName, d.Quantity, d.Quantity * p.Price
            FROM OrderDetails d JOIN Products p ON p.ProductID = d.ProductID
            WHERE d.OrderID = %s
        """, (seleccion[0],))
        self.detalle.delete(*self.detalle.get_children())
        total = 0
        for nombre, cantidad, subtotal in filas:
            self.detalle.insert("", tk.END, values=(nombre, cantidad, f"{float(subtotal):.2f}"))
            total += float(subtotal)
        self.total.config(text=f"Total: ${total:,.2f}")


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    ref = con.cursor(buffered=True)
    ref.execute("""
        SELECT c.CustomerID, c.CustomerName FROM Customers c
        WHERE EXISTS (SELECT 1 FROM Orders o WHERE o.CustomerID = c.CustomerID)
        ORDER BY c.CustomerName
    """)
    clientes = ref.fetchall()

    raiz = tk.Tk()
    raiz.withdraw()
    app = PedidosPorCliente(raiz, con)
    assert list(app.clientes.cget("values")) == [n for _, n in clientes]

    id_cliente, nombre = clientes[0]
    app.clientes.set(nombre)
    app.al_elegir_cliente()
    ref.execute("""
        SELECT o.OrderID, o.OrderDate, SUM(d.Quantity * p.Price)
        FROM Orders o JOIN OrderDetails d ON d.OrderID = o.OrderID JOIN Products p ON p.ProductID = d.ProductID
        WHERE o.CustomerID = %s GROUP BY o.OrderID, o.OrderDate ORDER BY o.OrderDate, o.OrderID
    """, (id_cliente,))
    pedidos = ref.fetchall()
    filas = [app.pedidos.item(i, "values") for i in app.pedidos.get_children()]
    esperado = [(str(i), fecha.strftime("%Y-%m-%d"), f"{float(t):.2f}") for i, fecha, t in pedidos]
    assert [tuple(f) for f in filas] == esperado, filas

    pedido = str(pedidos[0][0])
    app.pedidos.selection_set(pedido)
    app.al_elegir_pedido()
    ref.execute("SELECT COUNT(*) FROM OrderDetails WHERE OrderID = %s", (pedido,))
    assert len(app.detalle.get_children()) == ref.fetchone()[0]
    assert app.total.cget("text") == f"Total: ${float(pedidos[0][2]):,.2f}"

    app.clientes.set(clientes[1][1])
    app.al_elegir_cliente()
    assert app.detalle.get_children() == () and app.total.cget("text") == "", (
        "Al cambiar de cliente se debe limpiar el detalle"
    )
    ref.close()
    raiz.destroy()
    con.close()
    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        con = mysql.connector.connect(**CONFIG)
        raiz = tk.Tk()
        raiz.title("Pedidos por cliente")
        PedidosPorCliente(raiz, con).pack(fill="both", expand=True, padx=10, pady=10)
        raiz.mainloop()
        con.close()
