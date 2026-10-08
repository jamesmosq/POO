"""
Solución - Ejercicio para corregir 03 - Inventario como contenedor

CORRECCIÓN 1 (TypeError: 'str' object cannot be interpreted as an
integer): __len__ debe retornar un entero, no un texto.

CORRECCIÓN 2 (TypeError: iter() returned non-iterator of type 'list'):
__iter__ debe retornar un iterador, y una lista no lo es (es un iterable).
iter(lista) crea el iterador. También sirve escribir __iter__ como
generador con "yield from self._productos".
"""

class Inventario:
    def __init__(self):
        self._productos = []

    def agregar(self, producto):
        self._productos.append(producto)

    def __len__(self):
        return len(self._productos)  # CORRECCIÓN 1

    def __contains__(self, producto):
        return producto in self._productos

    def __iter__(self):
        return iter(self._productos)  # CORRECCIÓN 2


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    inv = Inventario()
    inv.agregar("pan")
    inv.agregar("leche")

    assert len(inv) == 2
    assert "pan" in inv
    assert [p for p in inv] == ["pan", "leche"]

    print("Todas las pruebas pasaron")
