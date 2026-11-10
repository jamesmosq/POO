"""
Ejemplo 03 - READ: leer documentos
Paso 3 de la ruta del CRUD con MongoDB.

Qué aprendes:
    - find() devuelve un cursor (se recorre con for); find_one() devuelve
      un diccionario o None.
    - Proyección: elegir qué campos traer (como el SELECT col1, col2).
    - Ordenar con sort(), limitar con limit() y contar con
      count_documents().
    - Buscar por _id: el texto hay que convertirlo a ObjectId.

Ejecuta antes 02_insertar.py para tener datos.
"""
import os

from bson import ObjectId
from pymongo import ASCENDING, DESCENDING, MongoClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "curso_poo")


def main():
    cliente = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
    productos = cliente[MONGO_DB]["productos"]

    # ---- Todos los documentos (SELECT * FROM productos) ---------------
    # El filtro vacío {} significa "sin condiciones".
    print("== Todos ==")
    for producto in productos.find({}):
        # Cada producto es un diccionario. Usamos .get() porque no todos
        # los documentos tienen los mismos campos.
        print(f"{producto['nombre']:<25} {producto.get('categoria', '-'):<15} ${producto['precio']:>10,}")

    # ---- Proyección: solo algunos campos ------------------------------
    # SQL: SELECT nombre, precio FROM productos
    # 1 = incluir el campo. El _id viene siempre, salvo que pongas "_id": 0.
    print("\n== Solo nombre y precio ==")
    for producto in productos.find({}, {"nombre": 1, "precio": 1, "_id": 0}):
        print(producto)

    # ---- Ordenar y limitar --------------------------------------------
    # SQL: SELECT ... ORDER BY precio DESC LIMIT 3
    print("\n== Los 3 más caros ==")
    for producto in productos.find().sort("precio", DESCENDING).limit(3):
        print(producto["nombre"], producto["precio"])

    # Ordenar por dos campos: una lista de tuplas.
    print("\n== Por categoría y luego por nombre ==")
    for producto in productos.find().sort([("categoria", ASCENDING), ("nombre", ASCENDING)]):
        print(producto.get("categoria"), "-", producto["nombre"])

    # ---- Contar -------------------------------------------------------
    print("\nTotal de productos:", productos.count_documents({}))

    # ---- Un solo documento --------------------------------------------
    primero = productos.find_one({"categoria": "Audio"})
    print("\nPrimer producto de Audio:", primero)

    # find_one devuelve None si no hay coincidencias: siempre revísalo.
    inexistente = productos.find_one({"categoria": "Juguetes"})
    print("Categoría Juguetes:", inexistente)

    # ---- Buscar por _id -----------------------------------------------
    # Error MUY común: buscar con el id como texto. No encuentra nada,
    # porque en la base el _id es un ObjectId, no un str.
    if primero is not None:
        id_texto = str(primero["_id"])
        print("\nCon texto     ->", productos.find_one({"_id": id_texto}))
        print("Con ObjectId  ->", productos.find_one({"_id": ObjectId(id_texto)})["nombre"])

    # ObjectId("hola") lanza una excepción. Para validar un texto que llega
    # del usuario se usa ObjectId.is_valid().
    print("¿'hola' es un id válido?", ObjectId.is_valid("hola"))

    # ---- El cursor se consume -----------------------------------------
    # Un cursor es como un iterador: después de recorrerlo queda vacío.
    # Si necesitas los datos dos veces, conviértelo a lista.
    cursor = productos.find({"stock": 0})
    agotados = list(cursor)
    print("\nAgotados:", [p["nombre"] for p in agotados])

    cliente.close()


if __name__ == "__main__":
    main()
