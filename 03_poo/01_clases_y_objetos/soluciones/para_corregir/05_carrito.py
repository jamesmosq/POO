"""
Solución - Ejercicio para corregir 05 - Carrito

CORRECCIÓN 1: item.cantidad + cantidad calcula la suma pero no la guarda.
Para modificar el atributo se usa +=.

CORRECCIÓN 2: el total sumaba solo los precios e ignoraba la cantidad de
cada item.

CORRECCIÓN 3: items=[] como valor por defecto crea UNA sola lista cuando se
define la clase, y todos los carritos creados sin argumento la comparten.
Se usa None y se crea una lista nueva en cada objeto.
"""

class Item:
    def __init__(self, producto, precio, cantidad):
        self.producto = producto
        self.precio = precio
        self.cantidad = cantidad


class Carrito:
    def __init__(self, items=None):  # CORRECCIÓN 3
        self.items = [] if items is None else list(items)

    def agregar(self, producto, precio, cantidad=1):
        for item in self.items:
            if item.producto == producto:
                item.cantidad += cantidad  # CORRECCIÓN 1
                return
        self.items.append(Item(producto, precio, cantidad))

    def total(self):
        return sum(item.precio * item.cantidad for item in self.items)  # CORRECCIÓN 2


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    c = Carrito()
    c.agregar("Café", 12000, 1)
    c.agregar("Café", 12000, 1)
    c.agregar("Pan", 500, 6)
    assert len(c.items) == 2
    assert c.items[0].cantidad == 2, f"El café quedó con cantidad {c.items[0].cantidad}"
    assert c.total() == 27000, f"total() retornó {c.total()}"

    otro = Carrito()
    assert otro.items == [], f"Un carrito nuevo ya tiene items: {len(otro.items)}"

    print("Todas las pruebas pasaron")
