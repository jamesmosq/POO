"""
Solución - Ejercicio propuesto 01 - Cola básica
"""

class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, elemento):
        self.elementos.append(elemento)

    def desencolar(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self.elementos.pop(0)  # sale el primero que entró

    def frente(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self.elementos[0]

    def esta_vacia(self):
        return len(self.elementos) == 0

    def __len__(self):
        return len(self.elementos)


# ----------------------------------------------------------------------
# Pruebas
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
