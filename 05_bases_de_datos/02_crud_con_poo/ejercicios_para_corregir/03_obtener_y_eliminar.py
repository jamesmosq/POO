"""
Ejercicio para corregir 03 - Obtener y eliminar
Nivel: intermedio
Errores a encontrar: 2

Qué debería hacer el programa:
    - obtener(id) retorna un diccionario {"id", "nombre", "telefono"} o
      None si no existe.
    - eliminar(id) retorna True si eliminó una fila y False si el id no
      existía.

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
    "password": os.getenv("DB_PASSWORD", "base1234"),
    "database": os.getenv("DB_NAME", "northwind"),
}


class RepositorioTransportadoras:
    def __init__(self, con):
        self.con = con

    def obtener(self, id_transportadora):
        sql = "SELECT ShipperID AS id, ShipperName AS nombre, Phone AS telefono FROM Shippers WHERE ShipperID = %s"
        with closing(self.con.cursor(buffered=True)) as cursor:
            cursor.execute(sql, (id_transportadora,))
            return cursor.fetchone()

    def eliminar(self, id_transportadora):
        with closing(self.con.cursor()) as cursor:
            cursor.execute("DELETE FROM Shippers WHERE ShipperID = %s", (id_transportadora,))
            self.con.commit()
            return True


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
