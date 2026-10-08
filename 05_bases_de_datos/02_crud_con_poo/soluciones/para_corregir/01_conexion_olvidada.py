"""
Solución - Ejercicio para corregir 01 - Conexión olvidada

CORRECCIÓN 1 (AttributeError: 'BaseDeDatos' object has no attribute
'con'): en __init__ la conexión se guardaba en una variable local que
desaparece al terminar el método. Para que los demás métodos la usen, debe
guardarse en self.con.

CORRECCIÓN 2 (el INSERT no quedaba guardado): mysql.connector trabaja con
autocommit desactivado. Los cambios quedan pendientes en la conexión que
los hizo y nadie más los ve hasta llamar a commit(). Al cerrar la conexión
sin commit, se pierden.
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
        self.con = mysql.connector.connect(**config)  # CORRECCIÓN 1

    def ejecutar(self, sql, parametros=()):
        with closing(self.con.cursor()) as cursor:
            cursor.execute(sql, parametros)
            self.con.commit()  # CORRECCIÓN 2
            return cursor.rowcount

    def cerrar(self):
        self.con.close()


# ----------------------------------------------------------------------
# Pruebas
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
