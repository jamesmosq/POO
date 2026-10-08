"""
Solución - Ejercicio para corregir 02 - Clientes por país

CORRECCIÓN 1 (Unknown column 'Mexico' in 'where clause'): al pegar el
texto con un f-string, la consulta queda "WHERE Country = Mexico", sin
comillas, y MySQL interpreta Mexico como el nombre de una columna. Además,
pegar textos del usuario en el SQL permite inyección SQL. Se usa un
parámetro %s y el valor va aparte, en una tupla.

CORRECCIÓN 2 (orden invertido): DESC ordena de la Z a la A. El orden
alfabético es ASC, que es el valor por defecto.
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


def clientes_de(con, pais):
    with closing(con.cursor(buffered=True)) as cursor:
        cursor.execute(
            "SELECT CustomerName FROM Customers WHERE Country = %s ORDER BY CustomerName",  # CORRECCIÓN 1 y 2
            (pais,),
        )
        return [fila[0] for fila in cursor.fetchall()]


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    ref = con.cursor(buffered=True)
    ref.execute("SELECT CustomerName FROM Customers WHERE Country = %s ORDER BY CustomerName", ("Mexico",))
    esperado = [fila[0] for fila in ref.fetchall()]
    obtenido = clientes_de(con, "Mexico")
    assert obtenido == esperado, obtenido
    ref.close()
    con.close()
    print("Todas las pruebas pasaron")
