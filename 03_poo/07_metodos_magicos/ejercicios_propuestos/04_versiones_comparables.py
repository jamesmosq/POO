"""
Ejercicio propuesto 04 - Versiones comparables
Nivel: intermedio

Las versiones de software no se pueden comparar como texto:
    "1.10.0" < "1.9.0"   es True como texto (compara carácter por carácter)
pero la versión 1.10 es MÁS nueva que la 1.9.

Requisitos. Crea la clase Version(texto), por ejemplo Version("1.10.2"):
1. Guarda las partes como una tupla de enteros: (1, 10, 2). Si el texto no
   tiene el formato correcto, lanza ValueError.
2. __eq__ y __lt__ comparando las tuplas (Python compara tuplas elemento
   por elemento).
3. Decora la clase con @functools.total_ordering: a partir de __eq__ y
   __lt__ genera <=, > y >=.
4. __hash__: para poder usar versiones en un set o como claves de un
   diccionario. Dos versiones iguales deben tener el mismo hash.
5. __str__: "1.10.2".

Conceptos: comparaciones, total_ordering, __hash__ y su relación con __eq__.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
