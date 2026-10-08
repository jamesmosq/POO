"""
Solución - Ejercicio propuesto 01 - Probar la conexión
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

TABLAS_PERMITIDAS = ["Products", "Customers", "Employees", "Orders", "Categories", "Suppliers", "Shippers"]


def conectar():
    return mysql.connector.connect(**CONFIG)


def version_servidor(con):
    with closing(con.cursor(buffered=True)) as cursor:
        cursor.execute("SELECT VERSION()")
        return cursor.fetchone()[0]


def contar_registros(con, tabla):
    # Los nombres de tabla no pueden ir como parámetro %s. Validarlos contra
    # una lista cerrada evita que se cuele SQL malicioso.
    if tabla not in TABLAS_PERMITIDAS:
        raise ValueError(f"Tabla no permitida: {tabla}")
    with closing(con.cursor(buffered=True)) as cursor:
        cursor.execute(f"SELECT COUNT(*) FROM {tabla}")
        return cursor.fetchone()[0]


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = conectar()
    assert con.is_connected()

    version = version_servidor(con)
    assert isinstance(version, str) and version[0].isdigit(), version

    referencia = con.cursor(buffered=True)
    for tabla in ("Products", "Customers"):
        referencia.execute(f"SELECT COUNT(*) FROM {tabla}")
        esperado = referencia.fetchone()[0]
        assert contar_registros(con, tabla) == esperado, tabla
    referencia.close()

    try:
        contar_registros(con, "Products; DROP TABLE Products")
        raise AssertionError("Una tabla que no está permitida debe lanzar ValueError")
    except ValueError:
        pass

    con.close()
    print("Todas las pruebas pasaron")
