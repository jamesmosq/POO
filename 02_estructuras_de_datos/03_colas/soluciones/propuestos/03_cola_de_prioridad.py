"""
Solución - Ejercicio propuesto 03 - Cola de prioridad
"""

class ColaPrioridad:
    def __init__(self):
        self.elementos = []

    def encolar(self, elemento, prioridad):
        posicion = 0
        # Con <= el nuevo queda después de los que tienen su misma prioridad.
        while posicion < len(self.elementos) and self.elementos[posicion][0] <= prioridad:
            posicion += 1
        self.elementos.insert(posicion, (prioridad, elemento))

    def desencolar(self):
        if not self.elementos:
            raise IndexError("La cola está vacía")
        _, elemento = self.elementos.pop(0)
        return elemento

    def __len__(self):
        return len(self.elementos)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    urgencias = ColaPrioridad()
    urgencias.encolar("dolor de cabeza", 3)
    urgencias.encolar("fractura", 2)
    urgencias.encolar("infarto", 1)
    urgencias.encolar("gripa", 3)
    urgencias.encolar("quemadura", 2)
    assert len(urgencias) == 5

    orden = [urgencias.desencolar() for _ in range(5)]
    assert orden == ["infarto", "fractura", "quemadura", "dolor de cabeza", "gripa"], orden

    try:
        urgencias.desencolar()
        raise AssertionError("Debe lanzar IndexError")
    except IndexError as error:
        assert str(error) == "La cola está vacía"

    print("Todas las pruebas pasaron")
