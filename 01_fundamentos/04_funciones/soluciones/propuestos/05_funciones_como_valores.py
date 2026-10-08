"""
Solución - Ejercicio propuesto 05 - Funciones como valores
"""

def aplicar_varias_veces(funcion, valor, veces):
    # Caso base: si no hay que aplicarla más, el valor ya es el resultado.
    if veces == 0:
        return valor
    return aplicar_varias_veces(funcion, funcion(valor), veces - 1)


def componer(f, g):
    def compuesta(x):
        return f(g(x))
    return compuesta


def crear_multiplicador(n):
    # La función interna "recuerda" el valor de n aunque crear_multiplicador
    # ya haya terminado. A eso se le llama clausura.
    return lambda x: x * n


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert aplicar_varias_veces(lambda x: x * 2, 1, 3) == 8
    assert aplicar_varias_veces(lambda x: x + 10, 5, 0) == 5
    assert aplicar_varias_veces(str.upper, "hola", 1) == "HOLA"

    sumar_uno_y_duplicar = componer(lambda x: x * 2, lambda x: x + 1)
    assert sumar_uno_y_duplicar(3) == 8
    duplicar_y_sumar_uno = componer(lambda x: x + 1, lambda x: x * 2)
    assert duplicar_y_sumar_uno(3) == 7

    triple = crear_multiplicador(3)
    doble = crear_multiplicador(2)
    assert triple(5) == 15
    assert doble(5) == 10
    assert componer(triple, doble)(1) == 6

    print("Todas las pruebas pasaron")
