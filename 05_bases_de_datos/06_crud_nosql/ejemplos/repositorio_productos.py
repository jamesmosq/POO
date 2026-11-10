"""
Módulo con las clases del CRUD de productos en MongoDB.

Lo usan el ejemplo 07 (para explicarlas) y el ejemplo 08 (la interfaz
con Tkinter). Separar el acceso a datos en su propio módulo permite que
la interfaz no sepa nada de MongoDB: solo llama métodos del repositorio.
"""
import os
import re

from bson import ObjectId
from pymongo import ASCENDING, MongoClient
from pymongo.errors import DuplicateKeyError

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "curso_poo")


class ConexionMongo:
    """Abre la conexión al entrar al with y la cierra al salir."""

    def __init__(self, uri=MONGO_URI, nombre_bd=MONGO_DB):
        self.uri = uri
        self.nombre_bd = nombre_bd
        self.cliente = None

    def __enter__(self):
        self.cliente = MongoClient(self.uri, serverSelectionTimeoutMS=3000)
        self.cliente.admin.command("ping")   # falla aquí si no hay servidor
        return self.cliente[self.nombre_bd]

    def __exit__(self, tipo, valor, traza):
        self.cliente.close()
        return False   # no ocultar las excepciones


class RepositorioProductos:
    CAMPOS = ("nombre", "categoria", "precio", "stock")

    def __init__(self, db, nombre_coleccion="productos"):
        self.coleccion = db[nombre_coleccion]
        # create_index no falla si el índice ya existe, así que se puede
        # llamar siempre. unique=True: dos documentos no pueden tener el
        # mismo nombre. (Si la colección YA tiene nombres repetidos, crear
        # el índice falla: hay que limpiarlos primero.)
        self.coleccion.create_index([("nombre", ASCENDING)], unique=True)

    # ---- Conversión entre la base de datos y el resto del programa ----
    @staticmethod
    def _a_diccionario(documento):
        """Cambia el _id (ObjectId) por "id" (texto)."""
        if documento is None:
            return None
        documento = dict(documento)
        documento["id"] = str(documento.pop("_id"))
        return documento

    @staticmethod
    def _id(id_texto):
        """Convierte el texto a ObjectId. Lanza ValueError si no es válido."""
        if not ObjectId.is_valid(id_texto):
            raise ValueError(f"Id no válido: {id_texto!r}")
        return ObjectId(id_texto)

    @classmethod
    def _validar(cls, datos):
        nombre = str(datos.get("nombre", "")).strip()
        if not nombre:
            raise ValueError("El nombre es obligatorio")
        precio = float(datos.get("precio", 0))
        stock = int(datos.get("stock", 0))
        if precio < 0 or stock < 0:
            raise ValueError("El precio y el stock no pueden ser negativos")
        return {"nombre": nombre, "categoria": str(datos.get("categoria", "")).strip(),
                "precio": precio, "stock": stock}

    # ---- CRUD ---------------------------------------------------------
    def crear(self, datos):
        documento = self._validar(datos)
        try:
            resultado = self.coleccion.insert_one(documento)
        except DuplicateKeyError:
            raise ValueError(f"Ya existe un producto llamado {documento['nombre']!r}") from None
        return str(resultado.inserted_id)

    def listar(self, texto=""):
        filtro = {}
        if texto.strip():
            filtro = {"nombre": {"$regex": re.escape(texto.strip()), "$options": "i"}}
        return [self._a_diccionario(d) for d in self.coleccion.find(filtro).sort("nombre", ASCENDING)]

    def obtener(self, id_texto):
        return self._a_diccionario(self.coleccion.find_one({"_id": self._id(id_texto)}))

    def actualizar(self, id_texto, datos):
        cambios = self._validar(datos)
        try:
            resultado = self.coleccion.update_one({"_id": self._id(id_texto)}, {"$set": cambios})
        except DuplicateKeyError:
            raise ValueError(f"Ya existe un producto llamado {cambios['nombre']!r}") from None
        return resultado.matched_count == 1

    def eliminar(self, id_texto):
        return self.coleccion.delete_one({"_id": self._id(id_texto)}).deleted_count == 1
