"""
Solución - Ejercicio para corregir 02 - Burbuja

CORRECCIÓN 1: el intercambio perdía un valor. Después de
lista[j] = lista[j + 1], el valor original de lista[j] ya no existe, y la
segunda línea copia el mismo valor de vuelta. En Python se intercambia en
una sola línea: a, b = b, a (o con una variable temporal).

CORRECCIÓN 2: con < se intercambiaba cuando el de la izquierda era menor,
lo que ordena de mayor a menor. Para ordenar de menor a mayor se
intercambia cuando el de la izquierda es MAYOR.
"""

def burbuja(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:  # CORRECCIÓN 2
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  # CORRECCIÓN 1
    return lista


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert burbuja([5, 1, 4, 2]) == [1, 2, 4, 5], burbuja([5, 1, 4, 2])
    assert burbuja([3, 3, 1]) == [1, 3, 3]
    assert burbuja([]) == []

    print("Todas las pruebas pasaron")
