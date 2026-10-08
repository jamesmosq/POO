"""
Ejercicio para corregir 02 - Clientes por país
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    clientes_de(con, pais) retorna la lista de nombres de los clientes de
    ese país, en orden alfabético (de la A a la Z).

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


def clientes_de(con, pais):
    with closing(con.cursor()) as cursor:
        cursor.execute(f"SELECT CustomerName FROM Customers WHERE Country = {pais} ORDER BY CustomerName DESC")
        return [fila[0] for fila in cursor.fetchall()]


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    ref = con.cursor(buffered=True)
    ref.execute("SELECT CustomerName FROM Customers WHERE Country = %s ORDER BY CustomerName", ("Mexico",))
    esperado = [fila[0] for fila in ref.fetchall()]
    obtenido = clientes_de(con, "Mexico")
    assert obtenido == esperado, obtenido
    ref.close()
    con.close()
    print("Todas las pruebas pasaron")
