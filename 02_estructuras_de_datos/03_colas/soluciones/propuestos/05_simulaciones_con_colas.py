"""
Solución - Ejercicio propuesto 05 - Simulaciones con colas
"""

import math
from collections import deque


def papa_caliente(nombres, pases):
    circulo = deque(nombres)
    eliminados = []
    while len(circulo) > 1:
        circulo.rotate(-pases)  # negativo: el primero pasa al final
        eliminados.append(circulo.popleft())
    return eliminados, circulo[0]


def imprimir_trabajos(trabajos, paginas_por_minuto):
    cola = deque(trabajos)
    reloj = 0
    resultado = []
    while cola:
        nombre, paginas = cola.popleft()
        reloj += math.ceil(paginas / paginas_por_minuto)
        resultado.append((nombre, reloj))
    return resultado


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert papa_caliente(["Ana", "Luis", "Eva", "Pedro"], 2) == (["Eva", "Luis", "Pedro"], "Ana")
    assert papa_caliente(["Solo"], 5) == ([], "Solo")
    eliminados, ganador = papa_caliente(["A", "B", "C", "D", "E", "F", "G"], 3)
    assert ganador == "B" and eliminados == ["D", "A", "F", "E", "G", "C"], (eliminados, ganador)

    assert imprimir_trabajos([("tesis", 25), ("foto", 1)], 10) == [("tesis", 3), ("foto", 4)]
    assert imprimir_trabajos([("a", 10), ("b", 10), ("c", 5)], 10) == [("a", 1), ("b", 2), ("c", 3)]
    assert imprimir_trabajos([], 10) == []

    print("Todas las pruebas pasaron")
