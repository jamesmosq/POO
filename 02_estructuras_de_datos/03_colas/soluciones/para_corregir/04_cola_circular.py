"""
Solución - Ejercicio para corregir 04 - Cola circular

CORRECCIÓN 1 (IndexError al encolar en una cola llena): la cola está llena
cuando cantidad es IGUAL a la capacidad. Con > nunca se detectaba.

CORRECCIÓN 2 (cantidad no bajaba): desencolar no restaba 1 a cantidad, así
que la cola creía tener más elementos de los reales.

CORRECCIÓN 3 (IndexError al dar la vuelta): la posición donde se encola
debe dar la vuelta con % capacidad; si no, se sale del final de la lista.
"""

class ColaCircular:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.datos = [None] * capacidad
        self.frente = 0
        self.cantidad = 0

    def esta_llena(self):
        return self.cantidad == self.capacidad  # CORRECCIÓN 1

    def encolar(self, elemento):
        if self.esta_llena():
            raise OverflowError("La cola está llena")
        posicion = (self.frente + self.cantidad) % self.capacidad  # CORRECCIÓN 3
        self.datos[posicion] = elemento
        self.cantidad += 1

    def desencolar(self):
        if self.cantidad == 0:
            raise IndexError("La cola está vacía")
        elemento = self.datos[self.frente]
        self.frente = (self.frente + 1) % self.capacidad
        self.cantidad -= 1  # CORRECCIÓN 2
        return elemento


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    cola = ColaCircular(3)
    for letra in "abc":
        cola.encolar(letra)
    try:
        cola.encolar("d")
        raise AssertionError("La cola está llena: debe lanzar OverflowError")
    except OverflowError:
        pass

    assert cola.desencolar() == "a"
    assert cola.cantidad == 2, f"Después de desencolar, cantidad vale {cola.cantidad}"
    cola.encolar("d")
    assert cola.datos[0] == "d"
    assert [cola.desencolar() for _ in range(3)] == ["b", "c", "d"]

    print("Todas las pruebas pasaron")
