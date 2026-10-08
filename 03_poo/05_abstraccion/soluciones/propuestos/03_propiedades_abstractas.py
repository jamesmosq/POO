"""
Solución - Ejercicio propuesto 03 - Propiedades abstractas
"""

import math
from abc import ABC, abstractmethod


class Figura(ABC):
    @property
    @abstractmethod
    def nombre(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    def resumen(self):
        return f"{self.nombre}: área {self.area():.2f}, perímetro {self.perimetro():.2f}"


class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    @property
    def nombre(self):
        return "Cuadrado"

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    @property
    def nombre(self):
        return "Círculo"

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert Cuadrado(2).resumen() == "Cuadrado: área 4.00, perímetro 8.00"
    assert Circulo(1).resumen() == "Círculo: área 3.14, perímetro 6.28"
    assert isinstance(Cuadrado.nombre, property), "nombre debe ser una propiedad"

    class Incompleta(Figura):
        @property
        def nombre(self):
            return "Incompleta"

        def area(self):
            return 0

    try:
        Incompleta()
        raise AssertionError("Una figura sin perimetro() no se debe poder crear")
    except TypeError:
        pass

    print("Todas las pruebas pasaron")
