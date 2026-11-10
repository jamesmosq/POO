"""
Ejemplo 02 - CREATE: insertar documentos
Paso 2 de la ruta del CRUD con MongoDB.

Qué aprendes:
    - insert_one() para un documento, insert_many() para varios.
    - Qué es el _id y el ObjectId que MongoDB genera solo.
    - Que los documentos de una colección no tienen que ser iguales
      (esquema flexible), y que un campo puede guardar una lista.

Este ejemplo también deja cargados los datos de muestra que usan los
ejemplos 03 a 08. Si la colección ya tiene datos, no los vuelve a insertar.
"""
import os

from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "curso_poo")

# En MySQL cada fila es una tupla; en MongoDB cada documento es un
# diccionario de Python. No hace falta crear la tabla antes.
PRODUCTOS_DE_MUESTRA = [
    {"nombre": "Teclado mecánico", "categoria": "Periféricos", "precio": 180000, "stock": 12,
     "etiquetas": ["gamer", "usb"]},
    {"nombre": "Mouse inalámbrico", "categoria": "Periféricos", "precio": 65000, "stock": 30,
     "etiquetas": ["inalámbrico"]},
    {"nombre": "Monitor 24 pulgadas", "categoria": "Pantallas", "precio": 620000, "stock": 5},
    {"nombre": "Portátil 14 pulgadas", "categoria": "Computadores", "precio": 2450000, "stock": 3,
     "especificaciones": {"ram_gb": 16, "disco_gb": 512}},
    {"nombre": "Memoria USB 64 GB", "categoria": "Almacenamiento", "precio": 35000, "stock": 50},
    {"nombre": "Disco SSD 1 TB", "categoria": "Almacenamiento", "precio": 290000, "stock": 8},
    {"nombre": "Diadema con micrófono", "categoria": "Audio", "precio": 95000, "stock": 0},
]


def main():
    cliente = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
    productos = cliente[MONGO_DB]["productos"]

    # ---- insert_one: un documento ------------------------------------
    # MongoDB no impide nombres repetidos (la única clave única por defecto
    # es el _id), así que si ejecutas el ejemplo varias veces insertaría
    # otra "Cámara web HD" cada vez. Por ahora lo revisamos a mano; el
    # ejemplo 07 muestra cómo hacer que la base lo impida (índice único).
    if productos.count_documents({"nombre": "Cámara web HD"}) == 0:
        nuevo = {"nombre": "Cámara web HD", "categoria": "Periféricos", "precio": 120000, "stock": 7}
        resultado = productos.insert_one(nuevo)

        # Si no le das un _id, MongoDB crea uno (un ObjectId) y PyMongo
        # además lo agrega al diccionario que le pasaste.
        print("Id generado:", resultado.inserted_id)
        print("Tipo del id:", type(resultado.inserted_id).__name__)
        print("El diccionario ahora tiene _id:", nuevo["_id"])

        # El ObjectId NO es un texto. Para mostrarlo en pantalla o
        # guardarlo en un Entry de Tkinter se convierte con str().
        print("Como texto:", str(resultado.inserted_id))
    else:
        print("La 'Cámara web HD' ya existía; no se insertó de nuevo")

    # ---- insert_many: varios documentos -------------------------------
    # Solo cargamos la muestra si todavía no está (para no duplicar datos
    # cada vez que ejecutas el ejemplo).
    if productos.count_documents({"nombre": "Teclado mecánico"}) == 0:
        # Copiamos cada diccionario para no modificar la lista original
        # (insert_many les agrega el _id).
        resultado = productos.insert_many([dict(p) for p in PRODUCTOS_DE_MUESTRA])
        print(f"Se insertaron {len(resultado.inserted_ids)} productos de muestra")
    else:
        print("Los productos de muestra ya estaban cargados")

    # Observa que los documentos no tienen todos los mismos campos:
    # "etiquetas" y "especificaciones" solo aparecen en algunos. En SQL
    # tendrías que agregar columnas (con NULL) u otras tablas.
    print("Total de productos:", productos.count_documents({}))

    cliente.close()


if __name__ == "__main__":
    main()
