"""
Solución - Ejercicio para corregir 02 - Promedio de una lista

CORRECCIÓN 1: total = 0 estaba dentro del ciclo, así que se reiniciaba en
cada vuelta. El acumulador se inicializa una sola vez, antes del for.

CORRECCIÓN 2: el return estaba dentro del ciclo, por eso la función
terminaba en la primera vuelta. El resultado se retorna cuando el ciclo
ya terminó.
"""

def promedio(numeros):
    total = 0  # CORRECCIÓN 1
    for n in numeros:
        total += n
    return total / len(numeros)  # CORRECCIÓN 2


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert promedio([2, 4, 6]) == 4.0, f"promedio([2, 4, 6]) retornó {promedio([2, 4, 6])}"
    assert promedio([10]) == 10.0
    assert promedio([1, 2, 3, 4]) == 2.5

    print("Todas las pruebas pasaron")
