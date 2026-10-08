"""
Ejercicio para corregir 05 - Merge sort
Nivel: avanzado
Errores a encontrar: 3

Qué debería hacer el programa:
    merge_sort(lista, key) ordena con el algoritmo merge sort. Debe ser
    ESTABLE: si dos elementos tienen la misma clave, conservan el orden en
    que venían.

        personas = [("Ana", 3), ("Luis", 1), ("Eva", 3)]
        merge_sort(personas, key=lambda p: p[1])
            -> [("Luis", 1), ("Ana", 3), ("Eva", 3)]

Pista: si ves RecursionError, revisa el caso base: ¿cuándo debe dejar de
llamarse a sí misma la función?

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


def mezclar(izquierda, derecha, key):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if key(izquierda[i]) < key(derecha[j]):
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    return resultado


def merge_sort(lista, key=lambda x: x):
    if len(lista) < 1:
        return lista
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio], key)
    derecha = merge_sort(lista[medio:], key)
    return mezclar(izquierda, derecha, key)


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert merge_sort([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82], merge_sort([38, 27, 43, 3, 9, 82, 10])
    assert merge_sort([]) == []

    personas = [("Ana", 3), ("Luis", 1), ("Eva", 3)]
    assert merge_sort(personas, key=lambda p: p[1]) == [("Luis", 1), ("Ana", 3), ("Eva", 3)], merge_sort(personas, key=lambda p: p[1])

    print("Todas las pruebas pasaron")
