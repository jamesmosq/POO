"""
Solución - Ejercicio para corregir 04 - Lista de notas protegida

CORRECCIÓN 1: una nota no puede ser al mismo tiempo menor que 0 Y mayor
que 5, así que la condición nunca se cumplía. Fuera del rango significa
menor que 0 O mayor que 5.

CORRECCIÓN 2: retornar self._notas entrega la lista interna; quien la
recibe puede agregarle cualquier cosa sin validación. Se retorna una
tupla, que no se puede modificar.

CORRECCIÓN 3: la propiedad promedio calculaba el valor pero no lo
retornaba.
"""

class Boletin:
    def __init__(self):
        self._notas = []

    def agregar_nota(self, nota):
        if nota < 0 or nota > 5:  # CORRECCIÓN 1
            raise ValueError("La nota debe estar entre 0 y 5")
        self._notas.append(nota)

    @property
    def notas(self):
        return tuple(self._notas)  # CORRECCIÓN 2

    @property
    def promedio(self):
        if not self._notas:
            return 0
        return sum(self._notas) / len(self._notas)  # CORRECCIÓN 3


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    b = Boletin()
    b.agregar_nota(4.0)
    b.agregar_nota(3.0)

    try:
        b.agregar_nota(7)
        raise AssertionError("Una nota de 7 debe lanzar ValueError")
    except ValueError:
        pass

    notas = b.notas
    try:
        notas.append(99)
    except AttributeError:
        pass
    assert b.notas == (4.0, 3.0), f"Las notas cambiaron desde afuera: {b.notas}"
    assert b.promedio == 3.5, f"promedio vale {b.promedio}"

    print("Todas las pruebas pasaron")
