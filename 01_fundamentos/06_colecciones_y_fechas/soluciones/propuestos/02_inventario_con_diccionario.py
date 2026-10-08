"""
Solución - Ejercicio propuesto 02 - Inventario con diccionario
"""

def agregar_stock(inventario, producto, cantidad):
    inventario[producto] = inventario.get(producto, 0) + cantidad


def vender(inventario, producto, cantidad):
    if producto not in inventario:
        raise KeyError(f"No existe el producto {producto}")
    if inventario[producto] < cantidad:
        raise ValueError(f"No hay suficiente {producto}")
    # Se valida todo ANTES de modificar: si algo falla, el inventario queda igual.
    inventario[producto] -= cantidad


def agotados(inventario):
    resultado = []
    for producto, cantidad in inventario.items():
        if cantidad == 0:
            resultado.append(producto)
    return sorted(resultado)


def total_unidades(inventario):
    return sum(inventario.values())


# ----------------------------------------------------------------------
# Pruebas
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
