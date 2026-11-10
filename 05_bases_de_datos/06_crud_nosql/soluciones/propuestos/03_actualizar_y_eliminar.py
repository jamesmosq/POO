"""
Solución - Ejercicio propuesto 03 - Actualizar y eliminar
"""
import os

from bson import ObjectId
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "curso_poo")


def _id(id_texto):
    return ObjectId(id_texto) if ObjectId.is_valid(id_texto) else None


def cambiar_precio(coleccion, id_texto, nuevo_precio):
    if nuevo_precio < 0:
        raise ValueError("El precio no puede ser negativo")
    oid = _id(id_texto)
    if oid is None:
        return False
    return coleccion.update_one({"_id": oid}, {"$set": {"precio": nuevo_precio}}).matched_count == 1


def registrar_entrada(coleccion, id_texto, cantidad):
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor que cero")
    oid = _id(id_texto)
    if oid is None:
        return False
    return coleccion.update_one({"_id": oid}, {"$inc": {"stock": cantidad}}).matched_count == 1


def registrar_venta(coleccion, id_texto, cantidad):
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor que cero")
    oid = _id(id_texto)
    if oid is None:
        return False
    resultado = coleccion.update_one({"_id": oid, "stock": {"$gte": cantidad}},
                                     {"$inc": {"stock": -cantidad}})
    return resultado.matched_count == 1


def agregar_etiqueta(coleccion, id_texto, etiqueta):
    oid = _id(id_texto)
    if oid is None:
        return False
    return coleccion.update_one({"_id": oid}, {"$addToSet": {"etiquetas": etiqueta}}).matched_count == 1


def eliminar_producto(coleccion, id_texto):
    oid = _id(id_texto)
    if oid is None:
        return False
    return coleccion.delete_one({"_id": oid}).deleted_count == 1


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
        def leer(id_texto):
            return coleccion.find_one({"_id": ObjectId(id_texto)})

        id_mouse = str(coleccion.insert_one({"nombre": "PRUEBA_EJ_Mouse", "categoria": "Periféricos",
                                             "precio": 50000, "stock": 5}).inserted_id)
        inexistente = str(ObjectId())

        assert cambiar_precio(coleccion, id_mouse, 45000) is True
        documento = leer(id_mouse)
        assert documento["precio"] == 45000
        assert documento.get("nombre") == "PRUEBA_EJ_Mouse" and documento.get("stock") == 5, \
            "cambiar_precio borró otros campos: usa update_one con $set, no replace_one"
        assert cambiar_precio(coleccion, inexistente, 1) is False
        assert cambiar_precio(coleccion, "abc", 1) is False
        debe_fallar(cambiar_precio, coleccion, id_mouse, -1)

        assert registrar_entrada(coleccion, id_mouse, 3) is True
        assert leer(id_mouse)["stock"] == 8, "registrar_entrada debe SUMAR al stock ($inc)"
        debe_fallar(registrar_entrada, coleccion, id_mouse, 0)
        assert registrar_entrada(coleccion, inexistente, 3) is False

        assert registrar_venta(coleccion, id_mouse, 6) is True
        assert leer(id_mouse)["stock"] == 2, "registrar_venta debe RESTAR del stock"
        assert registrar_venta(coleccion, id_mouse, 3) is False, "No hay stock suficiente para vender 3"
        assert leer(id_mouse)["stock"] == 2, "Sin stock suficiente, el stock no cambia"
        assert registrar_venta(coleccion, id_mouse, 2) is True
        assert leer(id_mouse)["stock"] == 0

        assert agregar_etiqueta(coleccion, id_mouse, "oferta") is True
        agregar_etiqueta(coleccion, id_mouse, "oferta")
        agregar_etiqueta(coleccion, id_mouse, "usb")
        assert leer(id_mouse)["etiquetas"] == ["oferta", "usb"], "Las etiquetas no se deben repetir"

        assert eliminar_producto(coleccion, id_mouse) is True
        assert leer(id_mouse) is None
        assert eliminar_producto(coleccion, id_mouse) is False, "Ya no existe"
        assert eliminar_producto(coleccion, "no-es-un-id") is False
    finally:
        coleccion.delete_many({"nombre": {"$regex": "^PRUEBA_EJ_"}})
        cliente.close()
    print("Todas las pruebas pasaron")
