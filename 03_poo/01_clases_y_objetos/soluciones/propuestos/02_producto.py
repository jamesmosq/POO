"""
Solución - Ejercicio propuesto 02 - Producto
"""

class Producto:
    def __init__(self, nombre, precio, cantidad=0):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def valor_inventario(self):
        return self.precio * self.cantidad

    def reponer(self, unidades):
        if unidades <= 0:
            raise ValueError("Las unidades deben ser positivas")
        self.cantidad += unidades

    def vender(self, unidades):
        if unidades <= 0:
            raise ValueError("Las unidades deben ser positivas")
        if unidades > self.cantidad:
            raise ValueError("No hay suficientes unidades")
        self.cantidad -= unidades
        return self.precio * unidades

    def disponible(self):
        return self.cantidad > 0


# ----------------------------------------------------------------------
# Pruebas
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
