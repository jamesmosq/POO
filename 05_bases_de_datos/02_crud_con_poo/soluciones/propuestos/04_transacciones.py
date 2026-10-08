"""
Solución - Ejercicio propuesto 04 - Transacciones
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


def crear_pedido(con, customer_id, employee_id, shipper_id, items, fecha):
    if not items:
        raise ValueError("El pedido no tiene productos")
    if any(cantidad <= 0 for _, cantidad in items):
        raise ValueError("Las cantidades deben ser positivas")

    with closing(con.cursor(buffered=True)) as cursor:
        try:
            cursor.execute(
                "INSERT INTO Orders (CustomerID, EmployeeID, OrderDate, ShipperID) VALUES (%s, %s, %s, %s)",
                (customer_id, employee_id, fecha, shipper_id),
            )
            pedido_id = cursor.lastrowid
            for product_id, cantidad in items:
                cursor.execute("SELECT COUNT(*) FROM Products WHERE ProductID = %s", (product_id,))
                if cursor.fetchone()[0] == 0:
                    raise ValueError(f"No existe el producto {product_id}")
                cursor.execute(
                    "INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES (%s, %s, %s)",
                    (pedido_id, product_id, cantidad),
                )
            con.commit()  # un solo commit, al final, cuando todo salió bien
            return pedido_id
        except Exception:
            con.rollback()  # deshace el encabezado y los detalles ya insertados
            raise


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
FECHA_DE_PRUEBA = "1999-09-09"


def contar(con, sql, parametros=()):
    cursor = con.cursor(buffered=True)
    cursor.execute(sql, parametros)
    valor = cursor.fetchone()[0]
    cursor.close()
    return valor


if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    try:
        cliente = contar(con, "SELECT MIN(CustomerID) FROM Customers")
        empleado = contar(con, "SELECT MIN(EmployeeID) FROM Employees")
        transportadora = contar(con, "SELECT MIN(ShipperID) FROM Shippers")
        producto = contar(con, "SELECT MIN(ProductID) FROM Products")

        pedido = crear_pedido(con, cliente, empleado, transportadora, [(producto, 3), (producto + 1, 2)], FECHA_DE_PRUEBA)
        assert contar(con, "SELECT COUNT(*) FROM Orders WHERE OrderID = %s AND OrderDate = %s", (pedido, FECHA_DE_PRUEBA)) == 1
        assert contar(con, "SELECT COUNT(*) FROM OrderDetails WHERE OrderID = %s", (pedido,)) == 2

        antes = contar(con, "SELECT COUNT(*) FROM Orders WHERE OrderDate = %s", (FECHA_DE_PRUEBA,))
        try:
            crear_pedido(con, cliente, empleado, transportadora, [(producto, 1), (-99, 1)], FECHA_DE_PRUEBA)
            raise AssertionError("Un producto inexistente debe lanzar ValueError")
        except ValueError:
            pass
        despues = contar(con, "SELECT COUNT(*) FROM Orders WHERE OrderDate = %s", (FECHA_DE_PRUEBA,))
        assert despues == antes, "Si el pedido falla no debe quedar guardado (rollback)"

        for items in ([], [(producto, 0)]):
            try:
                crear_pedido(con, cliente, empleado, transportadora, items, FECHA_DE_PRUEBA)
                raise AssertionError(f"{items} debe lanzar ValueError")
            except ValueError:
                pass
    finally:
        con.rollback()
        cursor = con.cursor()
        cursor.execute("DELETE FROM OrderDetails WHERE OrderID IN (SELECT OrderID FROM Orders WHERE OrderDate = %s)", (FECHA_DE_PRUEBA,))
        cursor.execute("DELETE FROM Orders WHERE OrderDate = %s", (FECHA_DE_PRUEBA,))
        con.commit()
        cursor.close()
        con.close()

    print("Todas las pruebas pasaron")
