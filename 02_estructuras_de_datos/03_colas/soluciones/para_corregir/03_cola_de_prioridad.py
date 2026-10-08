"""
Solución - Ejercicio para corregir 03 - Cola de prioridad

CORRECCIÓN 1: con < el nuevo elemento se insertaba ANTES de los que tenían
su misma prioridad, así que entre iguales se atendía primero al último en
llegar. Con <= queda después de ellos.

CORRECCIÓN 2: la lista está ordenada de más urgente a menos urgente, así
que el más urgente está al principio: pop(0). Con pop() se atendía primero
al menos urgente.
"""

class ColaPrioridad:
    def __init__(self):
        self.elementos = []

    def encolar(self, elemento, prioridad):
        posicion = 0
        while posicion < len(self.elementos) and self.elementos[posicion][0] <= prioridad:  # CORRECCIÓN 1
            posicion += 1
        self.elementos.insert(posicion, (prioridad, elemento))

    def desencolar(self):
        prioridad, elemento = self.elementos.pop(0)  # CORRECCIÓN 2
        return elemento


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    cola = ColaPrioridad()
    cola.encolar("gripa", 3)
    cola.encolar("infarto", 1)
    cola.encolar("tos", 3)
    cola.encolar("fractura", 2)
    orden = [cola.desencolar() for _ in range(4)]
    assert orden == ["infarto", "fractura", "gripa", "tos"], orden

    print("Todas las pruebas pasaron")
