"""
Ejercicio para corregir 02 - Resultados de búsqueda
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    buscar(con, texto) llama a ej_buscar_nombres(p_texto) y retorna la
    lista de nombres de productos que contienen el texto.

        buscar(con, "Chef") -> ["Chef Anton's Cajun Seasoning",
                                "Chef Anton's Gumbo Mix"]

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
        cursor.execute("DROP PROCEDURE IF EXISTS ej_buscar_nombres")
        cursor.execute("""
            CREATE PROCEDURE ej_buscar_nombres(IN p_texto VARCHAR(50))
            BEGIN
                SELECT ProductName FROM Products
                WHERE ProductName LIKE CONCAT('%', p_texto, '%') ORDER BY ProductName;
            END
        """)


def buscar(con, texto):
    with closing(con.cursor()) as cursor:
        cursor.callproc("ej_buscar_nombres", texto)
        for resultado in cursor.stored_results():
            return list(resultado)


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    preparar(con)
    ref = con.cursor(buffered=True)
    ref.execute("SELECT ProductName FROM Products WHERE ProductName LIKE '%Chef%' ORDER BY ProductName")
    esperado = [fila[0] for fila in ref.fetchall()]
    ref.close()
    assert buscar(con, "Chef") == esperado, buscar(con, "Chef")
    con.close()
    print("Todas las pruebas pasaron")
