"""
Ejercicio para corregir 02 - Burbuja
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    burbuja(lista) ordena la lista de MENOR a MAYOR (la modifica) y la
    retorna.

        burbuja([5, 1, 4, 2]) -> [1, 2, 4, 5]

Ojo: el programa no lanza errores. Imprime la lista después de cada
intercambio para ver qué está pasando con los valores.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


def burbuja(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] < lista[j + 1]:
                lista[j] = lista[j + 1]
                lista[j + 1] = lista[j]
    return lista


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert burbuja([5, 1, 4, 2]) == [1, 2, 4, 5], burbuja([5, 1, 4, 2])
    assert burbuja([3, 3, 1]) == [1, 3, 3]
    assert burbuja([]) == []

    print("Todas las pruebas pasaron")
