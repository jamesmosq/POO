"""
Ejercicio para corregir 03 - Validar desde el constructor
Nivel: intermedio
Errores a encontrar: 2

Qué debería hacer el programa:
    - Persona(nombre, edad): la edad se valida con una propiedad (entre 0
      y 120). La validación también debe aplicarse al crear el objeto.
    - Estudiante hereda de Persona y su método ficha() usa la edad.

        Persona("Ana", 150)              -> ValueError
        Estudiante("Luis", 20).ficha()   -> "Luis (20 años)"

Pista: busca en internet "name mangling Python" si un atributo con doble
guion bajo "desaparece" en la clase hija.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad

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
        return f"{self.nombre} ({self.__edad} años)"


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert Estudiante("Luis", 20).ficha() == "Luis (20 años)"

    try:
        Persona("Ana", 150)
        raise AssertionError("El constructor debe validar la edad")
    except ValueError:
        pass

    print("Todas las pruebas pasaron")
