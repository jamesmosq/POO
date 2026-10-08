"""
Solución - Ejercicio propuesto 04 - Versiones comparables
"""

from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, texto):
        try:
            self.partes = tuple(int(parte) for parte in texto.split("."))
        except ValueError:
            raise ValueError(f"Versión inválida: {texto!r}")

    def __eq__(self, otra):
        if not isinstance(otra, Version):
            return NotImplemented
        return self.partes == otra.partes

    def __lt__(self, otra):
        if not isinstance(otra, Version):
            return NotImplemented
        return self.partes < otra.partes

    def __hash__(self):
        # Objetos iguales deben tener el mismo hash: se usa lo mismo que __eq__.
        return hash(self.partes)

    def __str__(self):
        return ".".join(str(parte) for parte in self.partes)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert Version("1.10.0") > Version("1.9.0")
    assert Version("2.0.0") >= Version("2.0.0")
    assert Version("1.0.1") <= Version("1.0.2")
    assert Version("1.2.3") == Version("1.2.3")

    textos = ["1.10.0", "1.2.0", "1.9.3", "0.9.9"]
    ordenadas = sorted(Version(t) for t in textos)
    assert [str(v) for v in ordenadas] == ["0.9.9", "1.2.0", "1.9.3", "1.10.0"]

    assert len({Version("1.0.0"), Version("1.0.0"), Version("2.0.0")}) == 2
    assert max(Version(t) for t in textos) == Version("1.10.0")

    for invalido in ["1.a.0", "", "1..2"]:
        try:
            Version(invalido)
            raise AssertionError(f"{invalido!r} debe lanzar ValueError")
        except ValueError:
            pass

    print("Todas las pruebas pasaron")
