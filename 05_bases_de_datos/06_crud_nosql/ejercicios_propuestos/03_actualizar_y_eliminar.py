"""
Ejercicio propuesto 03 - Actualizar y eliminar
Nivel: intermedio

Funciones para manejar el inventario. Todas reciben el id como texto.
Si el id no es válido o no existe, devuelven False (sin lanzar errores).

Requisitos:
1. cambiar_precio(coleccion, id_texto, nuevo_precio) -> bool
   Lanza ValueError si el precio es negativo. Cambia SOLO el precio: los
   demás campos deben quedar como estaban (usa $set, no replace_one).
2. registrar_entrada(coleccion, id_texto, cantidad) -> bool
   Suma cantidad al stock con $inc. Si cantidad <= 0, ValueError.
3. registrar_venta(coleccion, id_texto, cantidad) -> bool
   Resta cantidad al stock, pero SOLO si hay stock suficiente. Hazlo en
   una sola operación: pon la condición en el filtro,
       {"_id": ..., "stock": {"$gte": cantidad}}
   y usa $inc con la cantidad en negativo. Devuelve True si se vendió.
   (Así dos cajeros vendiendo al mismo tiempo no dejan el stock negativo.)
4. agregar_etiqueta(coleccion, id_texto, etiqueta) -> bool
   Agrega la etiqueta a la lista "etiquetas" sin repetirla ($addToSet).
5. eliminar_producto(coleccion, id_texto) -> bool
   True si se eliminó un documento.

Pista: update_one devuelve un resultado con matched_count; delete_one uno
con deleted_count.

Conceptos: update_one, $set, $inc, $addToSet, delete_one, filtros como
condición de la actualización.
"""
import os

from bson import ObjectId
from pymongo import MongoClient

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
        def leer(id_texto):
            return coleccion.find_one({"_id": ObjectId(id_texto)})

        id_mouse = str(coleccion.insert_one({"nombre": "PRUEBA_EJ_Mouse", "categoria": "Periféricos",
                                             "precio": 50000, "stock": 5}).inserted_id)
        inexistente = str(ObjectId())

        assert cambiar_precio(coleccion, id_mouse, 45000) is True
        documento = leer(id_mouse)
        assert documento["precio"] == 45000
        assert documento.get("nombre") == "PRUEBA_EJ_Mouse" and documento.get("stock") == 5, \
            "cambiar_precio borró otros campos: usa update_one con $set, no replace_one"
        assert cambiar_precio(coleccion, inexistente, 1) is False
        assert cambiar_precio(coleccion, "abc", 1) is False
        debe_fallar(cambiar_precio, coleccion, id_mouse, -1)

        assert registrar_entrada(coleccion, id_mouse, 3) is True
        assert leer(id_mouse)["stock"] == 8, "registrar_entrada debe SUMAR al stock ($inc)"
        debe_fallar(registrar_entrada, coleccion, id_mouse, 0)
        assert registrar_entrada(coleccion, inexistente, 3) is False

        assert registrar_venta(coleccion, id_mouse, 6) is True
        assert leer(id_mouse)["stock"] == 2, "registrar_venta debe RESTAR del stock"
        assert registrar_venta(coleccion, id_mouse, 3) is False, "No hay stock suficiente para vender 3"
        assert leer(id_mouse)["stock"] == 2, "Sin stock suficiente, el stock no cambia"
        assert registrar_venta(coleccion, id_mouse, 2) is True
        assert leer(id_mouse)["stock"] == 0

        assert agregar_etiqueta(coleccion, id_mouse, "oferta") is True
        agregar_etiqueta(coleccion, id_mouse, "oferta")
        agregar_etiqueta(coleccion, id_mouse, "usb")
        assert leer(id_mouse)["etiquetas"] == ["oferta", "usb"], "Las etiquetas no se deben repetir"

        assert eliminar_producto(coleccion, id_mouse) is True
        assert leer(id_mouse) is None
        assert eliminar_producto(coleccion, id_mouse) is False, "Ya no existe"
        assert eliminar_producto(coleccion, "no-es-un-id") is False
    finally:
        coleccion.delete_many({"nombre": {"$regex": "^PRUEBA_EJ_"}})
        cliente.close()
    print("Todas las pruebas pasaron")
