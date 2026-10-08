"""
Solución - Ejercicio propuesto 05 - Carrito de compras
"""

class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio


class Item:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def subtotal(self):
        return self.producto.precio * self.cantidad


class Carrito:
    DESCUENTOS = {"DESC10": 10}

    def __init__(self):
        # Un diccionario codigo -> Item permite encontrar un item sin
        # recorrer la lista, y desde Python 3.7 conserva el orden de inserción.
        self.items = {}

    def agregar(self, producto, cantidad=1):
        if producto.codigo in self.items:
            self.items[producto.codigo].cantidad += cantidad
        else:
            self.items[producto.codigo] = Item(producto, cantidad)

    def quitar(self, codigo):
        if codigo not in self.items:
            raise KeyError(codigo)
        del self.items[codigo]

    def cantidad_total(self):
        return sum(item.cantidad for item in self.items.values())

    def total(self, cupon=None):
        bruto = sum(item.subtotal() for item in self.items.values())
        if cupon is None:
            return bruto
        if cupon not in self.DESCUENTOS:
            raise ValueError(f"Cupón inválido: {cupon}")
        return bruto - bruto * self.DESCUENTOS[cupon] / 100

    def resumen(self):
        return [
            f"{item.cantidad} x {item.producto.nombre} = {item.subtotal()}"
            for item in self.items.values()
        ]


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    cafe = Producto("P1", "Café", 12000)
    pan = Producto("P2", "Pan", 500)

    carrito = Carrito()
    carrito.agregar(cafe)
    carrito.agregar(pan, 6)
    carrito.agregar(cafe)
    assert carrito.cantidad_total() == 8
    assert carrito.resumen() == ["2 x Café = 24000", "6 x Pan = 3000"]
    assert carrito.total() == 27000
    assert carrito.total("DESC10") == 24300

    try:
        carrito.total("FALSO")
        raise AssertionError("Un cupón desconocido debe lanzar ValueError")
    except ValueError:
        pass

    carrito.quitar("P2")
    assert carrito.resumen() == ["2 x Café = 24000"]
    try:
        carrito.quitar("P9")
        raise AssertionError("Debe lanzar KeyError")
    except KeyError:
        pass

    otro = Carrito()
    assert otro.cantidad_total() == 0, "Cada carrito es independiente"

    print("Todas las pruebas pasaron")
