"""
Solución - Ejercicio propuesto 04 - JOIN y agregaciones
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


def productos_por_categoria(con):
    sql = """
        SELECT c.CategoryName, COUNT(*) AS cantidad
        FROM Products p
        JOIN Categories c ON c.CategoryID = p.CategoryID
        GROUP BY c.CategoryID, c.CategoryName
        ORDER BY cantidad DESC, c.CategoryName
    """
    with closing(con.cursor(buffered=True)) as cursor:
        cursor.execute(sql)
        return [(nombre, int(cantidad)) for nombre, cantidad in cursor.fetchall()]


def unidades_vendidas_por_producto(con, n):
    sql = """
        SELECT p.ProductName, SUM(d.Quantity) AS total
        FROM OrderDetails d
        JOIN Products p ON p.ProductID = d.ProductID
        GROUP BY p.ProductID, p.ProductName
        ORDER BY total DESC, p.ProductName
        LIMIT %s
    """
    with closing(con.cursor(buffered=True)) as cursor:
        cursor.execute(sql, (n,))
        return [(nombre, int(total)) for nombre, total in cursor.fetchall()]


def pedidos_por_empleado(con):
    # LEFT JOIN conserva a los empleados sin pedidos; COUNT(o.OrderID) no
    # cuenta los NULL, así que para ellos da 0.
    sql = """
        SELECT CONCAT(e.FirstName, ' ', e.LastName) AS nombre, COUNT(o.OrderID) AS pedidos
        FROM Employees e
        LEFT JOIN Orders o ON o.EmployeeID = e.EmployeeID
        GROUP BY e.EmployeeID, nombre
    """
    with closing(con.cursor(buffered=True)) as cursor:
        cursor.execute(sql)
        return {nombre: int(pedidos) for nombre, pedidos in cursor.fetchall()}


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    ref = con.cursor(buffered=True)

    ref.execute("""
        SELECT c.CategoryName, COUNT(*) FROM Products p
        JOIN Categories c ON c.CategoryID = p.CategoryID
        GROUP BY c.CategoryID, c.CategoryName ORDER BY COUNT(*) DESC, c.CategoryName
    """)
    assert productos_por_categoria(con) == [(n, int(c)) for n, c in ref.fetchall()]

    ref.execute("""
        SELECT p.ProductName, SUM(d.Quantity) FROM OrderDetails d
        JOIN Products p ON p.ProductID = d.ProductID
        GROUP BY p.ProductID, p.ProductName ORDER BY SUM(d.Quantity) DESC, p.ProductName LIMIT 5
    """)
    esperado = [(n, int(t)) for n, t in ref.fetchall()]
    assert [(n, int(t)) for n, t in unidades_vendidas_por_producto(con, 5)] == esperado

    ref.execute("SELECT COUNT(*) FROM Employees")
    total_empleados = ref.fetchone()[0]
    ref.execute("SELECT COUNT(*) FROM Orders")
    total_pedidos = ref.fetchone()[0]
    resultado = pedidos_por_empleado(con)
    assert len(resultado) == total_empleados, "Deben aparecer todos los empleados"
    assert sum(resultado.values()) == total_pedidos
    assert all(isinstance(v, int) for v in resultado.values())

    ref.close()
    con.close()
    print("Todas las pruebas pasaron")
