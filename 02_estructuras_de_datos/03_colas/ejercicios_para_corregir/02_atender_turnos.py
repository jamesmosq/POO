"""
Ejercicio para corregir 02 - Atender turnos
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    atender(fila, cantidad) quita del frente de la fila (una deque) hasta
    cantidad personas y retorna la lista de atendidos. Si la fila se vacía
    antes, atiende solo a los que había.

        fila = deque(["Ana", "Luis", "Eva"])
        atender(fila, 2)   -> ["Ana", "Luis"]
        atender(fila, 5)   -> ["Eva"]

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""
from collections import deque


def atender(fila, cantidad):
    atendidos = []
    for _ in range(cantidad):
        atendidos.append(fila.popleft)
    return atendidos


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    fila = deque(["Ana", "Luis", "Eva"])
    assert atender(fila, 2) == ["Ana", "Luis"], atender(deque(["Ana", "Luis", "Eva"]), 2)
    assert atender(fila, 5) == ["Eva"]
    assert atender(fila, 1) == []

    print("Todas las pruebas pasaron")
