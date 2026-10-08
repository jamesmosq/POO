"""
Solución - Ejercicio para corregir 04 - Base de datos con with

CORRECCIÓN 1 (los errores desaparecían): si __exit__ retorna True, Python
entiende que el error ya se manejó y lo descarta. Un __exit__ que solo
libera recursos no debe retornar nada.

CORRECCIÓN 2 (nombre y teléfono intercambiados): los valores de la tupla se
asignan a los %s en el MISMO orden en que aparecen en el SQL.

CORRECCIÓN 3 (orden incorrecto): el enunciado pide ordenar por ShipperID.
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

    def __enter__(self):
        self.con = mysql.connector.connect(**self.config)
        return self

    def __exit__(self, tipo, valor, traza):
        self.con.close()  # CORRECCIÓN 1: sin "return True"

    def ejecutar(self, sql, parametros=()):
        with closing(self.con.cursor()) as cursor:
            cursor.execute(sql, parametros)
            self.con.commit()
            return cursor.rowcount

    def consultar(self, sql, parametros=()):
        with closing(self.con.cursor(buffered=True)) as cursor:
            cursor.execute(sql, parametros)
            return cursor.fetchall()


def actualizar_transportadora(db, id_transportadora, nombre, telefono):
    sql = "UPDATE Shippers SET ShipperName = %s, Phone = %s WHERE ShipperID = %s"
    return db.ejecutar(sql, (nombre, telefono, id_transportadora))  # CORRECCIÓN 2


def listar_transportadoras(db):
    filas = db.consultar("SELECT ShipperName FROM Shippers ORDER BY ShipperID")  # CORRECCIÓN 3
    return [fila[0] for fila in filas]


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    error_visible = False
    try:
        with BaseDeDatos(CONFIG) as db:
            db.consultar("SELECT * FROM TablaQueNoExiste")
    except mysql.connector.Error:
        error_visible = True
    assert error_visible, "__exit__ está escondiendo los errores que ocurren dentro del with"

    try:
        with BaseDeDatos(CONFIG) as db:
            db.ejecutar("INSERT INTO Shippers (ShipperName, Phone) VALUES ('PRUEBA_EJ_Antes', '1')")
            nuevo = db.consultar("SELECT MAX(ShipperID) FROM Shippers")[0][0]
            actualizar_transportadora(db, nuevo, "PRUEBA_EJ_Despues", "999")
            fila = db.consultar("SELECT ShipperName, Phone FROM Shippers WHERE ShipperID = %s", (nuevo,))[0]
            assert fila == ("PRUEBA_EJ_Despues", "999"), fila

            esperado = [f[0] for f in db.consultar("SELECT ShipperName FROM Shippers ORDER BY ShipperID")]
            assert listar_transportadoras(db) == esperado
    finally:
        with BaseDeDatos(CONFIG) as db:
            db.ejecutar("DELETE FROM Shippers WHERE ShipperName LIKE 'PRUEBA_EJ_%'")

    print("Todas las pruebas pasaron")
