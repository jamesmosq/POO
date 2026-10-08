"""
Ejercicio propuesto 02 - Repositorio de transportadoras
Nivel: intermedio

Un "repositorio" es una clase que concentra todas las operaciones de una
tabla. El resto del programa le pide datos al repositorio y nunca escribe
SQL.

Requisitos. Crea la clase RepositorioTransportadoras(con) para la tabla
Shippers (ShipperID, ShipperName, Phone):
1. crear(nombre, telefono): inserta y retorna el id nuevo. Lanza
   ValueError si el nombre está vacío.
2. obtener(id): diccionario {"id", "nombre", "telefono"} o None.
3. listar(): lista de diccionarios como el anterior, ordenada por id.
4. actualizar(id, nombre, telefono): True si actualizó una fila, False si
   el id no existe.
5. eliminar(id): True si eliminó, False si el id no existe.
Cada operación que modifica datos hace commit.

Pista: usa alias en el SQL para que las claves salgan en español:
    SELECT ShipperID AS id, ShipperName AS nombre, Phone AS telefono ...

Conceptos: patrón repositorio, CRUD completo, rowcount.
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

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
