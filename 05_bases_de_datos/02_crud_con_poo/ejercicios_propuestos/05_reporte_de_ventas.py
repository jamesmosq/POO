"""
Ejercicio propuesto 05 - Reporte de ventas
Nivel: avanzado

Requisitos. Crea la clase ReporteVentas(con):
1. total_pedido(order_id): suma de Quantity * Price de los detalles del
   pedido (el precio está en Products). Retorna un float; 0.0 si el pedido
   no tiene detalles o no existe.
2. mejores_clientes(n): lista de tuplas (CustomerName, total_comprado) con
   los n clientes que más compraron, de mayor a menor. total_comprado es un
   float redondeado a 2 decimales.
3. ventas_por_mes(anio): diccionario mes (1 a 12) -> total vendido en ese
   mes, solo con los meses que tuvieron ventas. Usa YEAR() y MONTH() sobre
   Orders.OrderDate.
4. exportar_csv(ruta, n): guarda mejores_clientes(n) en un archivo CSV con
   el encabezado "cliente,total". Usa el módulo csv (maneja bien las comas
   dentro de los nombres).

Conceptos: consultas de reporte, agregaciones con expresiones, csv.
"""
import os
from contextlib import closing

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
