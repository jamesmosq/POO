"""
Ejercicio propuesto 02 - Procedimiento de búsqueda
Nivel: básico

La función preparar() (ya escrita) crea el procedimiento
ej_buscar_productos(p_texto), que retorna DOS resultados:
    1. Los productos cuyo nombre contiene el texto (ProductName, Price),
       ordenados por nombre.
    2. Una sola fila con la cantidad encontrada (total).

Requisitos. Escribe buscar(con, texto), que retorne una tupla
    (lista_de_nombres, total)
leyendo los dos resultados en orden. Pista: list(cursor.stored_results())
te da los resultados en una lista.

Conceptos: procedimientos con varios resultados, parámetros de entrada.
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
        cursor.execute("DROP PROCEDURE IF EXISTS ej_buscar_productos")
        cursor.execute("""
            CREATE PROCEDURE ej_buscar_productos(IN p_texto VARCHAR(50))
            BEGIN
                SELECT ProductName, Price FROM Products
                WHERE ProductName LIKE CONCAT('%', p_texto, '%') ORDER BY ProductName;
                SELECT COUNT(*) AS total FROM Products
                WHERE ProductName LIKE CONCAT('%', p_texto, '%');
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
    for texto in ("Chef", "Queso", "zzz"):
        ref.execute("SELECT ProductName FROM Products WHERE ProductName LIKE %s ORDER BY ProductName", (f"%{texto}%",))
        esperado = [fila[0] for fila in ref.fetchall()]
        nombres, total = buscar(con, texto)
        assert nombres == esperado, (texto, nombres)
        assert total == len(esperado)
    ref.close()
    con.close()
    print("Todas las pruebas pasaron")
