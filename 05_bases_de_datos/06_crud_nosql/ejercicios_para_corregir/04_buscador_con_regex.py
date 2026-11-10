"""
Ejercicio para corregir 04 - Buscador con regex
Nivel: intermedio
Errores a encontrar: 2

Qué debería hacer el programa:
    buscar() devuelve, ordenados, los nombres de los productos que
    CONTIENEN el texto buscado, sin importar mayúsculas o minúsculas.
    Es el equivalente de LIKE '%texto%' en SQL.

Ojo: $regex recibe una expresión regular, no un texto común. En una
regex el punto significa "cualquier carácter".

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""
import os
import re

from pymongo import ASCENDING, MongoClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "curso_poo")


def buscar(coleccion, texto):
    patron = texto
    filtro = {"nombre": {"$regex": patron}}
    cursor = coleccion.find(filtro).sort("nombre", ASCENDING)
    return [producto["nombre"] for producto in cursor]


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
