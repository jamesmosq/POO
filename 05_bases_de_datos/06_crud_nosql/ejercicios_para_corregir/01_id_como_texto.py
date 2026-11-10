"""
Ejercicio para corregir 01 - El id como texto
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    insertar() guarda un producto y devuelve su id COMO TEXTO, para poder
    mostrarlo o guardarlo en un Entry. obtener() recibe ese texto y
    devuelve el documento (o None si el id no es válido o no existe).

Ojo: en MongoDB el _id es un ObjectId, no un str. Un ObjectId y su
texto se "ven" iguales al imprimirlos, pero no son lo mismo.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""
import os

from bson import ObjectId
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "curso_poo")


def insertar(coleccion, nombre, precio):
    resultado = coleccion.insert_one({"nombre": nombre, "precio": precio})
    return resultado


def obtener(coleccion, id_texto):
    if not ObjectId.is_valid(id_texto):
        return None
    return coleccion.find_one({"_id": id_texto})


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
