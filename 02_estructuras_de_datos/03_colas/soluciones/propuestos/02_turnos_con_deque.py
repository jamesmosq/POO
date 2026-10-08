"""
Solución - Ejercicio propuesto 02 - Turnos con deque
"""

def atender(fila, cantidad):
    atendidos = []
    while fila and len(atendidos) < cantidad:
        atendidos.append(fila.popleft())
    return atendidos


def llegada_prioritaria(fila, persona):
    fila.appendleft(persona)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    from collections import deque

    fila = deque(["Ana", "Luis", "Eva", "Pedro"])
    assert atender(fila, 2) == ["Ana", "Luis"]
    assert list(fila) == ["Eva", "Pedro"]

    llegada_prioritaria(fila, "Marta")
    assert list(fila) == ["Marta", "Eva", "Pedro"]

    assert atender(fila, 10) == ["Marta", "Eva", "Pedro"]
    assert len(fila) == 0
    assert atender(fila, 1) == []

    print("Todas las pruebas pasaron")
