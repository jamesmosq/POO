"""
Solución - Ejercicio propuesto 01 - Vehículos abstractos
"""

from abc import ABC, abstractmethod


class Vehiculo(ABC):
    def __init__(self, marca):
        self.marca = marca

    @abstractmethod
    def mover(self):
        pass

    def describir(self):
        return f"{self.marca}: {self.mover()}"


class Carro(Vehiculo):
    def mover(self):
        return "avanza por la carretera"


class Bicicleta(Vehiculo):
    def mover(self):
        return "avanza pedaleando"


class Lancha(Vehiculo):
    def mover(self):
        return "navega por el agua"


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    from abc import ABC

    try:
        Vehiculo("X")
        raise AssertionError("No se debe poder crear un Vehiculo directamente")
    except TypeError:
        pass

    assert issubclass(Vehiculo, ABC)
    assert Carro("Toyota").describir() == "Toyota: avanza por la carretera"
    assert Bicicleta("GW").describir() == "GW: avanza pedaleando"
    assert Lancha("Yamaha").describir() == "Yamaha: navega por el agua"

    print("Todas las pruebas pasaron")
