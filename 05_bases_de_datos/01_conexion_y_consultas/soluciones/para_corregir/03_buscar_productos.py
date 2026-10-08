"""
Solución - Ejercicio para corregir 03 - Buscar productos

CORRECCIÓN 1 (ProgrammingError: según la versión del conector dice "Could
not process parameters" o "1064 You have an error in your SQL syntax"):
(texto) no es una tupla, es solo texto entre paréntesis. El conector
recibe un str donde espera una secuencia de parámetros. Una tupla de un
elemento necesita la coma: (texto,).

CORRECCIÓN 2 (no encontraba nada): sin comodines, LIKE "Chef" solo
encuentra nombres que sean exactamente "Chef". Para buscar "que contenga"
se agregan % al valor: f"%{texto}%".
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
    with closing(con.cursor(buffered=True)) as cursor:
        cursor.execute(
            "SELECT ProductName FROM Products WHERE ProductName LIKE %s ORDER BY ProductName",
            (f"%{texto}%",),  # CORRECCIÓN 1 y 2
        )
        return [fila[0] for fila in cursor.fetchall()]


# ----------------------------------------------------------------------
# Pruebas
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
