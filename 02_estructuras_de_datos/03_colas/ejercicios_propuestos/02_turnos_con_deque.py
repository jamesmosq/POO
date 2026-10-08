"""
Ejercicio propuesto 02 - Turnos con deque
Nivel: básico

Sacar el primer elemento de una lista con pop(0) es lento cuando la lista
es grande, porque Python debe correr todos los demás. Para colas se usa
collections.deque, que agrega y quita por los dos extremos rápidamente:
    from collections import deque
    fila = deque(["Ana", "Luis"])
    fila.append("Eva")       # al final
    fila.popleft()           # quita el primero -> "Ana"

Requisitos:
1. atender(fila, cantidad): atiende (quita del frente) hasta cantidad
   personas y retorna la lista de atendidos, en orden. Si la fila se
   vacía antes, atiende solo a los que había.
2. llegada_prioritaria(fila, persona): una persona con prioridad (por
   ejemplo, una mujer embarazada) pasa al FRENTE de la fila. Pista:
   appendleft.

Conceptos: collections.deque, popleft, appendleft.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
