"""
Ejercicio para corregir 03 - Cola de prioridad
Nivel: intermedio
Errores a encontrar: 2

Qué debería hacer el programa:
    La cola guarda tuplas (prioridad, elemento) ordenadas; el número 1 es
    lo más urgente. Con la misma prioridad se respeta el orden de llegada.

        encolar("gripa", 3), encolar("infarto", 1), encolar("tos", 3)
        desencolar() -> "infarto"
        desencolar() -> "gripa"   (llegó antes que "tos")
        desencolar() -> "tos"

Ojo: el programa no lanza errores, pero atiende en otro orden.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class ColaPrioridad:
    def __init__(self):
        self.elementos = []

    def encolar(self, elemento, prioridad):
        posicion = 0
        while posicion < len(self.elementos) and self.elementos[posicion][0] < prioridad:
            posicion += 1
        self.elementos.insert(posicion, (prioridad, elemento))

    def desencolar(self):
        prioridad, elemento = self.elementos.pop()
        return elemento


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
