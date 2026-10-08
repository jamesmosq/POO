"""
Solución - Ejercicio propuesto 02 - Leer el MRO
"""

class A:
    def saludar(self):
        return "Hola desde A"

    def presentar(self):
        return "Soy A"


class B(A):
    def saludar(self):
        return "Hola desde B"


class C(A):
    def saludar(self):
        return "Hola desde C"

    def despedir(self):
        return "Adiós desde C"


class D(B, C):
    pass


def orden(clase):
    return [c.__name__ for c in clase.mro() if c is not object]


def definido_en(clase, metodo):
    # Así busca Python: recorre el MRO y se detiene en la primera clase que
    # tiene el método en su propio __dict__.
    for c in clase.mro():
        if metodo in c.__dict__:
            return c.__name__
    return None


# Predicción y explicación:
# - despedir: B no lo define, y el siguiente en el MRO es C, no A. Por eso
#   retorna "C". En un diamante, la base común va al final del MRO.
# - presentar: ni B ni C lo definen, así que llega hasta A.


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert orden(D) == ["D", "B", "C", "A"]
    assert orden(B) == ["B", "A"]

    assert definido_en(D, "saludar") == "B"
    assert definido_en(D, "despedir") == "C", "B no lo tiene, así que Python sigue con C (no con A)"
    assert definido_en(D, "presentar") == "A"
    assert definido_en(D, "volar") is None

    # Lo que retorna el objeto coincide con el método de la clase indicada.
    clases = {"A": A, "B": B, "C": C, "D": D}
    d = D()
    for metodo in ("saludar", "despedir", "presentar"):
        origen = clases[definido_en(D, metodo)]
        assert getattr(d, metodo)() == getattr(origen, metodo)(d)

    print("Todas las pruebas pasaron")
