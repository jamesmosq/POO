"""
Solución - Ejercicio propuesto 04 - Parámetros de salida
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

SQL_CREAR = """
CREATE PROCEDURE ej_estadisticas_categoria(
    IN p_categoria INT,
    OUT p_cantidad INT,
    OUT p_promedio DECIMAL(10,2)
)
BEGIN
    SELECT COUNT(*), AVG(Price) INTO p_cantidad, p_promedio
    FROM Products
    WHERE CategoryID = p_categoria;
END
"""


def crear_procedimiento(con):
    with closing(con.cursor()) as cursor:
        cursor.execute("DROP PROCEDURE IF EXISTS ej_estadisticas_categoria")
        cursor.execute(SQL_CREAR)


def estadisticas(con, categoria):
    with closing(con.cursor()) as cursor:
        # callproc retorna una tupla nueva: (p_categoria, p_cantidad, p_promedio)
        _, cantidad, promedio = cursor.callproc("ej_estadisticas_categoria", [categoria, 0, 0])
    promedio = round(float(promedio), 2) if promedio is not None else 0.0
    return int(cantidad), promedio


# ----------------------------------------------------------------------
# Pruebas
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
