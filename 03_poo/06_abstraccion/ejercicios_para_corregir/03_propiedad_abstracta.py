"""
Ejercicio para corregir 03 - Propiedad abstracta
Nivel: intermedio
Errores a encontrar: 2

Qué debería hacer el programa:
    Figura declara la propiedad abstracta nombre. Cada hija la implementa
    como PROPIEDAD, y resumen() la usa como atributo (sin paréntesis).

        Cuadrado(3).resumen() -> "Cuadrado de área 9"

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""
from abc import ABC, abstractmethod


class Figura(ABC):
    @abstractmethod
    @property
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

    def nombre(self):
        return "Cuadrado"

    def area(self):
        return self.lado ** 2


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert Cuadrado(3).resumen() == "Cuadrado de área 9", Cuadrado(3).resumen()

    print("Todas las pruebas pasaron")
