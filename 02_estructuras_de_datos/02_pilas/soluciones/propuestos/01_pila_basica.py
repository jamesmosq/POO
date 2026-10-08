"""
Solución - Ejercicio propuesto 01 - Pila básica
"""

class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.elementos.pop()

    def cima(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.elementos[-1]

    def esta_vacia(self):
        return len(self.elementos) == 0

    def __len__(self):
        return len(self.elementos)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    pila = Pila()
    assert pila.esta_vacia() is True
    assert len(pila) == 0

    pila.apilar(1)
    pila.apilar(2)
    pila.apilar(3)
    assert len(pila) == 3
    assert pila.cima() == 3
    assert len(pila) == 3, "cima() no debe quitar el elemento"

    assert pila.desapilar() == 3
    assert pila.desapilar() == 2
    assert pila.desapilar() == 1
    assert pila.esta_vacia() is True

    for metodo in (pila.desapilar, pila.cima):
        try:
            metodo()
            raise AssertionError(f"{metodo.__name__}() en una pila vacía debe lanzar IndexError")
        except IndexError as error:
            assert str(error) == "La pila está vacía"

    print("Todas las pruebas pasaron")
