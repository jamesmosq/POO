"""
Solución - Ejercicio para corregir 05 - Merge sort

CORRECCIÓN 1 (RecursionError: maximum recursion depth exceeded): con
len(lista) < 1, una lista de UN elemento se volvía a partir en [] y [x]
para siempre. Una lista de 0 o 1 elementos ya está ordenada: el caso base
es len(lista) <= 1.

CORRECCIÓN 2 (faltaban elementos): al terminar el while, pueden quedar
elementos en cualquiera de las dos listas. Se agregaban los de la
izquierda, pero no los de la derecha.

CORRECCIÓN 3 (orden no estable): con <, en un empate se tomaba primero el
de la derecha y los elementos iguales cambiaban de orden. Con <= gana el
de la izquierda y se conserva el orden original.
"""

def mezclar(izquierda, derecha, key):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if key(izquierda[i]) <= key(derecha[j]):  # CORRECCIÓN 3
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])  # CORRECCIÓN 2
    return resultado


def merge_sort(lista, key=lambda x: x):
    if len(lista) <= 1:  # CORRECCIÓN 1
        return lista
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio], key)
    derecha = merge_sort(lista[medio:], key)
    return mezclar(izquierda, derecha, key)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert merge_sort([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82], merge_sort([38, 27, 43, 3, 9, 82, 10])
    assert merge_sort([]) == []

    personas = [("Ana", 3), ("Luis", 1), ("Eva", 3)]
    assert merge_sort(personas, key=lambda p: p[1]) == [("Luis", 1), ("Ana", 3), ("Eva", 3)], merge_sort(personas, key=lambda p: p[1])

    print("Todas las pruebas pasaron")
