"""
Ejercicio para corregir 05 - Dinero
Nivel: avanzado
Errores a encontrar: 3

Qué debería hacer el programa:
    - Dinero guarda la cantidad con Decimal para que las sumas sean exactas.
    - Se pueden sumar con + y también con sum().
    - Multiplicar por un número retorna un Dinero.

        Dinero(0.1) + Dinero(0.2) == Dinero(0.3)    -> True
        sum([Dinero(1000), Dinero(500)])            -> Dinero(1500)
        Dinero(10) * 3                              -> Dinero(30)

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""
from decimal import Decimal


class Dinero:
    def __init__(self, cantidad):
        self.cantidad = Decimal(cantidad)

    def __add__(self, otro):
        return Dinero(self.cantidad + otro.cantidad)

    def __mul__(self, factor):
        return self.cantidad * Decimal(str(factor))

    def __eq__(self, otro):
        return isinstance(otro, Dinero) and self.cantidad == otro.cantidad

    def __repr__(self):
        return f"Dinero({self.cantidad})"


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert Dinero(0.1) + Dinero(0.2) == Dinero(0.3), Dinero(0.1) + Dinero(0.2)
    assert sum([Dinero(1000), Dinero(500)]) == Dinero(1500)
    triple = Dinero(10) * 3
    assert isinstance(triple, Dinero) and triple == Dinero(30), repr(triple)

    print("Todas las pruebas pasaron")
