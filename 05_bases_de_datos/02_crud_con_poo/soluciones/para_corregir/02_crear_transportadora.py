"""
Solución - Ejercicio para corregir 02 - Crear transportadora

CORRECCIÓN 1 (error de sintaxis SQL con "O'Brien"): al pegar el nombre
dentro del SQL, su comilla cierra el texto antes de tiempo y la consulta
queda mal escrita. Eso mismo es la puerta de entrada de la inyección SQL.
Los valores se pasan como parámetros %s.

CORRECCIÓN 2 (AttributeError: ... has no attribute 'lastrowid'): el id
generado lo tiene el CURSOR que ejecutó el INSERT, no la conexión.
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


class RepositorioTransportadoras:
    def __init__(self, con):
        self.con = con

    def crear(self, nombre, telefono):
        with closing(self.con.cursor()) as cursor:
            cursor.execute("INSERT INTO Shippers (ShipperName, Phone) VALUES (%s, %s)", (nombre, telefono))  # CORRECCIÓN 1
            self.con.commit()
            return cursor.lastrowid  # CORRECCIÓN 2


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    try:
        repo = RepositorioTransportadoras(con)
        nuevo = repo.crear("PRUEBA_EJ_O'Brien Express", "300")
        assert isinstance(nuevo, int) and nuevo > 0, f"crear() retornó {nuevo!r}"
        cursor = con.cursor(buffered=True)
        cursor.execute("SELECT ShipperName FROM Shippers WHERE ShipperID = %s", (nuevo,))
        assert cursor.fetchone()[0] == "PRUEBA_EJ_O'Brien Express"
        cursor.close()
    finally:
        cursor = con.cursor()
        cursor.execute("DELETE FROM Shippers WHERE ShipperName LIKE 'PRUEBA_EJ_%'")
        con.commit()
        cursor.close()
        con.close()

    print("Todas las pruebas pasaron")
