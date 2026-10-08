"""
Ejercicio para corregir 01 - Búsqueda lineal
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    busqueda_lineal(lista, objetivo) retorna la POSICIÓN (índice) de la
    primera aparición del objetivo, o -1 si no está.

        busqueda_lineal(["a", "b", "c"], "a") -> 0
        busqueda_lineal(["a", "b", "c"], "c") -> 2

Ojo: el programa no lanza errores, pero retorna valores incorrectos.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


def busqueda_lineal(lista, objetivo):
    for i in range(1, len(lista)):
        if lista[i] == objetivo:
            return lista[i]
    return -1


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    letras = ["a", "b", "c"]
    assert busqueda_lineal(letras, "c") == 2, f"Se obtuvo {busqueda_lineal(letras, 'c')!r}"
    assert busqueda_lineal(letras, "a") == 0, f"Se obtuvo {busqueda_lineal(letras, 'a')!r}"
    assert busqueda_lineal(letras, "z") == -1

    print("Todas las pruebas pasaron")
