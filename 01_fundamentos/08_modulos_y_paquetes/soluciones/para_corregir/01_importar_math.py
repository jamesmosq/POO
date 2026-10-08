"""
Solución - Ejercicio para corregir 01 - Importar math

CORRECCIÓN 1 (ModuleNotFoundError: No module named 'Math'): los nombres de
los módulos distinguen mayúsculas. El módulo se llama math.

CORRECCIÓN 2 (AttributeError: module 'math' has no attribute 'PI'): la
constante se llama math.pi, en minúscula. Ante la duda, dir(math) lista
todo lo que tiene el módulo.
"""

import math  # CORRECCIÓN 1


def perimetro_circulo(radio):
    return round(2 * math.pi * radio, 2)  # CORRECCIÓN 2


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert perimetro_circulo(1) == 6.28
    assert perimetro_circulo(10) == 62.83

    print("Todas las pruebas pasaron")
