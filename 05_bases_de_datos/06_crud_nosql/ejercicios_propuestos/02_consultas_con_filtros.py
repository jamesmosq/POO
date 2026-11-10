"""
Ejercicio propuesto 02 - Consultas con filtros
Nivel: intermedio

Las pruebas cargan unos productos de papelería y tú escribes las
consultas. Recuerda: en MongoDB el filtro es un diccionario y los
operadores empiezan por $.

Requisitos:
1. nombres_por_categoria(coleccion, categoria)
   Lista con los NOMBRES de los productos de esa categoría, ordenados
   alfabéticamente.
2. por_rango_de_precio(coleccion, minimo, maximo)
   Lista de DOCUMENTOS con precio entre minimo y maximo (ambos incluidos),
   ordenados de menor a mayor precio. Usa $gte y $lte.
3. buscar_por_nombre(coleccion, texto)
   Lista con los nombres (ordenados) que CONTIENEN el texto, sin importar
   mayúsculas y minúsculas. Es el LIKE '%texto%' de SQL: usa $regex con
   la opción "i". Ojo: el texto se debe escapar con re.escape(), porque
   caracteres como "." o "+" tienen significado especial en una regex.
4. nombres_con_etiqueta(coleccion, etiqueta)
   Nombres (ordenados) de los productos cuya lista "etiquetas" contiene
   esa etiqueta.

Conceptos: find con filtros, $gte/$lte, $regex, sort, consultas sobre
listas.
"""
import os
import re

from pymongo import ASCENDING, MongoClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "curso_poo")

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
def debe_fallar(funcion, *argumentos, **nombrados):
    try:
        funcion(*argumentos, **nombrados)
    except ValueError:
        return
    raise AssertionError(f"{funcion.__name__}{argumentos} debía lanzar ValueError")


def de_prueba(nombres):
    """Deja solo los nombres creados por las pruebas (la colección puede tener otros)."""
    return [n for n in nombres if n.startswith("PRUEBA_EJ_")]

if __name__ == "__main__":
    cliente = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
    coleccion = cliente[MONGO_DB]["ej_productos"]
    coleccion.delete_many({"nombre": {"$regex": "^PRUEBA_EJ_"}})
    try:
        coleccion.insert_many([
            {"nombre": "PRUEBA_EJ_Lápiz HB", "categoria": "PRUEBA_EJ_Papelería", "precio": 1500,
             "etiquetas": ["escolar"]},
            {"nombre": "PRUEBA_EJ_Cuaderno 100 hojas", "categoria": "PRUEBA_EJ_Papelería", "precio": 6500,
             "etiquetas": ["escolar", "oferta"]},
            {"nombre": "PRUEBA_EJ_Tijeras 5.5", "categoria": "PRUEBA_EJ_Papelería", "precio": 4000,
             "etiquetas": ["oferta"]},
            {"nombre": "PRUEBA_EJ_Tijeras 545", "categoria": "PRUEBA_EJ_Oficina", "precio": 4200},
            {"nombre": "PRUEBA_EJ_Libro de C++", "categoria": "PRUEBA_EJ_Libros", "precio": 120000,
             "etiquetas": []},
            {"nombre": "PRUEBA_EJ_Regla 30cm", "categoria": "PRUEBA_EJ_Geometría", "precio": 3000},
        ])

        assert nombres_por_categoria(coleccion, "PRUEBA_EJ_Papelería") == [
            "PRUEBA_EJ_Cuaderno 100 hojas", "PRUEBA_EJ_Lápiz HB", "PRUEBA_EJ_Tijeras 5.5"], \
            "nombres_por_categoria: deben ser solo los nombres, ordenados"
        assert nombres_por_categoria(coleccion, "PRUEBA_EJ_No existe") == []

        en_rango = por_rango_de_precio(coleccion, 3000, 6500)
        assert all(isinstance(d, dict) for d in en_rango), "por_rango_de_precio devuelve documentos"
        assert de_prueba([d["nombre"] for d in en_rango]) == [
            "PRUEBA_EJ_Regla 30cm", "PRUEBA_EJ_Tijeras 5.5", "PRUEBA_EJ_Tijeras 545",
            "PRUEBA_EJ_Cuaderno 100 hojas"], \
            "Rango con ambos extremos incluidos ($gte y $lte), ordenado por precio"

        assert de_prueba(buscar_por_nombre(coleccion, "CUADERNO")) == ["PRUEBA_EJ_Cuaderno 100 hojas"], \
            "La búsqueda no debe distinguir mayúsculas de minúsculas"
        assert de_prueba(buscar_por_nombre(coleccion, "tijeras")) == [
            "PRUEBA_EJ_Tijeras 5.5", "PRUEBA_EJ_Tijeras 545"]
        assert de_prueba(buscar_por_nombre(coleccion, "5.5")) == ["PRUEBA_EJ_Tijeras 5.5"], \
            "El punto debe buscarse literal: escapa el texto con re.escape()"
        assert de_prueba(buscar_por_nombre(coleccion, "c++")) == ["PRUEBA_EJ_Libro de C++"], \
            "Los + deben buscarse literales: escapa el texto con re.escape()"

        assert de_prueba(nombres_con_etiqueta(coleccion, "oferta")) == [
            "PRUEBA_EJ_Cuaderno 100 hojas", "PRUEBA_EJ_Tijeras 5.5"]
        assert de_prueba(nombres_con_etiqueta(coleccion, "escolar")) == [
            "PRUEBA_EJ_Cuaderno 100 hojas", "PRUEBA_EJ_Lápiz HB"]
    finally:
        coleccion.delete_many({"nombre": {"$regex": "^PRUEBA_EJ_"}})
        cliente.close()
    print("Todas las pruebas pasaron")
