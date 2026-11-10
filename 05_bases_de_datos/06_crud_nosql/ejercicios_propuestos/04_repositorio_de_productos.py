"""
Ejercicio propuesto 04 - Repositorio de productos
Nivel: avanzado

Organiza el CRUD en una clase, como en el ejemplo 07. El resto del
programa usará ids de texto y diccionarios normales: el ObjectId no debe
salir del repositorio.

Requisitos. Crea la clase RepositorioProductos:
1. __init__(self, db): guarda en self.coleccion la colección
   db["ej_productos"] y crea un índice ÚNICO sobre "nombre":
       self.coleccion.create_index("nombre", unique=True)
2. crear(nombre, precio, stock=0) -> id como texto.
   ValueError si el nombre (sin espacios a los lados) está vacío, si el
   precio o el stock son negativos, o si ya existe un producto con ese
   nombre (captura pymongo.errors.DuplicateKeyError y lanza ValueError).
3. obtener(id_texto) -> diccionario o None (también None si el id no es
   válido). El diccionario NO tiene "_id": tiene "id" con el id en texto.
4. listar(texto="") -> lista de diccionarios (con "id", sin "_id")
   ordenados por nombre. Si texto no está vacío, solo los que lo contienen
   en el nombre, sin importar mayúsculas (escapa el texto).
5. actualizar(id_texto, **cambios) -> bool
   Solo acepta los campos "nombre", "precio" y "stock"; con cualquier
   otro lanza ValueError. Un nombre repetido también da ValueError.
   Devuelve True si el producto existía.
6. eliminar(id_texto) -> bool.

Conceptos: repositorio, conversión ObjectId <-> texto, índice único,
DuplicateKeyError, **kwargs.
"""
import os
import re

from bson import ObjectId
from pymongo import ASCENDING, MongoClient
from pymongo.errors import DuplicateKeyError

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "curso_poo")

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
def debe_fallar(funcion, *argumentos, **nombrados):
    try:
        funcion(*argumentos, **nombrados)
    except ValueError:
        return
    raise AssertionError(f"{funcion.__name__}{argumentos} debía lanzar ValueError")


def de_prueba(nombres):
    """Deja solo los nombres creados por las pruebas (la colección puede tener otros)."""
    return [n for n in nombres if n.startswith("PRUEBA_EJ_")]

if __name__ == "__main__":
    cliente = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
    coleccion = cliente[MONGO_DB]["ej_productos"]
    coleccion.delete_many({"nombre": {"$regex": "^PRUEBA_EJ_"}})
    try:
        repo = RepositorioProductos(cliente[MONGO_DB])
        assert repo.coleccion.name == "ej_productos"
        indices_unicos = [i for i in repo.coleccion.index_information().values()
                          if i.get("unique") and i["key"][0][0] == "nombre"]
        assert indices_unicos, "Falta el índice único sobre 'nombre'"

        id_teclado = repo.crear("  PRUEBA_EJ_Teclado ", 180000, 4)
        assert isinstance(id_teclado, str)
        id_monitor = repo.crear("PRUEBA_EJ_Monitor", 620000)

        debe_fallar(repo.crear, "PRUEBA_EJ_Teclado", 1)
        debe_fallar(repo.crear, "   ", 1)
        debe_fallar(repo.crear, "PRUEBA_EJ_Malo", -1)
        debe_fallar(repo.crear, "PRUEBA_EJ_Malo", 1, -1)

        teclado = repo.obtener(id_teclado)
        assert teclado is not None and "_id" not in teclado, "obtener no debe devolver '_id'"
        assert teclado["id"] == id_teclado and teclado["nombre"] == "PRUEBA_EJ_Teclado"
        assert teclado["stock"] == 4 and repo.obtener(id_monitor)["stock"] == 0
        assert repo.obtener("xyz") is None and repo.obtener(str(ObjectId())) is None

        todos = repo.listar()
        assert all("_id" not in p and "id" in p for p in todos)
        assert de_prueba([p["nombre"] for p in todos]) == ["PRUEBA_EJ_Monitor", "PRUEBA_EJ_Teclado"]
        assert [p["nombre"] for p in repo.listar("prueba_ej_tec")] == ["PRUEBA_EJ_Teclado"]
        assert repo.listar("PRUEBA_EJ_.*") == [], "Escapa el texto de la búsqueda"

        assert repo.actualizar(id_teclado, precio=150000, stock=9) is True
        teclado = repo.obtener(id_teclado)
        assert teclado["precio"] == 150000 and teclado["stock"] == 9
        assert teclado["nombre"] == "PRUEBA_EJ_Teclado", "actualizar solo cambia lo que recibe"
        debe_fallar(repo.actualizar, id_teclado, color="negro")
        debe_fallar(repo.actualizar, id_teclado, nombre="PRUEBA_EJ_Monitor")
        debe_fallar(repo.actualizar, id_teclado, precio=-3)
        assert repo.actualizar(str(ObjectId()), precio=1) is False

        assert repo.eliminar(id_monitor) is True
        assert repo.eliminar(id_monitor) is False
        assert repo.obtener(id_monitor) is None
    finally:
        coleccion.delete_many({"nombre": {"$regex": "^PRUEBA_EJ_"}})
        cliente.close()
    print("Todas las pruebas pasaron")
