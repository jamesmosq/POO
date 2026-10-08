"""
Ejercicio propuesto 04 - Transacciones
Nivel: avanzado

Un pedido se guarda en dos tablas: Orders (el encabezado) y OrderDetails
(una fila por producto). Si falla cualquiera de los INSERT, no debe quedar
NADA guardado: ni el encabezado ni los detalles. Eso es una transacción:
todo o nada.

En mysql.connector la conexión trabaja con autocommit desactivado: todo lo
que ejecutes queda PENDIENTE hasta que llames a:
    con.commit()     # confirma todos los cambios pendientes
    con.rollback()   # o los deshace todos si algo falló
Por eso NO se debe hacer commit después de cada INSERT, sino una sola vez
al final, cuando todo salió bien.

Requisitos. Escribe crear_pedido(con, customer_id, employee_id,
shipper_id, items, fecha):
1. items es una lista de tuplas (product_id, cantidad).
2. Lanza ValueError si la lista está vacía o si alguna cantidad es <= 0.
3. Dentro de una transacción:
   - inserta el pedido en Orders con la fecha recibida;
   - por cada item verifica que el producto exista (si no, ValueError) e
     inserta el detalle en OrderDetails.
4. Si todo sale bien: commit y retorna el OrderID nuevo.
5. Si algo falla: rollback y vuelve a lanzar el error (raise).

Conceptos: transacciones, commit, rollback, integridad de los datos.
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

# Escribe tu solución aquí



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
