"""
Ejercicio para corregir 01 - Contar productos
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    contar_productos(con) retorna la cantidad de productos como un número
    entero (por ejemplo 77), no como una lista ni como una tupla.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""
import os
from contextlib import closing

import mysql.conector

CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "base1234"),
    "database": os.getenv("DB_NAME", "northwind"),
}


def contar_productos(con):
    with closing(con.cursor()) as cursor:
        cursor.execute("SELECT COUNT(*) FROM Products")
        return cursor.fetchall()


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import mysql.connector

    con = mysql.connector.connect(**CONFIG)
    total = contar_productos(con)
    assert isinstance(total, int), f"Se esperaba un entero y se obtuvo {total!r}"
    assert total > 0
    con.close()
    print("Todas las pruebas pasaron")
