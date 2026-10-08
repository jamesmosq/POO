"""
Solución - Ejercicio para corregir 01 - Animal y perro

CORRECCIÓN 1 (SyntaxError): faltaban los dos puntos al final de la línea
    class Perro(Animal)
Toda definición de clase, función, if, for o while termina en ':'.

CORRECCIÓN 2 (AttributeError: 'Perro' object has no attribute 'nombre'):
el __init__ de Perro reemplaza al de Animal. Si no se llama a
super().__init__(), los atributos nombre y sonido nunca se crean. Además,
el sonido de un perro siempre es "guau", así que se pasa fijo.
"""


class Animal:
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido

    def hablar(self):
        return f"{self.nombre} dice {self.sonido}"


class Perro(Animal):  # CORRECCIÓN 1
    def __init__(self, nombre, raza):
        super().__init__(nombre, "guau")  # CORRECCIÓN 2
        self.raza = raza

    def ficha(self):
        return f"{self.nombre} es un {self.raza}"


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    toby = Perro("Toby", "labrador")
    assert toby.hablar() == "Toby dice guau"
    assert toby.ficha() == "Toby es un labrador"
    assert isinstance(toby, Animal)

    print("Todas las pruebas pasaron")
