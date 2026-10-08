"""
Ejercicio para corregir 03 - Búsqueda binaria
Nivel: intermedio
Errores a encontrar: 2

Qué debería hacer el programa:
    busqueda_binaria(lista, objetivo) busca en una lista ORDENADA y retorna
    la posición del objetivo, o -1 si no está.

        busqueda_binaria([2, 5, 8, 12], 12) -> 3

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1
    while inicio < fin:
        medio = (inicio + fin) / 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    datos = [2, 5, 8, 12, 16, 23, 38]
    for i, valor in enumerate(datos):
        assert busqueda_binaria(datos, valor) == i, f"{valor}: se esperaba {i}, se obtuvo {busqueda_binaria(datos, valor)}"
    assert busqueda_binaria(datos, 7) == -1
    assert busqueda_binaria([4], 4) == 0
    assert busqueda_binaria([], 4) == -1

    print("Todas las pruebas pasaron")
