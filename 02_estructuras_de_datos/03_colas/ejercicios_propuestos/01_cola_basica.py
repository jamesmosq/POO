"""
Ejercicio propuesto 01 - Cola básica
Nivel: básico

Una cola (queue) funciona como la fila de un banco: el primero que llega
es el primero en ser atendido. Esto se llama FIFO (First In, First Out).

Completa los métodos de la clase Cola. Guarda los elementos en
self.elementos: se encola al final y se desencola desde el principio.

    encolar(elemento)  agrega al final
    desencolar()       quita y retorna el primero
                       si está vacía: raise IndexError("La cola está vacía")
    frente()           retorna el primero SIN quitarlo
                       si está vacía: raise IndexError("La cola está vacía")
    esta_vacia()       True si no tiene elementos
    __len__()          cantidad de elementos

Conceptos: cola, FIFO, diferencia con la pila.
"""


class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, elemento):
        pass

    def desencolar(self):
        pass

    def frente(self):
        pass

    def esta_vacia(self):
        pass

    def __len__(self):
        pass


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    cola = Cola()
    assert cola.esta_vacia() is True

    for persona in ("Ana", "Luis", "Eva"):
        cola.encolar(persona)
    assert len(cola) == 3
    assert cola.frente() == "Ana"
    assert len(cola) == 3, "frente() no debe quitar el elemento"

    assert cola.desencolar() == "Ana"
    assert cola.desencolar() == "Luis"
    cola.encolar("Pedro")
    assert cola.desencolar() == "Eva"
    assert cola.desencolar() == "Pedro"
    assert cola.esta_vacia() is True

    for metodo in (cola.desencolar, cola.frente):
        try:
            metodo()
            raise AssertionError(f"{metodo.__name__}() en una cola vacía debe lanzar IndexError")
        except IndexError as error:
            assert str(error) == "La cola está vacía"

    print("Todas las pruebas pasaron")
