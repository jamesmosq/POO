"""
Solución - Ejercicio propuesto 03 - Entidad y repositorio
"""

import os
from contextlib import closing
from dataclasses import dataclass

import mysql.connector

CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "base1234"),
    "database": os.getenv("DB_NAME", "northwind"),
}


@dataclass
class Categoria:
    nombre: str
    descripcion: str = ""
    id: int = None

    def __post_init__(self):
        if not self.nombre or len(self.nombre) > 25:
            raise ValueError("El nombre es obligatorio y tiene máximo 25 caracteres")


class RepositorioCategorias:
    def __init__(self, con):
        self.con = con

    def _a_categoria(self, fila):
        return Categoria(nombre=fila["CategoryName"], descripcion=fila["Description"] or "", id=fila["CategoryID"])

    def guardar(self, categoria):
        with closing(self.con.cursor()) as cursor:
            if categoria.id is None:
                cursor.execute(
                    "INSERT INTO Categories (CategoryName, Description) VALUES (%s, %s)",
                    (categoria.nombre, categoria.descripcion),
                )
                categoria.id = cursor.lastrowid
            else:
                cursor.execute(
                    "UPDATE Categories SET CategoryName = %s, Description = %s WHERE CategoryID = %s",
                    (categoria.nombre, categoria.descripcion, categoria.id),
                )
            self.con.commit()
        return categoria

    def obtener(self, id_categoria):
        with closing(self.con.cursor(dictionary=True, buffered=True)) as cursor:
            cursor.execute("SELECT * FROM Categories WHERE CategoryID = %s", (id_categoria,))
            fila = cursor.fetchone()
        return self._a_categoria(fila) if fila else None

    def buscar(self, texto):
        with closing(self.con.cursor(dictionary=True, buffered=True)) as cursor:
            cursor.execute(
                "SELECT * FROM Categories WHERE CategoryName LIKE %s ORDER BY CategoryName",
                (f"%{texto}%",),
            )
            return [self._a_categoria(fila) for fila in cursor.fetchall()]

    def eliminar(self, categoria):
        with closing(self.con.cursor()) as cursor:
            cursor.execute("DELETE FROM Categories WHERE CategoryID = %s", (categoria.id,))
            self.con.commit()
            return cursor.rowcount == 1


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    for invalido in ("", "X" * 26):
        try:
            Categoria(invalido)
            raise AssertionError(f"Categoria({invalido!r}) debe lanzar ValueError")
        except ValueError:
            pass

    con = mysql.connector.connect(**CONFIG)
    try:
        repo = RepositorioCategorias(con)
        bebidas = repo.guardar(Categoria("PRUEBA_EJ_Bebidas", "Jugos y aguas"))
        assert isinstance(bebidas.id, int)
        assert repo.obtener(bebidas.id) == bebidas

        bebidas.descripcion = "Solo jugos"
        repo.guardar(bebidas)
        assert repo.obtener(bebidas.id).descripcion == "Solo jugos"

        repo.guardar(Categoria("PRUEBA_EJ_Aseo"))
        nombres = [c.nombre for c in repo.buscar("PRUEBA_EJ_")]
        assert nombres == ["PRUEBA_EJ_Aseo", "PRUEBA_EJ_Bebidas"]

        assert repo.eliminar(bebidas) is True
        assert repo.obtener(bebidas.id) is None
    finally:
        cursor = con.cursor()
        cursor.execute("DELETE FROM Categories WHERE CategoryName LIKE 'PRUEBA_EJ_%'")
        con.commit()
        cursor.close()
        con.close()

    print("Todas las pruebas pasaron")
