"""
Ejercicio propuesto 02 - Consultas simples
Nivel: básico

Requisitos. Todas las funciones reciben una conexión abierta (con):
1. productos_mas_caros(con, n): lista de tuplas (ProductName, Price) con
   los n productos más caros, del más caro al más barato. n se pasa como
   parámetro de la consulta (LIMIT %s).
2. clientes_de(con, pais): lista con los nombres (CustomerName) de los
   clientes de ese país, en orden alfabético. El país va como parámetro
   (%s): nunca lo pegues dentro del texto SQL.
3. paises_con_clientes(con): lista de países distintos de la tabla
   Customers, ordenada alfabéticamente (SELECT DISTINCT).

Recuerda: los parámetros se pasan como TUPLA, aunque sea uno solo:
    cursor.execute(sql, (pais,))

Conceptos: SELECT, WHERE, ORDER BY, LIMIT, DISTINCT, parámetros.
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

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
