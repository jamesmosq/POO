"""
Ejercicio para corregir 01 - Llamada mal hecha
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    nombre_producto(con, id) llama al procedimiento ej_nombre_producto y
    retorna el nombre del producto, o None si no existe.

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


def preparar(con):
    """Crea el procedimiento que usa este ejercicio. Este código está bien."""
    with closing(con.cursor()) as cursor:
        cursor.execute("DROP PROCEDURE IF EXISTS ej_nombre_producto")
        cursor.execute("""
            CREATE PROCEDURE ej_nombre_producto(IN p_id INT)
            BEGIN
                SELECT ProductName FROM Products WHERE ProductID = p_id;
            END
        """)


def nombre_producto(con, id_producto):
    with closing(con.cursor()) as cursor:
        cursor.execute("ej_nombre_producto", (id_producto,))
        filas = cursor.fetchall()
        return filas[0][0] if filas else None


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    preparar(con)
    ref = con.cursor(buffered=True)
    ref.execute("SELECT ProductID, ProductName FROM Products ORDER BY ProductID LIMIT 1")
    id_producto, nombre = ref.fetchone()
    ref.close()
    assert nombre_producto(con, id_producto) == nombre, nombre_producto(con, id_producto)
    assert nombre_producto(con, -1) is None
    con.close()
    print("Todas las pruebas pasaron")
