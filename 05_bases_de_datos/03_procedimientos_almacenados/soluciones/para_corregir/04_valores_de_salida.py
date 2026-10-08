"""
Solución - Ejercicio para corregir 04 - Valores de salida

CORRECCIÓN 1 (la cantidad y el máximo salían en 3 y 0): callproc no
modifica la lista que se le envía; RETORNA una tupla nueva con los valores
finales de todos los parámetros. Hay que guardar ese resultado.

CORRECCIÓN 2: en la tupla, la posición 0 es el parámetro IN (la
categoría). La cantidad es la posición 1 y el máximo la 2.

CORRECCIÓN 3 (valores intercambiados): en SELECT ... INTO, los valores se
asignan en el MISMO orden en que aparecen las columnas: COUNT(*) va a
p_cantidad y MAX(Price) a p_maximo.
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
CREATE PROCEDURE ej_resumen_categoria(IN p_categoria INT, OUT p_cantidad INT, OUT p_maximo DECIMAL(10,2))
BEGIN
    SELECT COUNT(*), MAX(Price) INTO p_cantidad, p_maximo
    FROM Products WHERE CategoryID = p_categoria;
END
"""  # CORRECCIÓN 3


def crear_procedimiento(con):
    with closing(con.cursor()) as cursor:
        cursor.execute("DROP PROCEDURE IF EXISTS ej_resumen_categoria")
        cursor.execute(SQL_CREAR)


def resumen(con, categoria):
    with closing(con.cursor()) as cursor:
        resultado = cursor.callproc("ej_resumen_categoria", [categoria, 0, 0])  # CORRECCIÓN 1
        cantidad = resultado[1]  # CORRECCIÓN 2
        maximo = resultado[2]
        return int(cantidad), float(maximo)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    crear_procedimiento(con)
    ref = con.cursor(buffered=True)
    ref.execute("SELECT COUNT(*), MAX(Price) FROM Products WHERE CategoryID = 3")
    cantidad, maximo = ref.fetchone()
    ref.close()
    assert resumen(con, 3) == (cantidad, float(maximo)), f"Se obtuvo {resumen(con, 3)}, se esperaba {(cantidad, float(maximo))}"
    con.close()
    print("Todas las pruebas pasaron")
