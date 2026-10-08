"""
Solución - Ejercicio para corregir 03 - Validar desde el constructor

CORRECCIÓN 1 (AttributeError: 'Estudiante' object has no attribute
'_Estudiante__edad'): Python cambia el nombre de los atributos con doble
guion bajo agregando el nombre de la clase (name mangling). En Persona,
self.__edad es en realidad self._Persona__edad, y desde Estudiante no se
encuentra. La clase hija debe usar la propiedad pública self.edad.

CORRECCIÓN 2 (la edad inválida se aceptaba): el constructor asignaba
directamente el atributo privado y se saltaba la validación del setter.
Asignando con self.edad = edad, también se valida al crear el objeto.
"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad  # CORRECCIÓN 2

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        if not 0 <= valor <= 120:
            raise ValueError("Edad fuera de rango")
        self.__edad = valor


class Estudiante(Persona):
    def ficha(self):
        return f"{self.nombre} ({self.edad} años)"  # CORRECCIÓN 1


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert Estudiante("Luis", 20).ficha() == "Luis (20 años)"

    try:
        Persona("Ana", 150)
        raise AssertionError("El constructor debe validar la edad")
    except ValueError:
        pass

    print("Todas las pruebas pasaron")
