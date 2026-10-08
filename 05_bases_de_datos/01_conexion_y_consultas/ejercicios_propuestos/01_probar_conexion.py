"""
Ejercicio propuesto 01 - Probar la conexión
Nivel: básico

Antes de empezar: este tema usa la base de datos Northwind en MySQL o
MariaDB (ver 05_bases_de_datos/README.md). Ajusta CONFIG con tus datos o
define las variables de entorno DB_PASSWORD, DB_NAME, etc.

Requisitos:
1. conectar(): retorna una conexión creada con mysql.connector.connect(**CONFIG).
2. version_servidor(con): ejecuta SELECT VERSION() y retorna el texto.
3. contar_registros(con, tabla): retorna cuántas filas tiene la tabla.
   Solo acepta tablas de la lista TABLAS_PERMITIDAS; para cualquier otra
   lanza ValueError. (Los nombres de tabla no se pueden pasar como
   parámetro %s, por eso se validan contra una lista.)
4. Cierra siempre el cursor:
       with closing(con.cursor()) as cursor:
   closing() (del módulo contextlib) llama a cursor.close() al salir del
   bloque, aunque ocurra un error. Funciona con cualquier versión del
   conector.

Conceptos: conexión, cursor, execute, fetchone, cerrar recursos.
"""
import os
from contextlib import closing

import mysql.connector

# Datos de conexión. Cambia los valores por defecto o define las variables
# de entorno DB_HOST, DB_USER, DB_PASSWORD y DB_NAME.
CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "northwind"),
}

TABLAS_PERMITIDAS = ["Products", "Customers", "Employees", "Orders", "Categories", "Suppliers", "Shippers"]

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
