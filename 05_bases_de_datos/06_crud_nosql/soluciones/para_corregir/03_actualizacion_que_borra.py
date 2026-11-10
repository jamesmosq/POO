"""
Solución - Ejercicio para corregir 03 - La actualización que borra

CORRECCIÓN 1 (se perdían el nombre y el stock): replace_one reemplaza el
documento COMPLETO por el que recibe, que solo tenía el precio. Para cambiar
algunos campos se usa update_one con el operador $set.

CORRECCIÓN 2 (el stock no sumaba): $set reemplaza el valor (el stock
quedaba igual a la cantidad que llegó). Para sumar se usa $inc, que además
hace la suma en el servidor sin tener que leer el valor antes.
"""
import os

from bson import ObjectId
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "curso_poo")


def cambiar_precio(coleccion, id_texto, precio):
    coleccion.update_one({"_id": ObjectId(id_texto)}, {"$set": {"precio": precio}})  # CORRECCIÓN 1


def registrar_entrada(coleccion, id_texto, cantidad):
    coleccion.update_one({"_id": ObjectId(id_texto)}, {"$inc": {"stock": cantidad}})  # CORRECCIÓN 2


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
        id_texto = str(coleccion.insert_one({"nombre": "PRUEBA_EJ_Teclado", "categoria": "Periféricos",
                                             "precio": 180000, "stock": 5}).inserted_id)

        cambiar_precio(coleccion, id_texto, 150000)
        documento = coleccion.find_one({"_id": ObjectId(id_texto)})
        assert documento["precio"] == 150000
        assert documento.get("nombre") == "PRUEBA_EJ_Teclado", \
            f"cambiar_precio() borró los demás campos. El documento quedó así: {documento}"
        assert documento.get("stock") == 5

        registrar_entrada(coleccion, id_texto, 3)
        stock = coleccion.find_one({"_id": ObjectId(id_texto)})["stock"]
        assert stock == 8, f"Había 5 y llegaron 3: el stock debe ser 8, quedó en {stock}"
    finally:
        coleccion.delete_many({"nombre": {"$regex": "^PRUEBA_EJ_"}})
        cliente.close()
    print("Todas las pruebas pasaron")
