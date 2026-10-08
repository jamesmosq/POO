"""
Solución - Ejercicio propuesto 03 - Crear un procedimiento
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
CREATE PROCEDURE ej_productos_por_categoria(IN p_categoria INT)
BEGIN
    SELECT ProductName, Price
    FROM Products
    WHERE CategoryID = p_categoria
    ORDER BY Price DESC;
END
"""


def crear_procedimiento(con):
    with closing(con.cursor()) as cursor:
        cursor.execute("DROP PROCEDURE IF EXISTS ej_productos_por_categoria")
        cursor.execute(SQL_CREAR)


def productos_por_categoria(con, categoria):
    with closing(con.cursor()) as cursor:
        cursor.callproc("ej_productos_por_categoria", [categoria])
        productos = []
        for resultado in cursor.stored_results():
            productos.extend((nombre, float(precio)) for nombre, precio in resultado.fetchall())
    return productos


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    crear_procedimiento(con)
    crear_procedimiento(con)  # la segunda vez no debe fallar

    ref = con.cursor(buffered=True)
    ref.execute("SELECT ProductName, Price FROM Products WHERE CategoryID = 1 ORDER BY Price DESC")
    esperado = [(n, float(p)) for n, p in ref.fetchall()]
    obtenido = productos_por_categoria(con, 1)
    assert [p for _, p in obtenido] == [p for _, p in esperado], obtenido
    assert sorted(obtenido) == sorted(esperado)
    assert productos_por_categoria(con, -1) == []
    assert "DELIMITER" not in SQL_CREAR.upper(), "DELIMITER no es SQL: no lo uses desde Python"

    ref.close()
    con.close()
    print("Todas las pruebas pasaron")
