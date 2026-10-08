"""
Solución - Ejercicio para corregir 05 - Impresora y papa caliente

CORRECCIÓN 1: rotate con un número positivo gira hacia la DERECHA (el
último pasa al principio). Para que el primero pase al final se usa un
número negativo: rotate(-pases).

CORRECCIÓN 2: // redondea hacia abajo; 25 páginas a 10 por minuto daban 2
minutos y no 3. Para redondear hacia arriba se usa math.ceil.

CORRECCIÓN 3: cada trabajo empieza cuando termina el anterior, así que el
minuto final se va ACUMULANDO. Se necesita una variable "reloj" que sume
las duraciones.
"""

import math
from collections import deque


def papa_caliente(nombres, pases):
    circulo = deque(nombres)
    eliminados = []
    while len(circulo) > 1:
        circulo.rotate(-pases)  # CORRECCIÓN 1
        eliminados.append(circulo.popleft())
    return eliminados, circulo[0]


def imprimir_trabajos(trabajos, paginas_por_minuto):
    cola = deque(trabajos)
    resultado = []
    reloj = 0
    while cola:
        nombre, paginas = cola.popleft()
        duracion = math.ceil(paginas / paginas_por_minuto)  # CORRECCIÓN 2
        reloj += duracion  # CORRECCIÓN 3
        resultado.append((nombre, reloj))
    return resultado


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert papa_caliente(["Ana", "Luis", "Eva", "Pedro"], 2) == (["Eva", "Luis", "Pedro"], "Ana"), (
        papa_caliente(["Ana", "Luis", "Eva", "Pedro"], 2)
    )
    resultado = imprimir_trabajos([("tesis", 25), ("foto", 1)], 10)
    assert resultado == [("tesis", 3), ("foto", 4)], resultado
    assert imprimir_trabajos([("a", 10), ("b", 10)], 10) == [("a", 1), ("b", 2)]

    print("Todas las pruebas pasaron")
