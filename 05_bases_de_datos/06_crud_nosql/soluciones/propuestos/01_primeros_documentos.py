"""
Solución - Ejercicio propuesto 01 - Primeros documentos
"""
import os

from bson import ObjectId
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "curso_poo")


def insertar_producto(coleccion, nombre, precio, stock=0):
    nombre = nombre.strip()
    if not nombre:
        raise ValueError("El nombre es obligatorio")
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
    resultado = coleccion.insert_one({"nombre": nombre, "precio": precio, "stock": stock})
    return str(resultado.inserted_id)


def obtener_producto(coleccion, id_texto):
    if not ObjectId.is_valid(id_texto):
        return None
    return coleccion.find_one({"_id": ObjectId(id_texto)})


def contar_agotados(coleccion):
    return coleccion.count_documents({"stock": 0})


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
        agotados_antes = contar_agotados(coleccion)

        id_lapiz = insertar_producto(coleccion, "PRUEBA_EJ_Lápiz", 1500, 10)
        assert isinstance(id_lapiz, str), "insertar_producto debe devolver el id como texto (str)"
        documento = coleccion.find_one({"_id": ObjectId(id_lapiz)})
        assert documento is not None, "El producto no quedó guardado en la colección"
        assert documento["nombre"] == "PRUEBA_EJ_Lápiz"
        assert documento["precio"] == 1500 and documento["stock"] == 10

        id_borrador = insertar_producto(coleccion, "   PRUEBA_EJ_Borrador  ", 800)
        documento = coleccion.find_one({"_id": ObjectId(id_borrador)})
        assert documento["nombre"] == "PRUEBA_EJ_Borrador", "Hay que quitar los espacios del nombre"
        assert documento["stock"] == 0, "Si no se indica, el stock es 0"

        debe_fallar(insertar_producto, coleccion, "", 100)
        debe_fallar(insertar_producto, coleccion, "    ", 100)
        debe_fallar(insertar_producto, coleccion, "PRUEBA_EJ_Malo", -5)
        assert coleccion.count_documents({"nombre": "PRUEBA_EJ_Malo"}) == 0, \
            "Con datos inválidos no se debe insertar nada"

        encontrado = obtener_producto(coleccion, id_lapiz)
        assert encontrado is not None and encontrado["nombre"] == "PRUEBA_EJ_Lápiz", \
            "obtener_producto debe buscar por _id convirtiendo el texto a ObjectId"
        assert obtener_producto(coleccion, str(ObjectId())) is None, "Un id que no existe da None"
        assert obtener_producto(coleccion, "no-es-un-id") is None, "Un id inválido da None, sin error"

        insertar_producto(coleccion, "PRUEBA_EJ_Compás", 9000, 0)
        assert contar_agotados(coleccion) == agotados_antes + 2, \
            "contar_agotados debe contar los documentos con stock 0"
    finally:
        coleccion.delete_many({"nombre": {"$regex": "^PRUEBA_EJ_"}})
        cliente.close()
    print("Todas las pruebas pasaron")
