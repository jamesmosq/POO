"""
Ejemplo 06 - DELETE: eliminar documentos
Paso 6 de la ruta del CRUD con MongoDB.

Qué aprendes:
    - delete_one(filtro) borra el primero que coincida.
    - delete_many(filtro) borra todos los que coincidan.
    - deleted_count dice cuántos se borraron (0 si no había ninguno).
    - Por qué delete_many({}) es peligroso.

Ejecuta antes 02_insertar.py para tener datos.
"""
import os

from bson import ObjectId
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "curso_poo")


def eliminar_por_id(productos, id_texto):
    """Elimina un producto a partir del id en texto. Devuelve True si borró."""
    if not ObjectId.is_valid(id_texto):
        return False
    resultado = productos.delete_one({"_id": ObjectId(id_texto)})
    return resultado.deleted_count == 1


def main():
    cliente = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
    productos = cliente[MONGO_DB]["productos"]

    # Creamos documentos propios para borrarlos sin tocar la muestra.
    resultado = productos.insert_many([
        {"nombre": "Temporal 06 A", "categoria": "Temporales", "precio": 1, "stock": 1},
        {"nombre": "Temporal 06 B", "categoria": "Temporales", "precio": 2, "stock": 1},
        {"nombre": "Temporal 06 C", "categoria": "Temporales", "precio": 3, "stock": 1},
    ])
    primer_id = str(resultado.inserted_ids[0])
    print("Temporales creados:", productos.count_documents({"categoria": "Temporales"}))

    # ---- delete_one por _id -------------------------------------------
    print("¿Se borró el primero?", eliminar_por_id(productos, primer_id))
    print("¿Se borró otra vez?  ", eliminar_por_id(productos, primer_id))   # ya no existe
    print("¿Id inválido?        ", eliminar_por_id(productos, "no-es-un-id"))

    # ---- delete_many con filtro ---------------------------------------
    # SQL: DELETE FROM productos WHERE categoria = 'Temporales'
    resultado = productos.delete_many({"categoria": "Temporales"})
    print("delete_many borró:", resultado.deleted_count)

    # ---- Cuidado ------------------------------------------------------
    # delete_many({}) borra TODOS los documentos de la colección, igual que
    # un DELETE sin WHERE. No hay confirmación ni papelera.
    # productos.delete_many({})        <- no lo ejecutes sin pensarlo
    #
    # Y productos.drop() borra la colección completa (como DROP TABLE).

    print("Productos que quedan:", productos.count_documents({}))
    cliente.close()


if __name__ == "__main__":
    main()
