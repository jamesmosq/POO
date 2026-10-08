"""
Ejercicio propuesto 03 - Entidad y repositorio
Nivel: intermedio

En lugar de diccionarios, el repositorio puede trabajar con objetos de una
clase que representa la fila (una "entidad"). @dataclass genera
automáticamente __init__, __repr__ y __eq__.

Requisitos:
1. @dataclass Categoria con los campos nombre, descripcion="" e id=None.
   En __post_init__ valida que el nombre no esté vacío y que tenga máximo
   25 caracteres (la columna CategoryName es VARCHAR(25)); si no, ValueError.
2. RepositorioCategorias(con):
   - guardar(categoria): si categoria.id es None, la inserta y le asigna el
     id nuevo; si ya tiene id, la actualiza. Retorna la categoría.
   - obtener(id): Categoria o None.
   - buscar(texto): lista de Categoria cuyo nombre contiene el texto,
     ordenadas por nombre.
   - eliminar(categoria): True si la eliminó.

Conceptos: dataclasses, entidades, mapear filas a objetos.
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

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
