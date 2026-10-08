"""
Solución - Ejercicio propuesto 05 - Resultados como diccionarios
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


def consultar(con, sql, parametros=()):
    # closing() cierra el cursor aunque execute lance un error.
    with closing(con.cursor(dictionary=True, buffered=True)) as cursor:
        cursor.execute(sql, parametros)
        return cursor.fetchall()


def resumen_cliente(con, customer_id):
    sql = """
        SELECT c.CustomerName AS cliente,
               c.Country AS pais,
               COUNT(DISTINCT o.OrderID) AS pedidos,
               COALESCE(SUM(d.Quantity), 0) AS unidades
        FROM Customers c
        LEFT JOIN Orders o ON o.CustomerID = c.CustomerID
        LEFT JOIN OrderDetails d ON d.OrderID = o.OrderID
        WHERE c.CustomerID = %s
        GROUP BY c.CustomerID, c.CustomerName, c.Country
    """
    filas = consultar(con, sql, (customer_id,))
    if not filas:
        return None
    resumen = filas[0]
    resumen["pedidos"] = int(resumen["pedidos"])
    resumen["unidades"] = int(resumen["unidades"])
    return resumen


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)

    filas = consultar(con, "SELECT CategoryID, CategoryName FROM Categories WHERE CategoryID = %s", (1,))
    assert isinstance(filas, list) and isinstance(filas[0], dict), "consultar() debe retornar una lista de diccionarios"
    assert set(filas[0]) == {"CategoryID", "CategoryName"}

    try:
        consultar(con, "SELECT columna_que_no_existe FROM Categories")
        raise AssertionError("Una consulta inválida debe lanzar el error de MySQL")
    except mysql.connector.Error:
        pass

    ref = con.cursor(buffered=True)
    ref.execute("""
        SELECT c.CustomerID, c.CustomerName, c.Country, COUNT(DISTINCT o.OrderID),
               COALESCE(SUM(d.Quantity), 0)
        FROM Customers c
        LEFT JOIN Orders o ON o.CustomerID = c.CustomerID
        LEFT JOIN OrderDetails d ON d.OrderID = o.OrderID
        GROUP BY c.CustomerID ORDER BY COUNT(DISTINCT o.OrderID) DESC LIMIT 1
    """)
    id_cliente, nombre, pais, pedidos, unidades = ref.fetchone()
    resumen = resumen_cliente(con, id_cliente)
    assert resumen["cliente"] == nombre and resumen["pais"] == pais
    assert int(resumen["pedidos"]) == pedidos and int(resumen["unidades"]) == int(unidades)

    ref.execute("""
        SELECT c.CustomerID FROM Customers c LEFT JOIN Orders o ON o.CustomerID = c.CustomerID
        WHERE o.OrderID IS NULL LIMIT 1
    """)
    sin_pedidos = ref.fetchone()
    if sin_pedidos:
        resumen = resumen_cliente(con, sin_pedidos[0])
        assert int(resumen["pedidos"]) == 0 and int(resumen["unidades"]) == 0

    assert resumen_cliente(con, -1) is None

    ref.close()
    con.close()
    print("Todas las pruebas pasaron")
