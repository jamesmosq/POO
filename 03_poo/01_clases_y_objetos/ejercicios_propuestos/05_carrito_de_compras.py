"""
Ejercicio propuesto 05 - Carrito de compras
Nivel: avanzado

Vas a diseñar tres clases que trabajan juntas.

Requisitos:
1. Producto(codigo, nombre, precio).
2. Item(producto, cantidad):
   - subtotal(): precio del producto por la cantidad.
3. Carrito():
   - agregar(producto, cantidad=1): si el producto ya está en el carrito
     (mismo codigo), suma la cantidad al item existente en lugar de crear
     otro.
   - quitar(codigo): elimina el item. Lanza KeyError si no está.
   - cantidad_total(): suma de las cantidades de todos los items.
   - total(cupon=None): suma de subtotales. El cupón "DESC10" descuenta
     10 %. Cualquier otro cupón distinto de None lanza ValueError.
   - resumen(): lista de textos "2 x Café = 24000" en el orden en que se
     agregaron.

Diseña tú los atributos internos. Piensa: ¿qué estructura te sirve mejor
para encontrar un item por su código?

Conceptos: diseño de clases, composición, responsabilidades.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
