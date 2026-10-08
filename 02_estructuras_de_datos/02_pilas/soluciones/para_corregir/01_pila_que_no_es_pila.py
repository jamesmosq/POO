"""
Solución - Ejercicio para corregir 01 - Una pila que no es pila

CORRECCIÓN 1: pop(0) saca el PRIMER elemento que entró; eso es una cola
(FIFO). En una pila sale el último: pop() sin argumento.

CORRECCIÓN 2: la cima de la pila es el último elemento, elementos[-1], no
el primero.

Nota: además de ser incorrecto, pop(0) es lento en listas grandes, porque
obliga a correr todos los demás elementos una posición.
"""

class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        return self.elementos.pop()  # CORRECCIÓN 1

    def cima(self):
        return self.elementos[-1]  # CORRECCIÓN 2


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    pila = Pila()
    for n in (1, 2, 3):
        pila.apilar(n)
    assert pila.cima() == 3, f"cima() retornó {pila.cima()}"
    assert pila.desapilar() == 3
    assert pila.desapilar() == 2
    assert pila.cima() == 1

    print("Todas las pruebas pasaron")
