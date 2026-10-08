"""
Solución - Ejercicio para corregir 03 - Obtener y eliminar

CORRECCIÓN 1 (retornaba una tupla): para obtener la fila como diccionario
el cursor se crea con dictionary=True. Los alias del SQL (AS id, AS nombre,
...) se convierten en las claves.

CORRECCIÓN 2 (eliminar siempre retornaba True): un DELETE que no encuentra
filas no es un error, simplemente afecta 0 filas. cursor.rowcount dice
cuántas filas se eliminaron.
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


class RepositorioTransportadoras:
    def __init__(self, con):
        self.con = con

    def obtener(self, id_transportadora):
        sql = "SELECT ShipperID AS id, ShipperName AS nombre, Phone AS telefono FROM Shippers WHERE ShipperID = %s"
        with closing(self.con.cursor(dictionary=True, buffered=True)) as cursor:  # CORRECCIÓN 1
            cursor.execute(sql, (id_transportadora,))
            return cursor.fetchone()

    def eliminar(self, id_transportadora):
        with closing(self.con.cursor()) as cursor:
            cursor.execute("DELETE FROM Shippers WHERE ShipperID = %s", (id_transportadora,))
            self.con.commit()
            return cursor.rowcount == 1  # CORRECCIÓN 2


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    try:
        cursor = con.cursor()
        cursor.execute("INSERT INTO Shippers (ShipperName, Phone) VALUES ('PRUEBA_EJ_Obtener', '555')")
        con.commit()
        nuevo = cursor.lastrowid
        cursor.close()

        repo = RepositorioTransportadoras(con)
        assert repo.obtener(nuevo) == {"id": nuevo, "nombre": "PRUEBA_EJ_Obtener", "telefono": "555"}, repo.obtener(nuevo)
        assert repo.obtener(-1) is None
        assert repo.eliminar(nuevo) is True
        assert repo.eliminar(nuevo) is False, "Eliminar un id que ya no existe debe retornar False"
    finally:
        cursor = con.cursor()
        cursor.execute("DELETE FROM Shippers WHERE ShipperName LIKE 'PRUEBA_EJ_%'")
        con.commit()
        cursor.close()
        con.close()

    print("Todas las pruebas pasaron")
