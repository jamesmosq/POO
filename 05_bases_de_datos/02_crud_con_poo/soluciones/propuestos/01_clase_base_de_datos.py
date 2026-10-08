"""
Solución - Ejercicio propuesto 01 - Clase BaseDeDatos
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


class BaseDeDatos:
    def __init__(self, config):
        self.config = config
        self.con = None
        self.ultimo_id = None

    def conectar(self):
        self.con = mysql.connector.connect(**self.config)

    def cerrar(self):
        if self.con is not None and self.con.is_connected():
            self.con.close()

    def __enter__(self):
        self.conectar()
        return self

    def __exit__(self, tipo, valor, traza):
        self.cerrar()
        # No se retorna True: si hubo un error dentro del with, debe verse.

    def consultar(self, sql, parametros=()):
        with closing(self.con.cursor(dictionary=True, buffered=True)) as cursor:
            cursor.execute(sql, parametros)
            return cursor.fetchall()

    def ejecutar(self, sql, parametros=()):
        with closing(self.con.cursor()) as cursor:
            cursor.execute(sql, parametros)
            self.con.commit()
            self.ultimo_id = cursor.lastrowid
            return cursor.rowcount


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
def limpiar_datos_de_prueba():
    con = mysql.connector.connect(**CONFIG)
    cursor = con.cursor()
    cursor.execute("DELETE FROM Shippers WHERE ShipperName LIKE 'PRUEBA_EJ_%'")
    con.commit()
    cursor.close()
    con.close()


if __name__ == "__main__":
    try:
        with BaseDeDatos(CONFIG) as db:
            assert db.con.is_connected()
            filas = db.ejecutar("INSERT INTO Shippers (ShipperName, Phone) VALUES (%s, %s)", ("PRUEBA_EJ_Uno", "555"))
            assert filas == 1
            nuevo_id = db.ultimo_id
            assert isinstance(nuevo_id, int) and nuevo_id > 0

            encontrados = db.consultar("SELECT ShipperID, ShipperName FROM Shippers WHERE ShipperID = %s", (nuevo_id,))
            assert encontrados == [{"ShipperID": nuevo_id, "ShipperName": "PRUEBA_EJ_Uno"}]

        assert not db.con.is_connected(), "Al salir del with la conexión debe cerrarse"

        otra = mysql.connector.connect(**CONFIG)
        cursor = otra.cursor(buffered=True)
        cursor.execute("SELECT COUNT(*) FROM Shippers WHERE ShipperID = %s", (nuevo_id,))
        assert cursor.fetchone()[0] == 1, "ejecutar() debe hacer commit"
        cursor.close()
        otra.close()

        try:
            with BaseDeDatos(CONFIG) as db:
                db.consultar("SELECT * FROM TablaQueNoExiste")
            raise AssertionError("El error de la consulta no debe quedar escondido")
        except mysql.connector.Error:
            pass
    finally:
        limpiar_datos_de_prueba()

    print("Todas las pruebas pasaron")
