"""
Ejercicio para corregir 05 - Pedido a medias
Nivel: avanzado
Errores a encontrar: 3

Qué debería hacer el programa:
    crear_pedido(con, customer_id, employee_id, shipper_id, items, fecha)
    guarda un pedido (Orders) con todos sus detalles (OrderDetails) en una
    sola transacción y retorna el OrderID del pedido.

    Si un producto no existe, lanza ValueError y NO debe quedar nada del
    pedido: ni el encabezado ni los detalles.

Ojo: el caso feliz parece funcionar. Los errores aparecen cuando algo falla
a mitad del pedido, o cuando se mira con cuidado qué id se retorna.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
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


def crear_pedido(con, customer_id, employee_id, shipper_id, items, fecha):
    with closing(con.cursor(buffered=True)) as cursor:
        try:
            cursor.execute(
                "INSERT INTO Orders (CustomerID, EmployeeID, OrderDate, ShipperID) VALUES (%s, %s, %s, %s)",
                (customer_id, employee_id, fecha, shipper_id),
            )
            con.commit()
            pedido_id = cursor.lastrowid
            for product_id, cantidad in items:
                cursor.execute("SELECT COUNT(*) FROM Products WHERE ProductID = %s", (product_id,))
                if cursor.fetchone()[0] == 0:
                    raise ValueError(f"No existe el producto {product_id}")
                cursor.execute(
                    "INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES (%s, %s, %s)",
                    (pedido_id, product_id, cantidad),
                )
            con.commit()
            return cursor.lastrowid
        except Exception:
            raise


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
