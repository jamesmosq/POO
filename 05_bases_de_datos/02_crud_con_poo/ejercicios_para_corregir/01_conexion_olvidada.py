"""
Ejercicio para corregir 01 - Conexión olvidada
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    BaseDeDatos abre la conexión al crearse. ejecutar() corre un INSERT,
    UPDATE o DELETE y lo deja GUARDADO en la base de datos (cualquier otra
    conexión debe poder verlo).

Ojo: uno de los errores no lanza ninguna excepción. El programa "funciona",
pero los datos nunca quedan guardados.

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
        con = mysql.connector.connect(**config)

    def ejecutar(self, sql, parametros=()):
        with closing(self.con.cursor()) as cursor:
            cursor.execute(sql, parametros)
            return cursor.rowcount

    def cerrar(self):
        self.con.close()


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
def contar_desde_otra_conexion():
    otra = mysql.connector.connect(**CONFIG)
    cursor = otra.cursor(buffered=True)
    cursor.execute("SELECT COUNT(*) FROM Shippers WHERE ShipperName = 'PRUEBA_EJ_Guardado'")
    total = cursor.fetchone()[0]
    cursor.close()
    otra.close()
    return total


if __name__ == "__main__":
    db = BaseDeDatos(CONFIG)
    try:
        filas = db.ejecutar("INSERT INTO Shippers (ShipperName, Phone) VALUES (%s, %s)", ("PRUEBA_EJ_Guardado", "555"))
        assert filas == 1
        assert contar_desde_otra_conexion() == 1, "El INSERT no quedó guardado en la base de datos"
    finally:
        if hasattr(db, "con"):
            db.cerrar()
        limpieza = mysql.connector.connect(**CONFIG)
        cursor = limpieza.cursor()
        cursor.execute("DELETE FROM Shippers WHERE ShipperName LIKE 'PRUEBA_EJ_%'")
        limpieza.commit()
        cursor.close()
        limpieza.close()

    print("Todas las pruebas pasaron")
