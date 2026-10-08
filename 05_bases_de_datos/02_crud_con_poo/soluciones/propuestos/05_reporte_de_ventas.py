"""
Solución - Ejercicio propuesto 05 - Reporte de ventas
"""

import os
from contextlib import closing

import mysql.connector

CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "northwind"),
}

import csv


class ReporteVentas:
    def __init__(self, con):
        self.con = con

    def _consultar(self, sql, parametros=()):
        with closing(self.con.cursor(buffered=True)) as cursor:
            cursor.execute(sql, parametros)
            return cursor.fetchall()

    def total_pedido(self, order_id):
        filas = self._consultar("""
            SELECT COALESCE(SUM(d.Quantity * p.Price), 0)
            FROM OrderDetails d JOIN Products p ON p.ProductID = d.ProductID
            WHERE d.OrderID = %s
        """, (order_id,))
        return float(filas[0][0])

    def mejores_clientes(self, n):
        filas = self._consultar("""
            SELECT c.CustomerName, ROUND(SUM(d.Quantity * p.Price), 2) AS total
            FROM Customers c
            JOIN Orders o ON o.CustomerID = c.CustomerID
            JOIN OrderDetails d ON d.OrderID = o.OrderID
            JOIN Products p ON p.ProductID = d.ProductID
            GROUP BY c.CustomerID, c.CustomerName
            ORDER BY total DESC
            LIMIT %s
        """, (n,))
        return [(nombre, float(total)) for nombre, total in filas]

    def ventas_por_mes(self, anio):
        filas = self._consultar("""
            SELECT MONTH(o.OrderDate) AS mes, SUM(d.Quantity * p.Price)
            FROM Orders o
            JOIN OrderDetails d ON d.OrderID = o.OrderID
            JOIN Products p ON p.ProductID = d.ProductID
            WHERE YEAR(o.OrderDate) = %s
            GROUP BY mes ORDER BY mes
        """, (anio,))
        return {int(mes): float(total) for mes, total in filas}

    def exportar_csv(self, ruta, n):
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["cliente", "total"])
            escritor.writerows(self.mejores_clientes(n))


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import csv
    import tempfile

    con = mysql.connector.connect(**CONFIG)
    ref = con.cursor(buffered=True)
    reporte = ReporteVentas(con)

    ref.execute("SELECT MIN(OrderID) FROM Orders")
    pedido = ref.fetchone()[0]
    ref.execute("""
        SELECT SUM(d.Quantity * p.Price) FROM OrderDetails d
        JOIN Products p ON p.ProductID = d.ProductID WHERE d.OrderID = %s
    """, (pedido,))
    assert round(reporte.total_pedido(pedido), 2) == round(float(ref.fetchone()[0]), 2)
    assert reporte.total_pedido(-1) == 0.0

    ref.execute("""
        SELECT c.CustomerName, ROUND(SUM(d.Quantity * p.Price), 2) AS total
        FROM Customers c JOIN Orders o ON o.CustomerID = c.CustomerID
        JOIN OrderDetails d ON d.OrderID = o.OrderID JOIN Products p ON p.ProductID = d.ProductID
        GROUP BY c.CustomerID, c.CustomerName ORDER BY total DESC LIMIT 3
    """)
    esperado = [(n, float(t)) for n, t in ref.fetchall()]
    assert reporte.mejores_clientes(3) == esperado, reporte.mejores_clientes(3)

    ref.execute("SELECT YEAR(OrderDate) FROM Orders GROUP BY YEAR(OrderDate) ORDER BY COUNT(*) DESC LIMIT 1")
    anio = ref.fetchone()[0]
    por_mes = reporte.ventas_por_mes(anio)
    assert por_mes and all(1 <= mes <= 12 for mes in por_mes)
    ref.execute("""
        SELECT SUM(d.Quantity * p.Price) FROM Orders o JOIN OrderDetails d ON d.OrderID = o.OrderID
        JOIN Products p ON p.ProductID = d.ProductID WHERE YEAR(o.OrderDate) = %s
    """, (anio,))
    assert round(sum(por_mes.values()), 2) == round(float(ref.fetchone()[0]), 2)

    ruta = os.path.join(tempfile.mkdtemp(), "clientes.csv")
    reporte.exportar_csv(ruta, 3)
    with open(ruta, newline="", encoding="utf-8") as archivo:
        filas = list(csv.reader(archivo))
    assert filas[0] == ["cliente", "total"]
    assert [(f[0], float(f[1])) for f in filas[1:]] == esperado

    ref.close()
    con.close()
    print("Todas las pruebas pasaron")
