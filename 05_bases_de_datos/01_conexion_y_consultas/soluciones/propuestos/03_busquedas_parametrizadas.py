"""
Solución - Ejercicio propuesto 03 - Búsquedas parametrizadas
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


def buscar_productos(con, texto):
    with closing(con.cursor(buffered=True)) as cursor:
        # Los % son parte del VALOR; el SQL solo tiene el marcador %s.
        cursor.execute(
            "SELECT ProductName FROM Products WHERE ProductName LIKE %s ORDER BY ProductName",
            (f"%{texto}%",),
        )
        return [fila[0] for fila in cursor.fetchall()]


def productos_en_rango(con, minimo, maximo):
    with closing(con.cursor(buffered=True)) as cursor:
        cursor.execute(
            "SELECT ProductName, Price FROM Products WHERE Price BETWEEN %s AND %s "
            "ORDER BY Price, ProductName",
            (minimo, maximo),
        )
        return cursor.fetchall()


def buscar_cliente_exacto(con, nombre):
    with closing(con.cursor(buffered=True)) as cursor:
        cursor.execute("SELECT CustomerID FROM Customers WHERE CustomerName = %s", (nombre,))
        fila = cursor.fetchone()
        return fila[0] if fila else None


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    ref = con.cursor(buffered=True)

    ref.execute("SELECT ProductName FROM Products WHERE ProductName LIKE '%Chef%' ORDER BY ProductName")
    assert buscar_productos(con, "Chef") == [fila[0] for fila in ref.fetchall()]
    ref.execute("SELECT ProductName FROM Products WHERE ProductName LIKE %s ORDER BY ProductName", ("%Anton's%",))
    assert buscar_productos(con, "Anton's") == [fila[0] for fila in ref.fetchall()], (
        "Un texto con comilla simple no debe romper la consulta"
    )
    assert buscar_productos(con, "' OR '1'='1") == [], "La inyección SQL no debe traer todos los productos"

    ref.execute("SELECT ProductName, Price FROM Products WHERE Price BETWEEN 10 AND 20 ORDER BY Price, ProductName")
    esperado = [(n, float(p)) for n, p in ref.fetchall()]
    assert [(n, float(p)) for n, p in productos_en_rango(con, 10, 20)] == esperado

    ref.execute("SELECT CustomerID, CustomerName FROM Customers ORDER BY CustomerID LIMIT 1")
    id_cliente, nombre = ref.fetchone()
    assert buscar_cliente_exacto(con, nombre) == id_cliente
    assert buscar_cliente_exacto(con, "No existe S.A.") is None

    ref.close()
    con.close()
    print("Todas las pruebas pasaron")
