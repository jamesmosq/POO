"""
Ejercicio propuesto 03 - Crear un procedimiento
Nivel: intermedio

Ahora escribes tú el procedimiento.

IMPORTANTE: DELIMITER es un comando del cliente de MySQL (la consola o
Workbench), no es SQL. Desde Python NO se usa: cada sentencia se envía por
separado con execute(), y el CREATE PROCEDURE completo (con su BEGIN y su
END) es una sola sentencia.

Requisitos:
1. Completa la constante SQL_CREAR con el CREATE PROCEDURE de
   ej_productos_por_categoria(IN p_categoria INT), que retorna ProductName
   y Price de los productos de esa categoría, del más caro al más barato.
2. crear_procedimiento(con): ejecuta primero
       DROP PROCEDURE IF EXISTS ej_productos_por_categoria
   y después SQL_CREAR. Así se puede ejecutar varias veces sin error.
3. productos_por_categoria(con, categoria): llama al procedimiento y
   retorna la lista de tuplas (nombre, precio) con el precio como float.

Conceptos: CREATE PROCEDURE, parámetros IN, DROP IF EXISTS, DELIMITER.
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

SQL_CREAR = """
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    crear_procedimiento(con)
    crear_procedimiento(con)  # la segunda vez no debe fallar

    ref = con.cursor(buffered=True)
    ref.execute("SELECT ProductName, Price FROM Products WHERE CategoryID = 1 ORDER BY Price DESC")
    esperado = [(n, float(p)) for n, p in ref.fetchall()]
    obtenido = productos_por_categoria(con, 1)
    assert [p for _, p in obtenido] == [p for _, p in esperado], obtenido
    assert sorted(obtenido) == sorted(esperado)
    assert productos_por_categoria(con, -1) == []
    assert "DELIMITER" not in SQL_CREAR.upper(), "DELIMITER no es SQL: no lo uses desde Python"

    ref.close()
    con.close()
    print("Todas las pruebas pasaron")
