"""
Solución - Ejercicio para corregir 01 - Una cola que no es cola

CORRECCIÓN 1: pop() saca el ÚLTIMO elemento; eso es una pila (LIFO). En
una cola sale el primero que entró: pop(0).

CORRECCIÓN 2: el frente de la cola es el primer elemento, elementos[0].
"""

class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, elemento):
        self.elementos.append(elemento)

    def desencolar(self):
        return self.elementos.pop(0)  # CORRECCIÓN 1

    def frente(self):
        return self.elementos[0]  # CORRECCIÓN 2


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    cola = Cola()
    for persona in ("Ana", "Luis", "Eva"):
        cola.encolar(persona)
    assert cola.frente() == "Ana", f"frente() retornó {cola.frente()}"
    assert cola.desencolar() == "Ana"
    assert cola.desencolar() == "Luis"
    assert cola.frente() == "Eva"

    print("Todas las pruebas pasaron")
