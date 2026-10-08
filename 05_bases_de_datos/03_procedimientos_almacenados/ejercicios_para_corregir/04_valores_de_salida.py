"""
Ejercicio para corregir 04 - Valores de salida
Nivel: intermedio
Errores a encontrar: 3

Qué debería hacer el programa:
    El procedimiento ej_resumen_categoria(IN p_categoria, OUT p_cantidad,
    OUT p_maximo) calcula cuántos productos tiene la categoría y el precio
    más alto. resumen(con, categoria) retorna (cantidad, precio_maximo).

Ojo: el programa no lanza errores. Imprime lo que retorna callproc para
ver dónde quedó cada valor.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
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
CREATE PROCEDURE ej_resumen_categoria(IN p_categoria INT, OUT p_cantidad INT, OUT p_maximo DECIMAL(10,2))
BEGIN
    SELECT COUNT(*), MAX(Price) INTO p_maximo, p_cantidad
    FROM Products WHERE CategoryID = p_categoria;
END
"""


def crear_procedimiento(con):
    with closing(con.cursor()) as cursor:
        cursor.execute("DROP PROCEDURE IF EXISTS ej_resumen_categoria")
        cursor.execute(SQL_CREAR)


def resumen(con, categoria):
    argumentos = [categoria, 0, 0]
    with closing(con.cursor()) as cursor:
        cursor.callproc("ej_resumen_categoria", argumentos)
        cantidad = argumentos[0]
        maximo = argumentos[2]
        return int(cantidad), float(maximo)


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
