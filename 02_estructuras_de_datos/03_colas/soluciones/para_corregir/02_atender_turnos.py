"""
Solución - Ejercicio para corregir 02 - Atender turnos

CORRECCIÓN 1: fila.popleft sin paréntesis agrega el método a la lista, no
la persona, y además no saca a nadie de la fila.

CORRECCIÓN 2 (IndexError: pop from an empty deque): si se piden más
personas de las que hay, popleft() falla al vaciarse la fila. Hay que
detenerse cuando la fila esté vacía.
"""

from collections import deque


def atender(fila, cantidad):
    atendidos = []
    for _ in range(cantidad):
        if not fila:  # CORRECCIÓN 2
            break
        atendidos.append(fila.popleft())  # CORRECCIÓN 1
    return atendidos


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    fila = deque(["Ana", "Luis", "Eva"])
    assert atender(fila, 2) == ["Ana", "Luis"], atender(deque(["Ana", "Luis", "Eva"]), 2)
    assert atender(fila, 5) == ["Eva"]
    assert atender(fila, 1) == []

    print("Todas las pruebas pasaron")
