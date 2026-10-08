"""
Ejercicio para corregir 01 - Animal y perro
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    Un Perro es un Animal cuyo sonido siempre es "guau". Además del nombre,
    el perro guarda su raza.

        Perro("Toby", "labrador").hablar()  ->  "Toby dice guau"
        Perro("Toby", "labrador").ficha()   ->  "Toby es un labrador"

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class Animal:
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido

    def hablar(self):
        return f"{self.nombre} dice {self.sonido}"


class Perro(Animal)
    def __init__(self, nombre, raza):
        self.raza = raza

    def ficha(self):
        return f"{self.nombre} es un {self.raza}"


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    toby = Perro("Toby", "labrador")
    assert toby.hablar() == "Toby dice guau"
    assert toby.ficha() == "Toby es un labrador"
    assert isinstance(toby, Animal)

    print("Todas las pruebas pasaron")
