"""
Solución - Ejercicio propuesto 02 - Repositorio de transportadoras
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
    COLUMNAS = "ShipperID AS id, ShipperName AS nombre, Phone AS telefono"

    def __init__(self, con):
        self.con = con

    def _consultar(self, sql, parametros=()):
        with closing(self.con.cursor(dictionary=True, buffered=True)) as cursor:
            cursor.execute(sql, parametros)
            return cursor.fetchall()

    def _ejecutar(self, sql, parametros):
        """Ejecuta un cambio y retorna (filas_afectadas, id_generado)."""
        with closing(self.con.cursor()) as cursor:
            cursor.execute(sql, parametros)
            self.con.commit()
            # Se leen antes de que closing() cierre el cursor.
            return cursor.rowcount, cursor.lastrowid

    def crear(self, nombre, telefono):
        if not nombre.strip():
            raise ValueError("El nombre es obligatorio")
        _, nuevo_id = self._ejecutar("INSERT INTO Shippers (ShipperName, Phone) VALUES (%s, %s)", (nombre.strip(), telefono))
        return nuevo_id

    def obtener(self, id_transportadora):
        filas = self._consultar(f"SELECT {self.COLUMNAS} FROM Shippers WHERE ShipperID = %s", (id_transportadora,))
        return filas[0] if filas else None

    def listar(self):
        return self._consultar(f"SELECT {self.COLUMNAS} FROM Shippers ORDER BY ShipperID")

    def actualizar(self, id_transportadora, nombre, telefono):
        filas, _ = self._ejecutar(
            "UPDATE Shippers SET ShipperName = %s, Phone = %s WHERE ShipperID = %s",
            (nombre, telefono, id_transportadora),
        )
        return filas == 1

    def eliminar(self, id_transportadora):
        filas, _ = self._ejecutar("DELETE FROM Shippers WHERE ShipperID = %s", (id_transportadora,))
        return filas == 1


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    try:
        repo = RepositorioTransportadoras(con)
        nuevo = repo.crear("PRUEBA_EJ_Rápido", "300 111 2233")
        assert repo.obtener(nuevo) == {"id": nuevo, "nombre": "PRUEBA_EJ_Rápido", "telefono": "300 111 2233"}
        assert repo.obtener(-1) is None

        otro = repo.crear("PRUEBA_EJ_O'Brien", "310")
        ids = [t["id"] for t in repo.listar()]
        assert ids == sorted(ids) and nuevo in ids and otro in ids

        assert repo.actualizar(nuevo, "PRUEBA_EJ_Veloz", "300 999 8877") is True
        assert repo.obtener(nuevo)["nombre"] == "PRUEBA_EJ_Veloz"
        assert repo.actualizar(-1, "x", "y") is False

        assert repo.eliminar(otro) is True
        assert repo.eliminar(otro) is False
        assert repo.obtener(otro) is None

        try:
            repo.crear("   ", "123")
            raise AssertionError("Un nombre vacío debe lanzar ValueError")
        except ValueError:
            pass
    finally:
        cursor = con.cursor()
        cursor.execute("DELETE FROM Shippers WHERE ShipperName LIKE 'PRUEBA_EJ_%'")
        con.commit()
        cursor.close()
        con.close()

    print("Todas las pruebas pasaron")
