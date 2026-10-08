"""
Solución - Ejercicio para corregir 02 - Propiedad nombre

CORRECCIÓN 1 (RecursionError): el getter retornaba self.nombre, que vuelve
a llamar al getter, y así infinitamente. El valor real está en
self._nombre.

CORRECCIÓN 2 (AttributeError: property 'nombre' of 'Mascota' object has no
setter): el setter debe llamarse IGUAL que la propiedad. Con otro nombre,
@nombre.setter crea una propiedad nueva llamada cambiar_nombre y nombre se
queda sin setter.
"""

class Mascota:
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre  # CORRECCIÓN 1

    @nombre.setter
    def nombre(self, valor):  # CORRECCIÓN 2
        if not valor:
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor


# ----------------------------------------------------------------------
# Pruebas
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
