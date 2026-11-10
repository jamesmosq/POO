"""
Solución - Ejercicio para corregir 02 - El cursor vacío

CORRECCIÓN 1 (faltaba el producto que cuesta exactamente el mínimo):
$gt es "mayor que". "Mayor o igual" es $gte.

CORRECCIÓN 2 (la lista de nombres salía vacía): list(cursor) recorre el
cursor completo para contar, y después el cursor ya no tiene nada que dar.
Se convierte a lista UNA vez y se usa esa lista para las dos cosas.
"""
import os

from pymongo import ASCENDING, MongoClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "curso_poo")


def caros_de_categoria(coleccion, categoria, minimo):
    cursor = coleccion.find({"categoria": categoria, "precio": {"$gte": minimo}})  # CORRECCIÓN 1
    cursor = cursor.sort("nombre", ASCENDING)
    productos = list(cursor)  # CORRECCIÓN 2
    cantidad = len(productos)
    nombres = [producto["nombre"] for producto in productos]
    return cantidad, nombres


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
        coleccion.insert_many([
            {"nombre": "PRUEBA_EJ_Monitor", "categoria": "PRUEBA_EJ_Pantallas", "precio": 620000},
            {"nombre": "PRUEBA_EJ_Televisor", "categoria": "PRUEBA_EJ_Pantallas", "precio": 1500000},
            {"nombre": "PRUEBA_EJ_Proyector", "categoria": "PRUEBA_EJ_Pantallas", "precio": 900000},
            {"nombre": "PRUEBA_EJ_Portátil", "categoria": "PRUEBA_EJ_Computadores", "precio": 2400000},
        ])
        cantidad, nombres = caros_de_categoria(coleccion, "PRUEBA_EJ_Pantallas", 900000)
        assert nombres, "La lista de nombres salió vacía"
        assert nombres == ["PRUEBA_EJ_Proyector", "PRUEBA_EJ_Televisor"], \
            f"Se esperaban el Proyector (cuesta justo 900000) y el Televisor, salió {nombres}"
        assert cantidad == 2
        assert caros_de_categoria(coleccion, "PRUEBA_EJ_Pantallas", 5000000) == (0, [])
    finally:
        coleccion.delete_many({"nombre": {"$regex": "^PRUEBA_EJ_"}})
        cliente.close()
    print("Todas las pruebas pasaron")
