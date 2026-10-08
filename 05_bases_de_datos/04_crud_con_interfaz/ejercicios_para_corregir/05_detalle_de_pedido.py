"""
Ejercicio para corregir 05 - Detalle de pedido
Nivel: avanzado
Errores a encontrar: 3

Qué debería hacer el programa:
    - Al elegir un cliente, self.pedidos muestra sus pedidos con la fecha
      en formato "1996-07-04" (sin hora), y el detalle anterior se limpia.
    - Al elegir un pedido, self.detalle muestra sus productos y self.total
      muestra el valor del pedido: suma de Quantity * Price, con el
      formato "Total: $1,863.40".

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
        filas = self._consultar(
            "SELECT OrderID, OrderDate FROM Orders WHERE CustomerID = %s ORDER BY OrderDate, OrderID",
            (id_cliente,),
        )
        for id_pedido, fecha in filas:
            self.pedidos.insert("", tk.END, iid=str(id_pedido), values=(id_pedido, fecha))

    def mostrar_detalle(self, id_pedido):
        filas = self._consultar("""
            SELECT p.ProductName, d.Quantity, p.Price
            FROM OrderDetails d JOIN Products p ON p.ProductID = d.ProductID
            WHERE d.OrderID = %s
        """, (id_pedido,))
        total = 0
        for nombre, cantidad, precio in filas:
            self.detalle.insert("", tk.END, values=(nombre, cantidad))
            total += cantidad
        self.total.config(text=f"Total: ${total:,.2f}")


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
