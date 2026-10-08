"""
Solución - Ejercicio propuesto 01 - Conversiones seguras
"""

def a_entero(texto):
    try:
        return int(texto)
    except ValueError:
        return None


def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert a_entero("42") == 42
    assert a_entero("-7") == -7
    assert a_entero("abc") is None
    assert a_entero("3.5") is None
    assert a_entero("") is None

    assert dividir(10, 4) == 2.5
    assert dividir(10, 0) is None

    fuente = open(__file__, encoding="utf-8").read().split("# Pruebas")[0]
    assert "except:" not in fuente, "No uses except sin tipo de error"

    print("Todas las pruebas pasaron")
