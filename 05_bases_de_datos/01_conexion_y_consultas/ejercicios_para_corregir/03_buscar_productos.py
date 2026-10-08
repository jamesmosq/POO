"""
Ejercicio para corregir 03 - Buscar productos
Nivel: intermedio
Errores a encontrar: 2

Qué debería hacer el programa:
    buscar_productos(con, texto) retorna los nombres de los productos que
    CONTIENEN el texto en cualquier parte del nombre, en orden alfabético.

        buscar_productos(con, "Chef") -> ["Chef Anton's Cajun Seasoning",
                                          "Chef Anton's Gumbo Mix"]

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


def buscar_productos(con, texto):
    with closing(con.cursor()) as cursor:
        cursor.execute(
            "SELECT ProductName FROM Products WHERE ProductName LIKE %s ORDER BY ProductName",
            (texto),
        )
        return [fila[0] for fila in cursor.fetchall()]


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    ref = con.cursor(buffered=True)
    ref.execute("SELECT ProductName FROM Products WHERE ProductName LIKE '%Chef%' ORDER BY ProductName")
    esperado = [fila[0] for fila in ref.fetchall()]
    assert buscar_productos(con, "Chef") == esperado, buscar_productos(con, "Chef")
    ref.close()
    con.close()
    print("Todas las pruebas pasaron")
