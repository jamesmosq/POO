"""
Solución - Ejercicio propuesto 05 - Merge sort y ordenamiento por criterios
"""

def mezclar(izquierda, derecha, key):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        # Con <= el empate se resuelve a favor de la izquierda: orden estable.
        if key(izquierda[i]) <= key(derecha[j]):
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado


def merge_sort(lista, key=None):
    if key is None:
        key = lambda x: x
    if len(lista) <= 1:
        return list(lista)
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio], key)
    derecha = merge_sort(lista[medio:], key)
    return mezclar(izquierda, derecha, key)


def ordenar_estudiantes(estudiantes):
    # -nota invierte el orden de la nota sin invertir el del nombre.
    return sorted(estudiantes, key=lambda e: (-e[1], e[0]))


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import random

    assert mezclar([1, 4, 9], [2, 3, 10], key=lambda x: x) == [1, 2, 3, 4, 9, 10]
    assert merge_sort([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82]
    assert merge_sort([]) == []

    aleatorios = [random.randint(-1000, 1000) for _ in range(500)]
    assert merge_sort(aleatorios) == sorted(aleatorios)

    personas = [("Ana", 3), ("Luis", 1), ("Eva", 3), ("Beto", 1)]
    assert merge_sort(personas, key=lambda p: p[1]) == [("Luis", 1), ("Beto", 1), ("Ana", 3), ("Eva", 3)], (
        "Con notas iguales se debe conservar el orden original"
    )

    estudiantes = [("Eva", 4.5), ("Ana", 3.8), ("Luis", 4.5), ("Beto", 3.8)]
    assert ordenar_estudiantes(estudiantes) == [("Eva", 4.5), ("Luis", 4.5), ("Ana", 3.8), ("Beto", 3.8)]

    print("Todas las pruebas pasaron")
