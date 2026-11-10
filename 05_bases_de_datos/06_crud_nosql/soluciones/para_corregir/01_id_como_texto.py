"""
Solución - Ejercicio para corregir 01 - El id como texto

CORRECCIÓN 1 (no devolvía un texto): insert_one() no devuelve el id
sino un objeto InsertOneResult. El id está en resultado.inserted_id, y es un
ObjectId; se convierte a texto con str().

CORRECCIÓN 2 (nunca encontraba nada): se buscaba el _id con el texto.
En la base el _id es un ObjectId, y un str nunca es igual a un ObjectId,
así que find_one devolvía None. Hay que convertir: ObjectId(id_texto).
"""
import os

from bson import ObjectId
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "curso_poo")


def insertar(coleccion, nombre, precio):
    resultado = coleccion.insert_one({"nombre": nombre, "precio": precio})
    return str(resultado.inserted_id)  # CORRECCIÓN 1


def obtener(coleccion, id_texto):
    if not ObjectId.is_valid(id_texto):
        return None
    return coleccion.find_one({"_id": ObjectId(id_texto)})  # CORRECCIÓN 2


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
def de_prueba(nombres):
    """Deja solo los nombres creados por las pruebas (la colección puede tener otros)."""
    return [n for n in nombres if n.startswith("PRUEBA_EJ_")]


if __name__ == "__main__":
    cliente = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
    coleccion = cliente[MONGO_DB]["ej_productos"]
    coleccion.delete_many({"nombre": {"$regex": "^PRUEBA_EJ_"}})
    try:
        id_texto = insertar(coleccion, "PRUEBA_EJ_Lápiz", 1500)
        assert isinstance(id_texto, str), f"insertar() debe devolver un str, devolvió {type(id_texto).__name__}"
        assert ObjectId.is_valid(id_texto), "El texto devuelto debe ser el id del documento"

        documento = obtener(coleccion, id_texto)
        assert documento is not None, "obtener() no encontró el producto que se acaba de insertar"
        assert documento["nombre"] == "PRUEBA_EJ_Lápiz"
        assert obtener(coleccion, "no-es-un-id") is None
        assert obtener(coleccion, str(ObjectId())) is None
    finally:
        coleccion.delete_many({"nombre": {"$regex": "^PRUEBA_EJ_"}})
        cliente.close()
    print("Todas las pruebas pasaron")
