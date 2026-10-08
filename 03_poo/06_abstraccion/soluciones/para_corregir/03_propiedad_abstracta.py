"""
Solución - Ejercicio para corregir 03 - Propiedad abstracta

CORRECCIÓN 1 (AttributeError: attribute '__isabstractmethod__' of
'property' objects is not writable): el orden de los decoradores importa.
Se aplican de abajo hacia arriba, y @abstractmethod debe recibir la función,
no la propiedad. Lo correcto es @property arriba y @abstractmethod abajo.

CORRECCIÓN 2 (el resumen mostraba "<bound method ...>"): Cuadrado
implementaba nombre como método normal. resumen() lo usa sin paréntesis,
así que debe ser una propiedad también en la hija.
"""

from abc import ABC, abstractmethod


class Figura(ABC):
    @property  # CORRECCIÓN 1
    @abstractmethod
    def nombre(self):
        pass

    @abstractmethod
    def area(self):
        pass

    def resumen(self):
        return f"{self.nombre} de área {self.area()}"


class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    @property  # CORRECCIÓN 2
    def nombre(self):
        return "Cuadrado"

    def area(self):
        return self.lado ** 2


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert Cuadrado(3).resumen() == "Cuadrado de área 9", Cuadrado(3).resumen()

    print("Todas las pruebas pasaron")
