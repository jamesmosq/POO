"""
Solución - Ejercicio para corregir 05 - Ficha de producto

CORRECCIÓN 1 (TypeError: tuple indices must be integers or slices, not
str): un cursor normal retorna tuplas. Para acceder por nombre de columna
se crea el cursor con dictionary=True.

CORRECCIÓN 2 (TypeError: 'NoneType' object is not subscriptable): si el
producto no existe, fetchone() retorna None. Hay que revisarlo antes de
usar la fila.

CORRECCIÓN 3 (contaba mal): en un SELECT, rowcount no es confiable antes
de leer los resultados (con el cursor por defecto vale -1). Es mejor pedirle
el conteo a la base de datos con COUNT(*).
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


def ficha_producto(con, product_id):
    sql = """
        SELECT p.ProductName, p.Price, c.CategoryName
        FROM Products p JOIN Categories c ON c.CategoryID = p.CategoryID
        WHERE p.ProductID = %s
    """
    with closing(con.cursor(dictionary=True, buffered=True)) as cursor:  # CORRECCIÓN 1
        cursor.execute(sql, (product_id,))
        fila = cursor.fetchone()
        if fila is None:  # CORRECCIÓN 2
            return None
        return {"ProductName": fila["ProductName"], "Price": float(fila["Price"]), "CategoryName": fila["CategoryName"]}


def contar_productos_caros(con, minimo):
    with closing(con.cursor(buffered=True)) as cursor:
        cursor.execute("SELECT COUNT(*) FROM Products WHERE Price > %s", (minimo,))  # CORRECCIÓN 3
        return cursor.fetchone()[0]


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    ref = con.cursor(buffered=True)
    ref.execute("""
        SELECT p.ProductID, p.ProductName, p.Price, c.CategoryName
        FROM Products p JOIN Categories c ON c.CategoryID = p.CategoryID ORDER BY p.ProductID LIMIT 1
    """)
    id_producto, nombre, precio, categoria = ref.fetchone()
    ficha = ficha_producto(con, id_producto)
    assert ficha == {"ProductName": nombre, "Price": float(precio), "CategoryName": categoria}, ficha
    assert ficha_producto(con, -1) is None

    ref.execute("SELECT COUNT(*) FROM Products WHERE Price > 50")
    esperado = ref.fetchone()[0]
    assert contar_productos_caros(con, 50) == esperado, f"Se obtuvo {contar_productos_caros(con, 50)}"
    ref.close()
    con.close()
    print("Todas las pruebas pasaron")
