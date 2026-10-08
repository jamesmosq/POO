"""
Ejercicio propuesto 03 - Cola de prioridad
Nivel: intermedio

En urgencias no se atiende por orden de llegada, sino por gravedad. Una
cola de prioridad saca primero el elemento con MAYOR prioridad. Aquí el
número 1 es la prioridad más alta (más urgente).

Completa la clase ColaPrioridad. Guarda tuplas (prioridad, elemento) en
self.elementos, siempre ordenadas.

    encolar(elemento, prioridad)  inserta en la posición que corresponde.
                                  Si hay varios con la misma prioridad,
                                  se respeta el orden de llegada (el nuevo
                                  queda DESPUÉS de los que ya estaban).
    desencolar()                  quita y retorna el ELEMENTO más urgente.
                                  Si está vacía: raise IndexError("La cola está vacía")
    __len__()                     cantidad de elementos

Conceptos: cola de prioridad, inserción ordenada, estabilidad.
"""


class ColaPrioridad:
    def __init__(self):
        self.elementos = []

    def encolar(self, elemento, prioridad):
        pass

    def desencolar(self):
        pass

    def __len__(self):
        pass


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
