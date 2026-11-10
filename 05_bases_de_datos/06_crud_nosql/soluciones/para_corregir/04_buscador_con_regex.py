"""
Solución - Ejercicio para corregir 04 - Buscador con regex

CORRECCIÓN 1 (distinguía mayúsculas): por defecto la regex distingue
mayúsculas de minúsculas. La opción "i" (ignore case) lo evita:
{"$regex": patron, "$options": "i"}.

CORRECCIÓN 2 (buscar "5.5" también traía "545"): el texto se usaba
como regex, y el punto significa "cualquier carácter". re.escape() convierte
el texto en una regex que lo busca literal. Es lo mismo que escapar % y _
en el LIKE de SQL (tema 05_seguridad_de_contrasenas).
"""
import os
import re

from pymongo import ASCENDING, MongoClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "curso_poo")


def buscar(coleccion, texto):
    patron = re.escape(texto)  # CORRECCIÓN 2
    filtro = {"nombre": {"$regex": patron, "$options": "i"}}  # CORRECCIÓN 1
    cursor = coleccion.find(filtro).sort("nombre", ASCENDING)
    return [producto["nombre"] for producto in cursor]


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
            {"nombre": "PRUEBA_EJ_Tijeras 5.5", "precio": 4000},
            {"nombre": "PRUEBA_EJ_Tijeras 545", "precio": 4200},
            {"nombre": "PRUEBA_EJ_Cuaderno", "precio": 6500},
        ])
        assert de_prueba(buscar(coleccion, "cuaderno")) == ["PRUEBA_EJ_Cuaderno"], \
            "Buscar 'cuaderno' debe encontrar 'Cuaderno' (sin distinguir mayúsculas)"
        assert de_prueba(buscar(coleccion, "TIJERAS")) == ["PRUEBA_EJ_Tijeras 5.5", "PRUEBA_EJ_Tijeras 545"]
        resultado = de_prueba(buscar(coleccion, "5.5"))
        assert resultado == ["PRUEBA_EJ_Tijeras 5.5"], \
            f"Buscar '5.5' debe traer solo 'Tijeras 5.5', trajo {resultado}"
    finally:
        coleccion.delete_many({"nombre": {"$regex": "^PRUEBA_EJ_"}})
        cliente.close()
    print("Todas las pruebas pasaron")
