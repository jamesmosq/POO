"""
Ejercicio para corregir 03 - La actualización que borra
Nivel: intermedio
Errores a encontrar: 2

Qué debería hacer el programa:
    cambiar_precio() cambia SOLO el precio de un producto.
    registrar_entrada() SUMA unidades al stock (llegó mercancía).
    Los demás campos del documento deben quedar intactos.

Ojo: después de ejecutar el código con errores, mira el documento en
MongoDB Compass y fíjate qué campos le quedan.

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


def cambiar_precio(coleccion, id_texto, precio):
    coleccion.replace_one({"_id": ObjectId(id_texto)}, {"precio": precio})


def registrar_entrada(coleccion, id_texto, cantidad):
    coleccion.update_one({"_id": ObjectId(id_texto)}, {"$set": {"stock": cantidad}})


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
