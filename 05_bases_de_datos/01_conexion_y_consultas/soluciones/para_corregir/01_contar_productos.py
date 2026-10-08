"""
Solución - Ejercicio para corregir 01 - Contar productos

CORRECCIÓN 1 (ModuleNotFoundError: No module named 'mysql.conector'): el
módulo se llama mysql.connector (con dos n).

CORRECCIÓN 2 (retornaba [(77,)]): fetchall() retorna una LISTA de filas y
cada fila es una TUPLA. Para una consulta que da un solo valor se usa
fetchone()[0]: la primera fila y su primera columna.
"""

import os
from contextlib import closing

import mysql.connector  # CORRECCIÓN 1

CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "base1234"),
    "database": os.getenv("DB_NAME", "northwind"),
}


def contar_productos(con):
    with closing(con.cursor(buffered=True)) as cursor:
        cursor.execute("SELECT COUNT(*) FROM Products")
        return cursor.fetchone()[0]  # CORRECCIÓN 2


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import mysql.connector

    con = mysql.connector.connect(**CONFIG)
    total = contar_productos(con)
    assert isinstance(total, int), f"Se esperaba un entero y se obtuvo {total!r}"
    assert total > 0
    con.close()
    print("Todas las pruebas pasaron")
