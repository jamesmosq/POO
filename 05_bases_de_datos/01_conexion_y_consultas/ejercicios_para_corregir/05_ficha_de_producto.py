"""
Ejercicio para corregir 05 - Ficha de producto
Nivel: avanzado
Errores a encontrar: 3

Qué debería hacer el programa:
    ficha_producto(con, product_id) retorna un diccionario con el producto
    y su categoría, o None si el producto no existe:
        {"ProductName": "Chai", "Price": 18.0, "CategoryName": "Beverages"}

    contar_productos_caros(con, minimo) retorna cuántos productos cuestan
    más que minimo.

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
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "northwind"),
}


def ficha_producto(con, product_id):
    sql = """
        SELECT p.ProductName, p.Price, c.CategoryName
        FROM Products p JOIN Categories c ON c.CategoryID = p.CategoryID
        WHERE p.ProductID = %s
    """
    with closing(con.cursor()) as cursor:
        cursor.execute(sql, (product_id,))
        fila = cursor.fetchone()
        return {"ProductName": fila["ProductName"], "Price": float(fila["Price"]), "CategoryName": fila["CategoryName"]}


def contar_productos_caros(con, minimo):
    with closing(con.cursor()) as cursor:
        cursor.execute("SELECT ProductID FROM Products WHERE Price > %s", (minimo,))
        return cursor.rowcount


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
