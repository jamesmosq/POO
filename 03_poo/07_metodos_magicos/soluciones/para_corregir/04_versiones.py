"""
Solución - Ejercicio para corregir 04 - Versiones

CORRECCIÓN 1 (TypeError: unhashable type: 'Version'): al definir __eq__,
Python elimina el __hash__ por defecto, y los objetos ya no pueden ir en un
set. Hay que definir __hash__ coherente con __eq__.

CORRECCIÓN 2 (1.10 salía menor que 1.9): comparar los textos los ordena
carácter por carácter, y "1" < "9". Se comparan las partes como números,
en una tupla de enteros.

CORRECCIÓN 3 (AttributeError: 'str' object has no attribute 'texto'):
__eq__ suponía que el otro objeto era una Version. Si no lo es, debe
retornar NotImplemented.
"""

from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, texto):
        self.texto = texto
        self.partes = tuple(int(p) for p in texto.split("."))  # CORRECCIÓN 2

    def __eq__(self, otra):
        if not isinstance(otra, Version):  # CORRECCIÓN 3
            return NotImplemented
        return self.partes == otra.partes

    def __lt__(self, otra):
        return self.partes < otra.partes  # CORRECCIÓN 2

    def __hash__(self):  # CORRECCIÓN 1
        return hash(self.partes)

    def __str__(self):
        return self.texto


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    unicas = {Version("1.0.0"), Version("1.0.0"), Version("2.0.0")}
    assert len(unicas) == 2

    assert Version("1.10.0") > Version("1.9.0"), "1.10 es más nueva que 1.9"
    ordenadas = sorted([Version("1.10.0"), Version("1.2.0"), Version("1.9.3")])
    assert [str(v) for v in ordenadas] == ["1.2.0", "1.9.3", "1.10.0"]

    assert (Version("1.0.0") == "1.0.0") is False, "Una Version no es igual a un texto"

    print("Todas las pruebas pasaron")
