"""
Solución - Ejercicio para corregir 05 - Pedido a medias

CORRECCIÓN 1 (quedaba un pedido sin detalles): el commit justo después de
insertar el encabezado lo dejaba guardado de forma definitiva. Si luego
fallaba un detalle, ya no había vuelta atrás. En una transacción se hace UN
solo commit, al final.

CORRECCIÓN 2 (el pedido fallido seguía pendiente en la conexión): el
except volvía a lanzar el error sin deshacer los cambios. Antes de relanzar
hay que llamar a con.rollback().

CORRECCIÓN 3 (retornaba el id equivocado): cursor.lastrowid siempre tiene
el id del ÚLTIMO insert, que era un detalle. El id del pedido se guarda en
una variable justo después de insertar el encabezado.
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
    with closing(con.cursor(buffered=True)) as cursor:
        try:
            cursor.execute(
                "INSERT INTO Orders (CustomerID, EmployeeID, OrderDate, ShipperID) VALUES (%s, %s, %s, %s)",
                (customer_id, employee_id, fecha, shipper_id),
            )
            pedido_id = cursor.lastrowid  # CORRECCIÓN 1: sin commit aquí
            for product_id, cantidad in items:
                cursor.execute("SELECT COUNT(*) FROM Products WHERE ProductID = %s", (product_id,))
                if cursor.fetchone()[0] == 0:
                    raise ValueError(f"No existe el producto {product_id}")
                cursor.execute(
                    "INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES (%s, %s, %s)",
                    (pedido_id, product_id, cantidad),
                )
            con.commit()
            return pedido_id  # CORRECCIÓN 3
        except Exception:
            con.rollback()  # CORRECCIÓN 2
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

        try:
            crear_pedido(con, cliente, empleado, transportadora, [(producto, 1), (-99, 1)], FECHA_DE_PRUEBA)
            raise AssertionError("Debe lanzar ValueError")
        except ValueError:
            pass
        quedaron = contar(con, "SELECT COUNT(*) FROM Orders WHERE OrderDate = %s", (FECHA_DE_PRUEBA,))
        assert quedaron == 0, f"Quedaron {quedaron} pedido(s) a medias en la base de datos"

        pedido = crear_pedido(con, cliente, empleado, transportadora, [(producto, 3), (producto + 1, 2)], FECHA_DE_PRUEBA)
        real = contar(con, "SELECT OrderID FROM Orders WHERE OrderDate = %s", (FECHA_DE_PRUEBA,))
        assert pedido == real, f"Se retornó {pedido}, pero el pedido creado es el {real}"
        assert contar(con, "SELECT COUNT(*) FROM OrderDetails WHERE OrderID = %s", (real,)) == 2
    finally:
        con.rollback()
        cursor = con.cursor()
        cursor.execute("DELETE FROM OrderDetails WHERE OrderID IN (SELECT OrderID FROM Orders WHERE OrderDate = %s)", (FECHA_DE_PRUEBA,))
        cursor.execute("DELETE FROM Orders WHERE OrderDate = %s", (FECHA_DE_PRUEBA,))
        con.commit()
        cursor.close()
        con.close()

    print("Todas las pruebas pasaron")
