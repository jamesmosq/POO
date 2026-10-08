"""
Ejercicio propuesto 01 - Llamar un procedimiento
Nivel: básico

Un procedimiento almacenado es código SQL guardado dentro de la base de
datos. Desde Python se llama con callproc, y sus resultados se leen con
stored_results():

    cursor.callproc("nombre_del_procedimiento", [argumento1, argumento2])
    for resultado in cursor.stored_results():
        filas = resultado.fetchall()

La función preparar() (ya escrita) crea en tu base de datos el
procedimiento ej_obtener_producto(p_id), que retorna ProductID,
ProductName y Price del producto.

Requisitos. Escribe obtener_producto(con, id_producto), que llame al
procedimiento y retorne un diccionario
    {"id": 1, "nombre": "Chais", "precio": 18.0}
o None si el producto no existe.

Conceptos: callproc, stored_results.
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
    """Crea el procedimiento que usa este ejercicio. No lo modifiques."""
    with closing(con.cursor()) as cursor:
        cursor.execute("DROP PROCEDURE IF EXISTS ej_obtener_producto")
        cursor.execute("""
            CREATE PROCEDURE ej_obtener_producto(IN p_id INT)
            BEGIN
                SELECT ProductID, ProductName, Price FROM Products WHERE ProductID = p_id;
            END
        """)

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
