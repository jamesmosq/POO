"""
Solución - Ejercicio para corregir 04 - Ventas por categoría

CORRECCIÓN 1: el JOIN con Categories usaba p.SupplierID. La columna que
relaciona un producto con su categoría es p.CategoryID. Un JOIN con la
columna equivocada no da error: simplemente une filas que no tienen nada
que ver.

CORRECCIÓN 2: COUNT(d.Quantity) cuenta cuántas FILAS hay, no cuántas
unidades. Para sumar las cantidades se usa SUM.

CORRECCIÓN 3: ORDER BY sin DESC ordena de menor a mayor.
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


def unidades_por_categoria(con):
    sql = """
        SELECT c.CategoryName, SUM(d.Quantity) AS unidades
        FROM OrderDetails d
        JOIN Products p ON p.ProductID = d.ProductID
        JOIN Categories c ON c.CategoryID = p.CategoryID
        GROUP BY c.CategoryID, c.CategoryName
        ORDER BY unidades DESC
    """
    # CORRECCIÓN 1: p.CategoryID   CORRECCIÓN 2: SUM   CORRECCIÓN 3: DESC
    with closing(con.cursor(buffered=True)) as cursor:
        cursor.execute(sql)
        return [(nombre, int(unidades)) for nombre, unidades in cursor.fetchall()]


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    ref = con.cursor(buffered=True)
    ref.execute("""
        SELECT c.CategoryName, SUM(d.Quantity) FROM OrderDetails d
        JOIN Products p ON p.ProductID = d.ProductID
        JOIN Categories c ON c.CategoryID = p.CategoryID
        GROUP BY c.CategoryID, c.CategoryName ORDER BY SUM(d.Quantity) DESC
    """)
    esperado = [(n, int(u)) for n, u in ref.fetchall()]
    obtenido = unidades_por_categoria(con)
    assert obtenido == esperado, f"\nObtenido: {obtenido}\nEsperado: {esperado}"
    ref.close()
    con.close()
    print("Todas las pruebas pasaron")
