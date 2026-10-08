"""
Ejercicio propuesto 01 - Pila básica
Nivel: básico

Una pila (stack) funciona como una torre de platos: el último que se pone
es el primero que se saca. Esto se llama LIFO (Last In, First Out).

Completa los métodos de la clase Pila. Guarda los elementos en la lista
self.elementos; el final de la lista es la cima de la pila.

    apilar(elemento)  agrega en la cima
    desapilar()       quita y retorna el de la cima
                      si está vacía: raise IndexError("La pila está vacía")
    cima()            retorna el de la cima SIN quitarlo
                      si está vacía: raise IndexError("La pila está vacía")
    esta_vacia()      True si no tiene elementos
    __len__()         cantidad de elementos (permite usar len(pila))

La clase ya está escrita; solo completa el cuerpo de cada método. Las
clases se estudian a fondo en 03_poo.

Conceptos: pila, LIFO, append y pop.
"""


class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, elemento):
        pass

    def desapilar(self):
        pass

    def cima(self):
        pass

    def esta_vacia(self):
        pass

    def __len__(self):
        pass


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
