"""
Ejercicio propuesto 04 - Parámetros de salida
Nivel: intermedio

Un procedimiento puede devolver valores sueltos en parámetros OUT, sin
necesidad de un SELECT de resultados:

    CREATE PROCEDURE ejemplo(IN p_entrada INT, OUT p_salida INT)
    BEGIN
        SELECT COUNT(*) INTO p_salida FROM ... WHERE ... = p_entrada;
    END

Desde Python, callproc retorna una TUPLA NUEVA con los valores de todos
los parámetros; ahí se leen los OUT. En la lista que se envía, los OUT
llevan cualquier valor inicial (por ejemplo 0):

    resultado = cursor.callproc("ejemplo", [5, 0])
    salida = resultado[1]

Requisitos:
1. SQL_CREAR: procedimiento ej_estadisticas_categoria(IN p_categoria INT,
   OUT p_cantidad INT, OUT p_promedio DECIMAL(10,2)) que calcule la
   cantidad de productos y el precio promedio de la categoría.
2. crear_procedimiento(con): DROP PROCEDURE IF EXISTS + SQL_CREAR.
3. estadisticas(con, categoria): retorna (cantidad, promedio). El promedio
   como float redondeado a 2 decimales; si la categoría no tiene
   productos, el promedio viene NULL: retorna 0.0.

Conceptos: parámetros OUT, SELECT ... INTO, valores NULL.
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
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    crear_procedimiento(con)

    ref = con.cursor(buffered=True)
    ref.execute("SELECT COUNT(*), ROUND(AVG(Price), 2) FROM Products WHERE CategoryID = 2")
    cantidad, promedio = ref.fetchone()
    assert estadisticas(con, 2) == (cantidad, float(promedio)), estadisticas(con, 2)
    assert estadisticas(con, -1) == (0, 0.0)
    ref.close()
    con.close()
    print("Todas las pruebas pasaron")
