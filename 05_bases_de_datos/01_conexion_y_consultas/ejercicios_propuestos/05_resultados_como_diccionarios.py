"""
Ejercicio propuesto 05 - Resultados como diccionarios
Nivel: avanzado

Por defecto el cursor retorna tuplas, y hay que recordar en qué posición
está cada columna. Con cursor(dictionary=True) cada fila es un diccionario
cuyas claves son los nombres de las columnas.

Requisitos:
1. consultar(con, sql, parametros=()): función genérica que ejecuta un
   SELECT y retorna una LISTA DE DICCIONARIOS. Cierra el cursor siempre,
   incluso si la consulta falla (usa with closing(...)).
2. resumen_cliente(con, customer_id): usa consultar() y retorna un
   diccionario:
       {"cliente": "Alfreds Futterkiste", "pais": "Germany",
        "pedidos": 1, "unidades": 15}
   (pedidos = cantidad de pedidos del cliente; unidades = suma de
   cantidades de todos sus pedidos; 0 si no tiene). Si el cliente no
   existe, retorna None.
   Pista: usa alias en el SQL (AS cliente, AS pedidos, ...) para que las
   claves del diccionario tengan esos nombres. COALESCE(SUM(...), 0)
   evita que la suma salga NULL.

Conceptos: cursor(dictionary=True), alias, COALESCE, funciones
reutilizables.
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

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)

    filas = consultar(con, "SELECT CategoryID, CategoryName FROM Categories WHERE CategoryID = %s", (1,))
    assert isinstance(filas, list) and isinstance(filas[0], dict), "consultar() debe retornar una lista de diccionarios"
    assert set(filas[0]) == {"CategoryID", "CategoryName"}

    try:
        consultar(con, "SELECT columna_que_no_existe FROM Categories")
        raise AssertionError("Una consulta inválida debe lanzar el error de MySQL")
    except mysql.connector.Error:
        pass

    ref = con.cursor(buffered=True)
    ref.execute("""
        SELECT c.CustomerID, c.CustomerName, c.Country, COUNT(DISTINCT o.OrderID),
               COALESCE(SUM(d.Quantity), 0)
        FROM Customers c
        LEFT JOIN Orders o ON o.CustomerID = c.CustomerID
        LEFT JOIN OrderDetails d ON d.OrderID = o.OrderID
        GROUP BY c.CustomerID ORDER BY COUNT(DISTINCT o.OrderID) DESC LIMIT 1
    """)
    id_cliente, nombre, pais, pedidos, unidades = ref.fetchone()
    resumen = resumen_cliente(con, id_cliente)
    assert resumen["cliente"] == nombre and resumen["pais"] == pais
    assert int(resumen["pedidos"]) == pedidos and int(resumen["unidades"]) == int(unidades)

    ref.execute("""
        SELECT c.CustomerID FROM Customers c LEFT JOIN Orders o ON o.CustomerID = c.CustomerID
        WHERE o.OrderID IS NULL LIMIT 1
    """)
    sin_pedidos = ref.fetchone()
    if sin_pedidos:
        resumen = resumen_cliente(con, sin_pedidos[0])
        assert int(resumen["pedidos"]) == 0 and int(resumen["unidades"]) == 0

    assert resumen_cliente(con, -1) is None

    ref.close()
    con.close()
    print("Todas las pruebas pasaron")
