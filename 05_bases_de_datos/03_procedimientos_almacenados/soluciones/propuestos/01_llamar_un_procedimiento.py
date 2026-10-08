"""
Solución - Ejercicio propuesto 01 - Llamar un procedimiento
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
    """Crea el procedimiento que usa este ejercicio. No lo modifiques."""
    with closing(con.cursor()) as cursor:
        cursor.execute("DROP PROCEDURE IF EXISTS ej_obtener_producto")
        cursor.execute("""
            CREATE PROCEDURE ej_obtener_producto(IN p_id INT)
            BEGIN
                SELECT ProductID, ProductName, Price FROM Products WHERE ProductID = p_id;
            END
        """)


def obtener_producto(con, id_producto):
    with closing(con.cursor()) as cursor:
        cursor.callproc("ej_obtener_producto", [id_producto])
        filas = []
        for resultado in cursor.stored_results():
            filas.extend(resultado.fetchall())
    if not filas:
        return None
    id_encontrado, nombre, precio = filas[0]
    return {"id": id_encontrado, "nombre": nombre, "precio": float(precio)}


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    preparar(con)
    ref = con.cursor(buffered=True)
    ref.execute("SELECT ProductID, ProductName, Price FROM Products ORDER BY ProductID LIMIT 1")
    id_producto, nombre, precio = ref.fetchone()
    ref.close()

    assert obtener_producto(con, id_producto) == {"id": id_producto, "nombre": nombre, "precio": float(precio)}
    assert obtener_producto(con, -1) is None

    fuente = open(__file__, encoding="utf-8").read().split("# Pruebas")[0].split("# Escribe tu solución aquí")[-1]
    assert "callproc" in fuente, "Usa callproc para llamar al procedimiento"
    con.close()
    print("Todas las pruebas pasaron")
