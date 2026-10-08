"""
Solución - Ejercicio propuesto 02 - Vector con operadores
"""

import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y)

    def __sub__(self, otro):
        return Vector(self.x - otro.x, self.y - otro.y)

    def __mul__(self, escalar):
        return Vector(self.x * escalar, self.y * escalar)

    def __rmul__(self, escalar):
        # 3 * v: int no sabe multiplicar por un Vector, así que Python llama
        # a v.__rmul__(3). La multiplicación por escalar es conmutativa.
        return self * escalar

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __eq__(self, otro):
        if not isinstance(otro, Vector):
            return NotImplemented
        return (self.x, self.y) == (otro.x, otro.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    a = Vector(1, 2)
    b = Vector(3, 4)

    assert a + b == Vector(4, 6)
    assert b - a == Vector(2, 2)
    assert a * 3 == Vector(3, 6)
    assert 3 * a == Vector(3, 6)
    assert abs(b) == 5
    assert repr(a + b) == "Vector(4, 6)"
    assert a == Vector(1, 2), "Los operadores no deben modificar los originales"

    print("Todas las pruebas pasaron")
