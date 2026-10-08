"""
Ejercicio propuesto 02 - Producto
Nivel: básico

Requisitos. Crea la clase Producto:
1. __init__(self, nombre, precio, cantidad=0)
2. valor_inventario(): precio * cantidad.
3. reponer(unidades): suma unidades a la cantidad. Lanza ValueError si
   unidades es menor o igual a 0.
4. vender(unidades): resta unidades. Lanza ValueError si unidades es menor
   o igual a 0 o si no hay suficientes. Retorna el valor de la venta
   (precio * unidades).
5. disponible(): True si hay al menos una unidad.

Conceptos: métodos que modifican el estado, validación, valores por
defecto.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
def lanza_value_error(funcion, *argumentos):
    try:
        funcion(*argumentos)
    except ValueError:
        return True
    return False


if __name__ == "__main__":
    cafe = Producto("Café", 12000)
    assert cafe.cantidad == 0
    assert cafe.disponible() is False

    cafe.reponer(10)
    assert cafe.valor_inventario() == 120000
    assert cafe.vender(3) == 36000
    assert cafe.cantidad == 7
    assert cafe.disponible() is True

    assert lanza_value_error(cafe.vender, 8), "No hay 8 unidades"
    assert lanza_value_error(cafe.vender, 0)
    assert lanza_value_error(cafe.reponer, -1)
    assert cafe.cantidad == 7, "Una operación inválida no debe cambiar la cantidad"

    print("Todas las pruebas pasaron")
