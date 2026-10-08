"""
Solución - Ejercicio para corregir 03 - Crear desde Python

CORRECCIÓN 1 (1064 You have an error in your SQL syntax): DELIMITER no es
SQL; es un comando que entienden la consola de MySQL y Workbench para saber
dónde termina un bloque. Desde Python cada sentencia se envía por separado,
así que no hace falta y el servidor no lo reconoce.

CORRECCIÓN 2 (1304 PROCEDURE ej_productos_baratos already exists): la
segunda vez que se ejecuta, el procedimiento ya existe. Antes de crearlo se
ejecuta DROP PROCEDURE IF EXISTS.
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

SQL_CREAR = """
CREATE PROCEDURE ej_productos_baratos(IN p_maximo DECIMAL(10,2))
BEGIN
    SELECT ProductName FROM Products WHERE Price <= p_maximo ORDER BY ProductName;
END
"""  # CORRECCIÓN 1: sin DELIMITER


def crear_procedimiento(con):
    with closing(con.cursor()) as cursor:
        cursor.execute("DROP PROCEDURE IF EXISTS ej_productos_baratos")  # CORRECCIÓN 2
        cursor.execute(SQL_CREAR)


def productos_baratos(con, maximo):
    with closing(con.cursor()) as cursor:
        cursor.callproc("ej_productos_baratos", [maximo])
        nombres = []
        for resultado in cursor.stored_results():
            nombres.extend(fila[0] for fila in resultado.fetchall())
        return nombres


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    crear_procedimiento(con)
    crear_procedimiento(con)
    ref = con.cursor(buffered=True)
    ref.execute("SELECT ProductName FROM Products WHERE Price <= 10 ORDER BY ProductName")
    assert productos_baratos(con, 10) == [fila[0] for fila in ref.fetchall()]
    ref.close()
    con.close()
    print("Todas las pruebas pasaron")
