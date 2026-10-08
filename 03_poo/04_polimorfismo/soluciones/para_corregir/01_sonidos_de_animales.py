"""
Solución - Ejercicio para corregir 01 - Sonidos de animales

CORRECCIÓN 1 (NotImplementedError): Gato definía "hacer_sonid", que es un
método nuevo con otro nombre. Como no sobrescribía hacer_sonido, se usaba
el de Animal, que lanza el error.

CORRECCIÓN 2 (la lista tenía métodos en lugar de sonidos): faltaban los
paréntesis para llamar a hacer_sonido().
"""

class Animal:
    def hacer_sonido(self):
        raise NotImplementedError("Cada animal debe implementar hacer_sonido()")


class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"


class Gato(Animal):
    def hacer_sonido(self):  # CORRECCIÓN 1
        return "Miau"


def coro(animales):
    return [animal.hacer_sonido() for animal in animales]  # CORRECCIÓN 2


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert Gato().hacer_sonido() == "Miau"
    assert coro([Perro(), Gato()]) == ["Guau", "Miau"], coro([Perro(), Gato()])

    print("Todas las pruebas pasaron")
