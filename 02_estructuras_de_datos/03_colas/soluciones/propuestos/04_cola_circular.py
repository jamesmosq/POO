"""
Solución - Ejercicio propuesto 04 - Cola circular
"""

class ColaCircular:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.datos = [None] * capacidad
        self.frente = 0
        self.cantidad = 0

    def encolar(self, elemento):
        if self.esta_llena():
            raise OverflowError("La cola está llena")
        posicion = (self.frente + self.cantidad) % self.capacidad
        self.datos[posicion] = elemento
        self.cantidad += 1

    def desencolar(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        elemento = self.datos[self.frente]
        self.datos[self.frente] = None
        self.frente = (self.frente + 1) % self.capacidad
        self.cantidad -= 1
        return elemento

    def esta_llena(self):
        return self.cantidad == self.capacidad

    def esta_vacia(self):
        return self.cantidad == 0

    def __len__(self):
        return self.cantidad


# ----------------------------------------------------------------------
# Pruebas
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
