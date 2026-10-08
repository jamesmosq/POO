"""
Solución - Ejercicio para corregir 02 - Empleados abstractos

CORRECCIÓN 1 (Empleado se podía instanciar): @abstractmethod solo tiene
efecto si la clase hereda de ABC. Sin eso, es un decorador que no hace
nada.

CORRECCIÓN 2 (TypeError: unsupported operand type(s) for +: 'NoneType' and
'str'): el método abstracto del padre no retorna nada (None). La hija debe
implementar rol() por completo, no extender el del padre.
"""

from abc import ABC, abstractmethod


class Empleado(ABC):  # CORRECCIÓN 1
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def rol(self):
        pass

    def presentacion(self):
        return f"{self.nombre} - {self.rol()}"


class Desarrollador(Empleado):
    def rol(self):
        return "Desarrollador"  # CORRECCIÓN 2


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    try:
        Empleado("X")
        raise AssertionError("Empleado debe ser abstracta: no se debe poder instanciar")
    except TypeError:
        pass

    assert Desarrollador("Ana").presentacion() == "Ana - Desarrollador"

    print("Todas las pruebas pasaron")
