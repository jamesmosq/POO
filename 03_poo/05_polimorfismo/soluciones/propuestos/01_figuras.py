"""
Solución - Ejercicio propuesto 01 - Figuras
"""

import math


class Figura:
    def area(self):
        raise NotImplementedError("Cada figura debe implementar area()")


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2


class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura / 2


def area_total(figuras):
    # No importa de qué clase es cada figura: todas saben calcular su área.
    return sum(figura.area() for figura in figuras)


def la_mas_grande(figuras):
    return max(figuras, key=lambda figura: figura.area())


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    figuras = [Rectangulo(4, 5), Circulo(1), Triangulo(6, 2)]
    assert round(area_total(figuras), 2) == 29.14
    assert isinstance(la_mas_grande(figuras), Rectangulo)

    try:
        Figura().area()
        raise AssertionError("Figura.area() debe lanzar NotImplementedError")
    except NotImplementedError:
        pass

    fuente = open(__file__, encoding="utf-8").read().split("# Pruebas")[0]
    assert "isinstance(" not in fuente and "type(" not in fuente, "Usa polimorfismo, no isinstance ni type"

    print("Todas las pruebas pasaron")
