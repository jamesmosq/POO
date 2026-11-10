"""
Ejercicio para corregir 02 - El cursor vacío
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    caros_de_categoria() devuelve una tupla (cantidad, nombres) con los
    productos de una categoría cuyo precio es MAYOR O IGUAL al mínimo.
    Los nombres van ordenados alfabéticamente.

Ojo: find() no devuelve una lista sino un cursor, que se "gasta" al
recorrerlo, igual que un iterador.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""
import os

from pymongo import ASCENDING, MongoClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "curso_poo")


def caros_de_categoria(coleccion, categoria, minimo):
    cursor = coleccion.find({"categoria": categoria, "precio": {"$gt": minimo}})
    cursor = cursor.sort("nombre", ASCENDING)
    cantidad = len(list(cursor))
    nombres = [producto["nombre"] for producto in cursor]
    return cantidad, nombres


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
