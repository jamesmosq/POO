"""
Solución - Ejercicio para corregir 01 - Búsqueda lineal

CORRECCIÓN 1: la función retornaba el elemento encontrado (lista[i]) en
lugar de su posición (i).

CORRECCIÓN 2: range(1, len(lista)) empieza en 1 y nunca revisa el primer
elemento. Los índices empiezan en 0.
"""

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):  # CORRECCIÓN 2
        if lista[i] == objetivo:
            return i  # CORRECCIÓN 1
    return -1


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    letras = ["a", "b", "c"]
    assert busqueda_lineal(letras, "c") == 2, f"Se obtuvo {busqueda_lineal(letras, 'c')!r}"
    assert busqueda_lineal(letras, "a") == 0, f"Se obtuvo {busqueda_lineal(letras, 'a')!r}"
    assert busqueda_lineal(letras, "z") == -1

    print("Todas las pruebas pasaron")
