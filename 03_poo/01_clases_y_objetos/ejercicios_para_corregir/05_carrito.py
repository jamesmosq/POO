"""
Ejercicio para corregir 05 - Carrito
Nivel: avanzado
Errores a encontrar: 3

Qué debería hacer el programa:
    - Item(producto, precio, cantidad).
    - Carrito.agregar(producto, precio, cantidad): si el producto ya está,
      suma la cantidad al item existente.
    - Carrito.total(): suma de precio * cantidad de todos los items.
    - Cada carrito es independiente de los demás.

        c = Carrito()
        c.agregar("Café", 12000, 1)
        c.agregar("Café", 12000, 1)
        c.agregar("Pan", 500, 6)
        len(c.items) -> 2
        c.total()    -> 27000

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class Item:
    def __init__(self, producto, precio, cantidad):
        self.producto = producto
        self.precio = precio
        self.cantidad = cantidad


class Carrito:
    def __init__(self, items=[]):
        self.items = items

    def agregar(self, producto, precio, cantidad=1):
        for item in self.items:
            if item.producto == producto:
                item.cantidad + cantidad
                return
        self.items.append(Item(producto, precio, cantidad))

    def total(self):
        return sum(item.precio for item in self.items)


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
