"""
Ejercicio propuesto 04 - JOIN y agregaciones
Nivel: intermedio

Las respuestas interesantes casi siempre necesitan datos de varias tablas.

Relaciones de Northwind que vas a usar:
    Products.CategoryID     -> Categories.CategoryID
    OrderDetails.ProductID  -> Products.ProductID
    OrderDetails.OrderID    -> Orders.OrderID
    Orders.EmployeeID       -> Employees.EmployeeID

Requisitos:
1. productos_por_categoria(con): lista de tuplas (CategoryName,
   cantidad_de_productos), de la categoría con más productos a la que
   tiene menos; si empatan, por nombre de categoría.
2. unidades_vendidas_por_producto(con, n): lista de tuplas (ProductName,
   total_unidades) con los n productos que más unidades vendieron
   (SUM(Quantity)), de mayor a menor; si empatan, por nombre.
3. pedidos_por_empleado(con): diccionario
   "Nombre Apellido" -> cantidad de pedidos, incluyendo a los empleados
   sin pedidos (con 0). Pista: LEFT JOIN y COUNT(Orders.OrderID).

Conceptos: INNER JOIN, LEFT JOIN, GROUP BY, COUNT, SUM, ORDER BY.
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
