"""
Solución - Ejercicio para corregir 04 - Quitar pares y buscar

CORRECCIÓN 1: al hacer remove dentro del for, la lista se corre y el ciclo
se salta el elemento siguiente a cada uno que se borra. Se construye una
lista nueva con los elementos que sí se quieren conservar.

CORRECCIÓN 2: la función modificaba la lista original (las listas se pasan
por referencia). Con la lista nueva del punto anterior se evita.

CORRECCIÓN 3: con return -1 en el else, la búsqueda terminaba en el primer
elemento que no coincidía. "No está" solo se sabe cuando se recorrió toda
la lista, así que el return -1 va después del for.
"""

def quitar_pares(numeros):
    resultado = []  # CORRECCIÓN 1 y 2
    for n in numeros:
        if n % 2 != 0:
            resultado.append(n)
    return resultado


def buscar_posicion(lista, objetivo):
    for i, elemento in enumerate(lista):
        if elemento == objetivo:
            return i
    return -1  # CORRECCIÓN 3


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    datos = [1, 2, 4, 5, 6, 8]
    assert quitar_pares(datos) == [1, 5], f"quitar_pares retornó {quitar_pares([1, 2, 4, 5, 6, 8])}"
    assert datos == [1, 2, 4, 5, 6, 8], f"La lista original cambió: {datos}"

    assert buscar_posicion(["a", "b", "c"], "a") == 0
    assert buscar_posicion(["a", "b", "c"], "c") == 2
    assert buscar_posicion(["a", "b", "c"], "z") == -1
    assert buscar_posicion([], "a") == -1

    print("Todas las pruebas pasaron")
