"""
Ejercicio para corregir 01 - Una pila que no es pila
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    La clase Pila debe comportarse como LIFO: el último elemento apilado es
    el primero en salir y el que se ve en la cima.

        apilar(1), apilar(2), apilar(3)
        cima()       -> 3
        desapilar()  -> 3

Ojo: el programa no lanza errores. Funciona, pero como otra estructura.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        return self.elementos.pop(0)

    def cima(self):
        return self.elementos[0]


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    pila = Pila()
    for n in (1, 2, 3):
        pila.apilar(n)
    assert pila.cima() == 3, f"cima() retornó {pila.cima()}"
    assert pila.desapilar() == 3
    assert pila.desapilar() == 2
    assert pila.cima() == 1

    print("Todas las pruebas pasaron")
