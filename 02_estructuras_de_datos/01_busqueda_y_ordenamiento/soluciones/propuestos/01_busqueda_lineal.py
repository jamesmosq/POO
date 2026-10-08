"""
Solución - Ejercicio propuesto 01 - Búsqueda lineal
"""

def busqueda_lineal(lista, objetivo):
    comparaciones = 0
    for i in range(len(lista)):
        comparaciones += 1
        if lista[i] == objetivo:
            return i, comparaciones
    return -1, comparaciones


def buscar_todas(lista, objetivo):
    posiciones = []
    for i, elemento in enumerate(lista):
        if elemento == objetivo:
            posiciones.append(i)
    return posiciones


# Respuesta a la pregunta:
# 1.000.000 de comparaciones: tiene que revisar todos los elementos para
# asegurar que el objetivo no está. Ese es el "peor caso" y crece en
# proporción al tamaño de la lista (complejidad O(n)).


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    datos = [7, 3, 9, 3, 5]
    assert busqueda_lineal(datos, 7) == (0, 1)
    assert busqueda_lineal(datos, 9) == (2, 3)
    assert busqueda_lineal(datos, 3) == (1, 2), "Retorna la primera aparición"
    assert busqueda_lineal(datos, 8) == (-1, 5)
    assert busqueda_lineal([], 1) == (-1, 0)

    assert buscar_todas(datos, 3) == [1, 3]
    assert buscar_todas(datos, 8) == []
    assert buscar_todas(["a", "b", "a"], "a") == [0, 2]

    print("Todas las pruebas pasaron")
