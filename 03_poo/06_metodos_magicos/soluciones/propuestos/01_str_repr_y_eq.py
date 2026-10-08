"""
Solución - Ejercicio propuesto 01 - __str__, __repr__ y __eq__
"""

import math


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Punto({self.x}, {self.y})"

    def __eq__(self, otro):
        if not isinstance(otro, Punto):
            # NotImplemented le dice a Python "no sé comparar con esto";
            # Python intenta entonces la comparación desde el otro objeto.
            return NotImplemented
        return self.x == otro.x and self.y == otro.y

    def distancia_al_origen(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


# Respuesta a la pregunta:
# Sin __eq__, Python compara la identidad: si son el MISMO objeto en
# memoria. Dos objetos distintos con los mismos datos darían False.


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    p = Punto(3, 4)
    assert str(p) == "(3, 4)"
    assert repr(p) == "Punto(3, 4)"
    assert f"{p}" == "(3, 4)"
    assert repr([Punto(1, 2)]) == "[Punto(1, 2)]", "Las listas usan repr de sus elementos"

    assert Punto(1, 2) == Punto(1, 2)
    assert Punto(1, 2) != Punto(2, 1)
    assert (Punto(1, 2) == (1, 2)) is False
    assert p.distancia_al_origen() == 5

    print("Todas las pruebas pasaron")
