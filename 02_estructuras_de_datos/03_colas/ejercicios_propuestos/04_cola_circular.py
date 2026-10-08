"""
Ejercicio propuesto 04 - Cola circular
Nivel: intermedio

Una cola circular usa una lista de tamaño FIJO. En lugar de correr los
elementos, mueve dos índices (frente y final) que dan la vuelta al llegar
al final de la lista, gracias al operador %:
    siguiente = (indice + 1) % capacidad

Así se usa en buffers de teclado, audio o comunicaciones.

Completa la clase ColaCircular:
    encolar(elemento)  si está llena: raise OverflowError("La cola está llena")
    desencolar()       si está vacía: raise IndexError("La cola está vacía")
    esta_llena()
    esta_vacia()
    __len__()

Usa self.datos (lista de tamaño fijo), self.frente (índice del primero),
self.cantidad y self.capacidad. La posición donde se encola es
(self.frente + self.cantidad) % self.capacidad.

Conceptos: aritmética modular, estructuras de tamaño fijo.
"""


class ColaCircular:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.datos = [None] * capacidad
        self.frente = 0
        self.cantidad = 0

    def encolar(self, elemento):
        pass

    def desencolar(self):
        pass

    def esta_llena(self):
        pass

    def esta_vacia(self):
        pass

    def __len__(self):
        pass


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    cola = ColaCircular(3)
    assert cola.esta_vacia() is True
    cola.encolar("a")
    cola.encolar("b")
    cola.encolar("c")
    assert cola.esta_llena() is True
    try:
        cola.encolar("d")
        raise AssertionError("Debe lanzar OverflowError")
    except OverflowError:
        pass

    assert cola.desencolar() == "a"
    cola.encolar("d")  # da la vuelta: se guarda en la posición 0
    assert cola.datos[0] == "d", "El elemento debe reutilizar la posición liberada"
    assert [cola.desencolar() for _ in range(3)] == ["b", "c", "d"]
    assert len(cola) == 0

    try:
        cola.desencolar()
        raise AssertionError("Debe lanzar IndexError")
    except IndexError:
        pass

    print("Todas las pruebas pasaron")
