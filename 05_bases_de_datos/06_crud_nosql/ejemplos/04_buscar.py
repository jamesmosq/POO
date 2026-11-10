"""
Ejemplo 04 - Filtros: el WHERE de MongoDB
Paso 4 de la ruta del CRUD con MongoDB.

Qué aprendes:
    - Los filtros son diccionarios. Los operadores empiezan por $.
    - Comparación: $gt, $gte, $lt, $lte, $ne, $in.
    - Combinar condiciones (AND implícito y $or).
    - Buscar texto parcial con $regex (el LIKE de SQL) de forma segura.
    - Buscar dentro de listas y de documentos anidados.

Ejecuta antes 02_insertar.py para tener datos.

Tabla de equivalencias:
    SQL                              MongoDB
    ------------------------------   -------------------------------------
    WHERE stock = 0                  {"stock": 0}
    WHERE precio > 100000            {"precio": {"$gt": 100000}}
    WHERE precio BETWEEN a AND b     {"precio": {"$gte": a, "$lte": b}}
    WHERE categoria IN ('A','B')     {"categoria": {"$in": ["A", "B"]}}
    WHERE a = 1 AND b = 2            {"a": 1, "b": 2}
    WHERE a = 1 OR b = 2             {"$or": [{"a": 1}, {"b": 2}]}
    WHERE nombre LIKE '%usb%'        {"nombre": {"$regex": "usb", "$options": "i"}}
"""
import os
import re

from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "curso_poo")


def mostrar(titulo, cursor):
    print(f"\n== {titulo} ==")
    for producto in cursor:
        print(f"  {producto['nombre']:<25} ${producto['precio']:>10,}  stock {producto['stock']}")


def buscar_por_nombre(productos, texto):
    """Busca productos cuyo nombre CONTENGA el texto, sin importar mayúsculas.

    re.escape() es importante: en una expresión regular caracteres como
    . + * ( ) tienen significado especial. Sin escapar, buscar "C++"
    falla y buscar "." encuentra todo. Es la misma idea que escapar % y _
    en el LIKE de SQL.
    """
    patron = re.escape(texto)
    return productos.find({"nombre": {"$regex": patron, "$options": "i"}}).sort("nombre")


def main():
    cliente = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
    productos = cliente[MONGO_DB]["productos"]

    # Igualdad
    mostrar("Categoría Periféricos", productos.find({"categoria": "Periféricos"}))

    # Comparación
    mostrar("Precio mayor a 300.000", productos.find({"precio": {"$gt": 300000}}))

    # Rango: dos operadores sobre el mismo campo
    mostrar("Precio entre 50.000 y 200.000",
            productos.find({"precio": {"$gte": 50000, "$lte": 200000}}).sort("precio"))

    # AND implícito: varios campos en el mismo diccionario
    mostrar("Almacenamiento con más de 10 unidades",
            productos.find({"categoria": "Almacenamiento", "stock": {"$gt": 10}}))

    # OR
    mostrar("Agotados o muy caros",
            productos.find({"$or": [{"stock": 0}, {"precio": {"$gte": 1000000}}]}))

    # IN
    mostrar("Audio o Pantallas", productos.find({"categoria": {"$in": ["Audio", "Pantallas"]}}))

    # Texto parcial (LIKE)
    mostrar("Nombre contiene 'usb'", buscar_por_nombre(productos, "usb"))
    mostrar("Nombre contiene '.' (escapado)", buscar_por_nombre(productos, "."))

    # Listas: {"etiquetas": "gamer"} encuentra los documentos cuya lista
    # "etiquetas" CONTIENE "gamer". No hace falta ningún operador especial.
    mostrar("Con la etiqueta 'gamer'", productos.find({"etiquetas": "gamer"}))

    # Documentos anidados: se usa la notación de punto entre comillas.
    mostrar("Con 16 GB de RAM", productos.find({"especificaciones.ram_gb": 16}))

    # $exists: documentos que tienen (o no) un campo.
    mostrar("Sin etiquetas", productos.find({"etiquetas": {"$exists": False}}))

    cliente.close()


if __name__ == "__main__":
    main()
