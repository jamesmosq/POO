"""
Ejercicio para corregir 03 - Crear desde Python
Nivel: intermedio
Errores a encontrar: 2

Qué debería hacer el programa:
    crear_procedimiento(con) crea el procedimiento ej_productos_baratos(
    IN p_maximo DECIMAL(10,2)) y debe poder ejecutarse varias veces seguidas
    sin error. productos_baratos(con, maximo) retorna los nombres de los
    productos con precio menor o igual a maximo.

Pista: lo que funciona en la consola de MySQL no siempre funciona igual
desde Python.

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
DELIMITER //
CREATE PROCEDURE ej_productos_baratos(IN p_maximo DECIMAL(10,2))
BEGIN
    SELECT ProductName FROM Products WHERE Price <= p_maximo ORDER BY ProductName;
END //
DELIMITER ;
"""


def crear_procedimiento(con):
    with closing(con.cursor()) as cursor:
        cursor.execute(SQL_CREAR)


def productos_baratos(con, maximo):
    with closing(con.cursor()) as cursor:
        cursor.callproc("ej_productos_baratos", [maximo])
        nombres = []
        for resultado in cursor.stored_results():
            nombres.extend(fila[0] for fila in resultado.fetchall())
        return nombres


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
