"""
Ejercicio para corregir 04 - Ventas por categoría
Nivel: intermedio
Errores a encontrar: 3

Qué debería hacer el programa:
    unidades_por_categoria(con) retorna una lista de tuplas
    (CategoryName, unidades_vendidas), donde unidades_vendidas es la SUMA
    de Quantity de OrderDetails de los productos de esa categoría. Va de la
    categoría que más vendió a la que menos.

Ojo: la consulta se ejecuta sin errores, pero los números no son los
correctos. Ejecuta la consulta por partes en tu cliente SQL para ver qué
está uniendo cada JOIN.

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


def unidades_por_categoria(con):
    sql = """
        SELECT c.CategoryName, COUNT(d.Quantity) AS unidades
        FROM OrderDetails d
        JOIN Products p ON p.ProductID = d.ProductID
        JOIN Categories c ON c.CategoryID = p.SupplierID
        GROUP BY c.CategoryID, c.CategoryName
        ORDER BY unidades
    """
    with closing(con.cursor()) as cursor:
        cursor.execute(sql)
        return [(nombre, int(unidades)) for nombre, unidades in cursor.fetchall()]


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
