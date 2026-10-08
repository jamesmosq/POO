"""
Solución - Ejercicio propuesto 02 - Consultas simples
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


def productos_mas_caros(con, n):
    with closing(con.cursor(buffered=True)) as cursor:
        cursor.execute(
            "SELECT ProductName, Price FROM Products ORDER BY Price DESC, ProductID LIMIT %s",
            (n,),
        )
        return cursor.fetchall()


def clientes_de(con, pais):
    with closing(con.cursor(buffered=True)) as cursor:
        cursor.execute(
            "SELECT CustomerName FROM Customers WHERE Country = %s ORDER BY CustomerName",
            (pais,),
        )
        return [fila[0] for fila in cursor.fetchall()]


def paises_con_clientes(con):
    with closing(con.cursor(buffered=True)) as cursor:
        cursor.execute("SELECT DISTINCT Country FROM Customers ORDER BY Country")
        return [fila[0] for fila in cursor.fetchall()]


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    ref = con.cursor(buffered=True)

    ref.execute("SELECT ProductName, Price FROM Products ORDER BY Price DESC, ProductID LIMIT 3")
    esperado = [(nombre, float(precio)) for nombre, precio in ref.fetchall()]
    obtenido = [(nombre, float(precio)) for nombre, precio in productos_mas_caros(con, 3)]
    assert [p for _, p in obtenido] == [p for _, p in esperado], obtenido

    ref.execute("SELECT CustomerName FROM Customers WHERE Country = 'Germany' ORDER BY CustomerName")
    assert clientes_de(con, "Germany") == [fila[0] for fila in ref.fetchall()]
    assert clientes_de(con, "Atlántida") == []

    ref.execute("SELECT DISTINCT Country FROM Customers ORDER BY Country")
    assert paises_con_clientes(con) == [fila[0] for fila in ref.fetchall()]

    ref.close()
    con.close()
    print("Todas las pruebas pasaron")
