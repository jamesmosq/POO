"""
Ejercicio propuesto 05 - Maestro y detalle
Nivel: avanzado

Una pantalla maestro-detalle muestra una lista principal y, al elegir un
elemento, sus detalles. Aquí: cliente -> sus pedidos -> productos del
pedido.

Requisitos. Crea la clase PedidosPorCliente(tk.Frame) que recibe
(master, con):
1. self.clientes: Combobox de solo lectura con los nombres de los clientes
   que tienen pedidos (orden alfabético). Guarda nombre -> CustomerID en
   self.ids_clientes.
2. self.pedidos: Treeview con columnas ("pedido", "fecha", "total"). La
   fecha en formato "1996-07-04" (sin hora) y el total con dos decimales
   ("1863.40"). Usa el OrderID como iid.
3. self.detalle: Treeview con columnas ("producto", "cantidad",
   "subtotal"), subtotal con dos decimales.
4. self.total: Label "Total: $1,863.40" del pedido elegido.
5. al_elegir_cliente(): llena self.pedidos con los pedidos del cliente
   (ordenados por fecha) y LIMPIA self.detalle y self.total.
6. al_elegir_pedido(): llena self.detalle con los productos del pedido
   seleccionado y actualiza self.total.
7. Conecta los eventos <<ComboboxSelected>> y <<TreeviewSelect>>.

Total de un pedido = suma de Quantity * Price de sus detalles.

Conceptos: maestro-detalle, varias consultas encadenadas, formato de
fechas y dinero.
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

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
