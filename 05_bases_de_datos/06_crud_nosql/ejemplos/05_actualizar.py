"""
Ejemplo 05 - UPDATE: modificar documentos
Paso 5 de la ruta del CRUD con MongoDB.

Qué aprendes:
    - update_one(filtro, cambios) y update_many(filtro, cambios).
    - Los cambios SIEMPRE llevan un operador:
        $set       cambia (o crea) campos
        $inc       suma a un número (resta si es negativo)
        $unset     elimina un campo
        $push      agrega a una lista
        $addToSet  agrega a una lista solo si no está
    - matched_count (cuántos coincidieron) y modified_count (cuántos
      cambiaron de verdad).
    - Por qué NO usar replace_one para cambiar un campo.

Ejecuta antes 02_insertar.py para tener datos.
"""
import os

from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "curso_poo")


def main():
    cliente = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
    productos = cliente[MONGO_DB]["productos"]

    # Trabajamos sobre un documento propio para no dañar los de muestra.
    productos.delete_many({"nombre": "Producto de prueba 05"})
    id_prueba = productos.insert_one(
        {"nombre": "Producto de prueba 05", "categoria": "Pruebas", "precio": 10000, "stock": 5}
    ).inserted_id
    print("Antes:", productos.find_one({"_id": id_prueba}))

    # ---- $set: cambiar campos -----------------------------------------
    # SQL: UPDATE productos SET precio = 12000 WHERE _id = ...
    resultado = productos.update_one({"_id": id_prueba}, {"$set": {"precio": 12000}})
    print(f"\n$set -> coincidieron {resultado.matched_count}, modificados {resultado.modified_count}")

    # Si el valor ya era ese, coincide pero NO se modifica.
    resultado = productos.update_one({"_id": id_prueba}, {"$set": {"precio": 12000}})
    print(f"$set repetido -> coincidieron {resultado.matched_count}, modificados {resultado.modified_count}")

    # $set también crea campos que no existían (esquema flexible).
    productos.update_one({"_id": id_prueba}, {"$set": {"proveedor": "Distribuidora ABC"}})

    # ---- $inc: sumar o restar -----------------------------------------
    # Ideal para inventarios: la base hace la suma, no hay que leer antes.
    productos.update_one({"_id": id_prueba}, {"$inc": {"stock": 10}})   # entran 10
    productos.update_one({"_id": id_prueba}, {"$inc": {"stock": -3}})   # se venden 3

    # ---- Listas -------------------------------------------------------
    productos.update_one({"_id": id_prueba}, {"$push": {"etiquetas": "oferta"}})
    productos.update_one({"_id": id_prueba}, {"$addToSet": {"etiquetas": "oferta"}})  # no se repite
    productos.update_one({"_id": id_prueba}, {"$addToSet": {"etiquetas": "nuevo"}})

    # ---- $unset: quitar un campo --------------------------------------
    productos.update_one({"_id": id_prueba}, {"$unset": {"proveedor": ""}})

    print("\nDespués:", productos.find_one({"_id": id_prueba}))

    # ---- Varios operadores en una sola operación ----------------------
    productos.update_one({"_id": id_prueba}, {"$set": {"categoria": "Pruebas 2"}, "$inc": {"stock": 1}})

    # ---- update_many ---------------------------------------------------
    # SQL: UPDATE productos SET agotado = TRUE WHERE stock = 0
    resultado = productos.update_many({"stock": 0}, {"$set": {"agotado": True}})
    print(f"\nMarcados como agotados: {resultado.modified_count}")

    # ---- El error clásico: replace_one --------------------------------
    # replace_one CAMBIA EL DOCUMENTO COMPLETO por el que le pases. Si solo
    # pones el precio, se pierden el nombre, el stock, etc.
    productos.replace_one({"_id": id_prueba}, {"precio": 99})
    print("\nTras replace_one({'precio': 99}):", productos.find_one({"_id": id_prueba}))
    print("¡Se perdieron los demás campos! Para cambiar campos usa update_one con $set.")

    # Y update_one sin operador lanza ValueError: PyMongo te protege.
    try:
        productos.update_one({"_id": id_prueba}, {"precio": 99})
    except ValueError as error:
        print("update_one sin $:", error)

    productos.delete_one({"_id": id_prueba})
    cliente.close()


if __name__ == "__main__":
    main()
