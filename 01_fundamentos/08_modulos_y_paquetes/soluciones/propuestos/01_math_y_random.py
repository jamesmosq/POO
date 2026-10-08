"""
Solución - Ejercicio propuesto 01 - Módulos math y random
"""

import math
import random


def area_circulo(radio):
    return round(math.pi * radio ** 2, 2)


def hipotenusa(a, b):
    return math.sqrt(a ** 2 + b ** 2)  # o math.hypot(a, b)


def lanzar_dados(cantidad, semilla):
    generador = random.Random(semilla)
    return [generador.randint(1, 6) for _ in range(cantidad)]


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert area_circulo(1) == 3.14
    assert area_circulo(2.5) == 19.63
    assert hipotenusa(3, 4) == 5

    tirada = lanzar_dados(100, semilla=42)
    assert len(tirada) == 100
    assert all(1 <= d <= 6 for d in tirada), "Los dados van de 1 a 6"
    assert set(tirada) == {1, 2, 3, 4, 5, 6}, "En 100 lanzamientos deberían salir todos los números"
    assert lanzar_dados(10, semilla=7) == lanzar_dados(10, semilla=7), "La misma semilla da los mismos dados"

    print("Todas las pruebas pasaron")
