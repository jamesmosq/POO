"""
Ejercicio para corregir 02 - Promedio de una lista
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    promedio(numeros) suma todos los números de la lista con un for y
    divide entre la cantidad.

        promedio([2, 4, 6]) -> 4.0

Ojo: el programa no lanza errores. Agrega un print() dentro del ciclo
para ver qué valor tiene total en cada vuelta.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


def promedio(numeros):
    for n in numeros:
        total = 0
        total += n
        return total / len(numeros)


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert promedio([2, 4, 6]) == 4.0, f"promedio([2, 4, 6]) retornó {promedio([2, 4, 6])}"
    assert promedio([10]) == 10.0
    assert promedio([1, 2, 3, 4]) == 2.5

    print("Todas las pruebas pasaron")
