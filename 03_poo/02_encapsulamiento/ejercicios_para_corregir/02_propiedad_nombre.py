"""
Ejercicio para corregir 02 - Propiedad nombre
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    La clase Mascota tiene una propiedad nombre que se puede leer y
    cambiar. El setter rechaza nombres vacíos con ValueError.

        m = Mascota("Toby")
        m.nombre          -> "Toby"
        m.nombre = "Max"
        m.nombre          -> "Max"

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class Mascota:
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self.nombre

    @nombre.setter
    def cambiar_nombre(self, valor):
        if not valor:
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    m = Mascota("Toby")
    assert m.nombre == "Toby"
    m.nombre = "Max"
    assert m.nombre == "Max"
    try:
        m.nombre = ""
        raise AssertionError("Debe lanzar ValueError")
    except ValueError:
        pass

    print("Todas las pruebas pasaron")
