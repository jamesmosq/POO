"""
Ejercicio para corregir 01 - Una cola que no es cola
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    La clase Cola debe ser FIFO: el primero en entrar es el primero en
    salir y el que está al frente.

        encolar("Ana"), encolar("Luis"), encolar("Eva")
        frente()      -> "Ana"
        desencolar()  -> "Ana"

Ojo: el programa no lanza errores. Funciona, pero como otra estructura.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, elemento):
        self.elementos.append(elemento)

    def desencolar(self):
        return self.elementos.pop()

    def frente(self):
        return self.elementos[-1]


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    cola = Cola()
    for persona in ("Ana", "Luis", "Eva"):
        cola.encolar(persona)
    assert cola.frente() == "Ana", f"frente() retornó {cola.frente()}"
    assert cola.desencolar() == "Ana"
    assert cola.desencolar() == "Luis"
    assert cola.frente() == "Eva"

    print("Todas las pruebas pasaron")
