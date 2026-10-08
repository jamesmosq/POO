"""
Solución - Ejercicio para corregir 01 - Llamada mal hecha

CORRECCIÓN 1 (según la versión del conector: "Not all parameters were used
in the SQL statement" o "1064 You have an error in your SQL syntax"):
execute() envía el texto tal cual como SQL, y "ej_nombre_producto" solo no
es una sentencia válida (ni tiene un %s para el parámetro). Para llamar un
procedimiento se usa callproc (o CALL nombre(%s)).

CORRECCIÓN 2 (InterfaceError: No result set to fetch from): los resultados
de un procedimiento no quedan en el cursor principal. Se leen recorriendo
cursor.stored_results().
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
        cursor.callproc("ej_nombre_producto", [id_producto])  # CORRECCIÓN 1
        filas = []
        for resultado in cursor.stored_results():  # CORRECCIÓN 2
            filas.extend(resultado.fetchall())
        return filas[0][0] if filas else None


# ----------------------------------------------------------------------
# Pruebas
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
