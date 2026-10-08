"""
Solución - Ejercicio para corregir 01 - Instrumentos

CORRECCIÓN 1 (NameError: name 'ABC' is not defined): ABC y abstractmethod
vienen del módulo abc y hay que importarlos.

CORRECCIÓN 2 (TypeError: Can't instantiate abstract class Piano): Piano
definía "toca" en lugar de "tocar". Como no implementaba el método
abstracto, Python no deja crear objetos de esa clase. Este es justamente
el beneficio de la abstracción: el error aparece al crear el objeto, no
más tarde.
"""

from abc import ABC, abstractmethod  # CORRECCIÓN 1


class Instrumento(ABC):
    @abstractmethod
    def tocar(self):
        pass


class Guitarra(Instrumento):
    def tocar(self):
        return "Rasgueo de guitarra"


class Piano(Instrumento):
    def tocar(self):  # CORRECCIÓN 2
        return "Notas de piano"


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert Guitarra().tocar() == "Rasgueo de guitarra"
    assert Piano().tocar() == "Notas de piano"

    print("Todas las pruebas pasaron")
