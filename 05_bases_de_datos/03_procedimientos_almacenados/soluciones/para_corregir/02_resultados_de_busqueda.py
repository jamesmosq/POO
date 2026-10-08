"""
Solución - Ejercicio para corregir 02 - Resultados de búsqueda

CORRECCIÓN 1 (error con los argumentos): callproc espera una lista o tupla
con un elemento por parámetro, aunque el procedimiento tenga uno solo.
Según la versión del conector el mensaje es "args must be a sequence" o
"Incorrect number of arguments".

CORRECCIÓN 2 (retornaba tuplas): cada resultado es un cursor que entrega
filas, y cada fila es una tupla. Hay que sacar la primera columna de cada
fila.
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

def preparar(con):
    """Crea el procedimiento que usa este ejercicio. Este código está bien."""
    with closing(con.cursor()) as cursor:
        cursor.execute("DROP PROCEDURE IF EXISTS ej_buscar_nombres")
        cursor.execute("""
            CREATE PROCEDURE ej_buscar_nombres(IN p_texto VARCHAR(50))
            BEGIN
                SELECT ProductName FROM Products
                WHERE ProductName LIKE CONCAT('%', p_texto, '%') ORDER BY ProductName;
            END
        """)


def buscar(con, texto):
    with closing(con.cursor()) as cursor:
        cursor.callproc("ej_buscar_nombres", [texto])  # CORRECCIÓN 1
        for resultado in cursor.stored_results():
            return [fila[0] for fila in resultado.fetchall()]  # CORRECCIÓN 2


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    preparar(con)
    ref = con.cursor(buffered=True)
    ref.execute("SELECT ProductName FROM Products WHERE ProductName LIKE '%Chef%' ORDER BY ProductName")
    esperado = [fila[0] for fila in ref.fetchall()]
    ref.close()
    assert buscar(con, "Chef") == esperado, buscar(con, "Chef")
    con.close()
    print("Todas las pruebas pasaron")
