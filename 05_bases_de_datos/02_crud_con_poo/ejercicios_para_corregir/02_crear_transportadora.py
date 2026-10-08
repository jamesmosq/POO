"""
Ejercicio para corregir 02 - Crear transportadora
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    RepositorioTransportadoras.crear(nombre, telefono) inserta una fila en
    Shippers y retorna el id nuevo. Debe funcionar con cualquier nombre,
    incluso con comillas, como "O'Brien Express".

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


class RepositorioTransportadoras:
    def __init__(self, con):
        self.con = con

    def crear(self, nombre, telefono):
        with closing(self.con.cursor()) as cursor:
            cursor.execute(f"INSERT INTO Shippers (ShipperName, Phone) VALUES ('{nombre}', '{telefono}')")
            self.con.commit()
            return self.con.lastrowid


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
