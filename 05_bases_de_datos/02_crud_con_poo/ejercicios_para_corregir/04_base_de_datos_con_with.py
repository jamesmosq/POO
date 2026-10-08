"""
Ejercicio para corregir 04 - Base de datos con with
Nivel: intermedio
Errores a encontrar: 3

Qué debería hacer el programa:
    - BaseDeDatos se usa con with: abre la conexión al entrar y la cierra
      al salir. Si ocurre un error dentro del with, el error NO se esconde.
    - actualizar_transportadora(db, id, nombre, telefono) cambia el nombre
      y el teléfono de una transportadora.
    - listar_transportadoras(db) retorna los nombres ordenados por
      ShipperID.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
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
        self.con.close()
        return True

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
    return db.ejecutar(sql, (telefono, nombre, id_transportadora))


def listar_transportadoras(db):
    filas = db.consultar("SELECT ShipperName FROM Shippers ORDER BY ShipperName DESC")
    return [fila[0] for fila in filas]


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
