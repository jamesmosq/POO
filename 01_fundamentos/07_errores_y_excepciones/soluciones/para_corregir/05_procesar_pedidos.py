"""
Solución - Ejercicio para corregir 05 - Procesar pedidos

CORRECCIÓN 1 (UnboundLocalError con 'disponible'): except KeyError: pass
silenciaba el error y el programa seguía sin tener el dato. Silenciar
errores casi nunca es buena idea: aquí se debe lanzar el ValueError que pide
el enunciado.

CORRECCIÓN 2 (ValueError sin atrapar): "StockInsuficiente or ValueError"
no significa "cualquiera de los dos". Python evalúa el or primero y da
StockInsuficiente, así que ValueError nunca se atrapaba. Para varias
excepciones se usa una tupla, o mejor, un except para cada una.

CORRECCIÓN 3 (el inventario quedaba negativo): se descontaba antes de
validar. Si la venta falla, el inventario no debe cambiar: primero se
valida y después se modifica.
"""

class StockInsuficiente(Exception):
    pass


def vender(inventario, producto, cantidad):
    if producto not in inventario:
        raise ValueError(f"Producto desconocido: {producto}")  # CORRECCIÓN 1
    if inventario[producto] < cantidad:  # CORRECCIÓN 3
        raise StockInsuficiente(f"No hay suficiente {producto}")
    inventario[producto] -= cantidad


def procesar(inventario, pedidos):
    estados = []
    for producto, cantidad in pedidos:
        try:
            vender(inventario, producto, cantidad)
            estados.append("ok")
        except StockInsuficiente:  # CORRECCIÓN 2
            estados.append("sin stock")
        except ValueError:
            estados.append("desconocido")
    return estados


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    inventario = {"pan": 5}
    estados = procesar(inventario, [("pan", 2), ("pan", 10), ("leche", 1)])
    assert estados == ["ok", "sin stock", "desconocido"], estados
    assert inventario == {"pan": 3}, f"El inventario quedó así: {inventario}"

    try:
        vender({}, "arroz", 1)
        raise AssertionError("Debe lanzar ValueError")
    except ValueError as error:
        assert str(error) == "Producto desconocido: arroz"

    print("Todas las pruebas pasaron")
