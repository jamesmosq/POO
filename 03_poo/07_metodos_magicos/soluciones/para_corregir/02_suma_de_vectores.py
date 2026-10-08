"""
Solución - Ejercicio para corregir 02 - Suma de vectores

CORRECCIÓN 1 (dos vectores iguales no eran ==): sin __eq__, Python compara
si son el mismo objeto en memoria. Hay que definir qué significa que dos
vectores sean iguales.

CORRECCIÓN 2 (la suma modificaba a): __add__ cambiaba self y lo retornaba.
Un operador como + no debe modificar los operandos: igual que 2 + 3 no
cambia al 2, a + b debe crear un vector nuevo.
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y)  # CORRECCIÓN 2

    def __eq__(self, otro):  # CORRECCIÓN 1
        if not isinstance(otro, Vector):
            return NotImplemented
        return self.x == otro.x and self.y == otro.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


# ----------------------------------------------------------------------
# Pruebas
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
