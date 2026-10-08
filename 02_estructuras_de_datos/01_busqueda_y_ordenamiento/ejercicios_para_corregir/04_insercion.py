"""
Ejercicio para corregir 04 - Inserción
Nivel: intermedio
Errores a encontrar: 3

Qué debería hacer el programa:
    insercion(lista, descendente=False) retorna una lista NUEVA ordenada
    con el método de inserción. La original no cambia.

        insercion([5, 2, 4])                    -> [2, 4, 5]
        insercion([5, 2, 4], descendente=True)  -> [5, 4, 2]

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


def insercion(lista, descendente=False):
    resultado = lista
    for i in range(1, len(resultado)):
        actual = resultado[i]
        j = i - 1
        while j > 0 and resultado[j] > actual:
            resultado[j + 1] = resultado[j]
            j -= 1
        resultado[j + 1] = actual
    return resultado


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert insercion([5, 2, 4, 6, 1, 3]) == [1, 2, 3, 4, 5, 6], insercion([5, 2, 4, 6, 1, 3])

    datos = [5, 2, 4]
    insercion(datos)
    assert datos == [5, 2, 4], f"La lista original cambió: {datos}"

    assert insercion([5, 2, 4], descendente=True) == [5, 4, 2], insercion([5, 2, 4], descendente=True)

    print("Todas las pruebas pasaron")
