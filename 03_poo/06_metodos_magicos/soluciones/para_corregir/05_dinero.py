"""
Solución - Ejercicio para corregir 05 - Dinero

CORRECCIÓN 1 (0.1 + 0.2 no daba 0.3): Decimal(0.1) recibe el float 0.1,
que ya es inexacto (0.1000000000000000055...). Para obtener exactamente 0.1
hay que pasarle el texto: Decimal(str(cantidad)).

CORRECCIÓN 2 (TypeError: unsupported operand type(s) for +: 'int' and
'Dinero'): sum() empieza con 0 y hace 0 + Dinero(...). int no sabe sumar
Dinero, así que Python busca __radd__ en Dinero, que no existía.

CORRECCIÓN 3 (la multiplicación retornaba un Decimal): __mul__ debe
retornar un Dinero, para que el resultado siga siendo dinero.
"""

from decimal import Decimal


class Dinero:
    def __init__(self, cantidad):
        self.cantidad = Decimal(str(cantidad))  # CORRECCIÓN 1

    def __add__(self, otro):
        return Dinero(self.cantidad + otro.cantidad)

    def __radd__(self, otro):  # CORRECCIÓN 2
        if otro == 0:
            return self
        return self + otro

    def __mul__(self, factor):
        return Dinero(self.cantidad * Decimal(str(factor)))  # CORRECCIÓN 3

    def __eq__(self, otro):
        return isinstance(otro, Dinero) and self.cantidad == otro.cantidad

    def __repr__(self):
        return f"Dinero({self.cantidad})"


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert Dinero(0.1) + Dinero(0.2) == Dinero(0.3), Dinero(0.1) + Dinero(0.2)
    assert sum([Dinero(1000), Dinero(500)]) == Dinero(1500)
    triple = Dinero(10) * 3
    assert isinstance(triple, Dinero) and triple == Dinero(30), repr(triple)

    print("Todas las pruebas pasaron")
