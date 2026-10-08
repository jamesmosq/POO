"""
Ejercicio para corregir 01 - Sonidos de animales
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    Cada animal responde a hacer_sonido() a su manera, y la función coro()
    reúne los sonidos de una lista de animales.

        coro([Perro(), Gato()]) -> ["Guau", "Miau"]

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class Animal:
    def hacer_sonido(self):
        raise NotImplementedError("Cada animal debe implementar hacer_sonido()")


class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"


class Gato(Animal):
    def hacer_sonid(self):
        return "Miau"


def coro(animales):
    return [animal.hacer_sonido for animal in animales]


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert Gato().hacer_sonido() == "Miau"
    assert coro([Perro(), Gato()]) == ["Guau", "Miau"], coro([Perro(), Gato()])

    print("Todas las pruebas pasaron")
