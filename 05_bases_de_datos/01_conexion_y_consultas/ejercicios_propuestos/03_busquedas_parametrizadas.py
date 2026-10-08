"""
Ejercicio propuesto 03 - Búsquedas parametrizadas
Nivel: intermedio

Nunca se arma una consulta pegando textos que escribió el usuario:
    f"... WHERE ProductName LIKE '%{texto}%'"     <- PELIGROSO
Si el texto trae una comilla, la consulta se rompe; y si alguien escribe
SQL a propósito, puede leer o borrar datos (inyección SQL).

Requisitos:
1. buscar_productos(con, texto): nombres de los productos cuyo nombre
   CONTIENE el texto, ordenados alfabéticamente. Los % del LIKE se agregan
   al VALOR del parámetro, no al SQL:
       cursor.execute("... LIKE %s", (f"%{texto}%",))
2. productos_en_rango(con, minimo, maximo): lista de tuplas
   (ProductName, Price) con precio entre minimo y maximo (incluidos),
   ordenadas por precio y luego por nombre.
3. buscar_cliente_exacto(con, nombre): el CustomerID del cliente con ese
   nombre exacto, o None si no existe.

Las pruebas usan nombres con comillas simples, como "Chef Anton's Cajun
Seasoning", para comprobar que la consulta no se rompe.

Conceptos: LIKE, BETWEEN, parámetros, inyección SQL.
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
