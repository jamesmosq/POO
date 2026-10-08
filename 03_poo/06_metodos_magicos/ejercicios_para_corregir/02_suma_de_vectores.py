"""
Ejercicio para corregir 02 - Suma de vectores
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    a = Vector(1, 2); b = Vector(3, 4)
    a + b         -> Vector(4, 6), un objeto NUEVO
    a             -> sigue siendo Vector(1, 2)
    a == Vector(1, 2) -> True

Ojo: el programa no lanza errores.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        self.x += otro.x
        self.y += otro.y
        return self

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert Vector(1, 2) == Vector(1, 2), "Dos vectores con las mismas coordenadas son iguales"

    a = Vector(1, 2)
    b = Vector(3, 4)
    c = a + b
    assert c == Vector(4, 6)
    assert a == Vector(1, 2), f"La suma modificó a: {a}"
    assert c is not a, "La suma debe crear un vector nuevo"

    print("Todas las pruebas pasaron")
