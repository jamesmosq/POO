"""
Solución - Ejercicio propuesto 04 - Repositorio de productos
"""
import os
import re

from bson import ObjectId
from pymongo import ASCENDING, MongoClient
from pymongo.errors import DuplicateKeyError

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "curso_poo")


class RepositorioProductos:
    CAMPOS_EDITABLES = {"nombre", "precio", "stock"}

    def __init__(self, db):
        self.coleccion = db["ej_productos"]
        self.coleccion.create_index("nombre", unique=True)

    @staticmethod
    def _a_diccionario(documento):
        if documento is None:
            return None
        documento = dict(documento)
        documento["id"] = str(documento.pop("_id"))
        return documento

    @staticmethod
    def _validar(nombre=None, precio=None, stock=None):
        datos = {}
        if nombre is not None:
            nombre = nombre.strip()
            if not nombre:
                raise ValueError("El nombre es obligatorio")
            datos["nombre"] = nombre
        if precio is not None:
            if precio < 0:
                raise ValueError("El precio no puede ser negativo")
            datos["precio"] = precio
        if stock is not None:
            if stock < 0:
                raise ValueError("El stock no puede ser negativo")
            datos["stock"] = stock
        return datos

    def crear(self, nombre, precio, stock=0):
        documento = self._validar(nombre, precio, stock)
        try:
            return str(self.coleccion.insert_one(documento).inserted_id)
        except DuplicateKeyError:
            raise ValueError(f"Ya existe un producto llamado {documento['nombre']!r}") from None

    def obtener(self, id_texto):
        if not ObjectId.is_valid(id_texto):
            return None
        return self._a_diccionario(self.coleccion.find_one({"_id": ObjectId(id_texto)}))

    def listar(self, texto=""):
        filtro = {}
        if texto.strip():
            filtro["nombre"] = {"$regex": re.escape(texto.strip()), "$options": "i"}
        return [self._a_diccionario(d) for d in self.coleccion.find(filtro).sort("nombre", ASCENDING)]

    def actualizar(self, id_texto, **cambios):
        no_permitidos = set(cambios) - self.CAMPOS_EDITABLES
        if no_permitidos:
            raise ValueError(f"Campos no permitidos: {', '.join(sorted(no_permitidos))}")
        datos = self._validar(**cambios)
        if not ObjectId.is_valid(id_texto):
            return False
        try:
            resultado = self.coleccion.update_one({"_id": ObjectId(id_texto)}, {"$set": datos})
        except DuplicateKeyError:
            raise ValueError(f"Ya existe un producto llamado {datos['nombre']!r}") from None
        return resultado.matched_count == 1

    def eliminar(self, id_texto):
        if not ObjectId.is_valid(id_texto):
            return False
        return self.coleccion.delete_one({"_id": ObjectId(id_texto)}).deleted_count == 1


# ----------------------------------------------------------------------
# Pruebas
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
