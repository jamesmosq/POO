"""
Ejercicio propuesto 02 - Inventario con diccionario
Nivel: básico

El inventario es un diccionario: la clave es el nombre del producto y el
valor es la cantidad disponible.
    {"manzana": 10, "pera": 0}

Requisitos:
1. agregar_stock(inventario, producto, cantidad): suma la cantidad; si el
   producto no existe, lo crea. Pista: inventario.get(producto, 0).
2. vender(inventario, producto, cantidad): resta la cantidad.
   - Lanza KeyError si el producto no existe.
   - Lanza ValueError si no hay suficiente cantidad.
3. agotados(inventario): retorna la lista de productos con cantidad 0,
   ordenada alfabéticamente.
4. total_unidades(inventario): suma de todas las cantidades. Pista:
   inventario.values().

Conceptos: diccionarios, get, items, values, excepciones.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    inv = {"manzana": 10, "pera": 0}
    agregar_stock(inv, "manzana", 5)
    agregar_stock(inv, "uva", 3)
    assert inv == {"manzana": 15, "pera": 0, "uva": 3}

    vender(inv, "uva", 3)
    assert inv["uva"] == 0
    assert agotados(inv) == ["pera", "uva"]
    assert total_unidades(inv) == 15

    try:
        vender(inv, "manzana", 100)
        raise AssertionError("Vender más de lo que hay debe lanzar ValueError")
    except ValueError:
        pass
    assert inv["manzana"] == 15, "Si la venta falla, el inventario no debe cambiar"

    try:
        vender(inv, "kiwi", 1)
        raise AssertionError("Un producto inexistente debe lanzar KeyError")
    except KeyError:
        pass

    print("Todas las pruebas pasaron")
