"""
Solución - Ejercicio para corregir 04 - Inserción

CORRECCIÓN 1: con while j > 0 el ciclo nunca compara contra la posición 0,
así que el primer elemento no se movía. La condición es j >= 0.

CORRECCIÓN 2: resultado = lista no copia; ordenaba la lista original. Se
trabaja sobre lista.copy().

CORRECCIÓN 3: el parámetro descendente no se usaba. La condición para
correr un elemento depende del orden pedido.
"""

def insercion(lista, descendente=False):
    resultado = lista.copy()  # CORRECCIÓN 2
    for i in range(1, len(resultado)):
        actual = resultado[i]
        j = i - 1
        while j >= 0 and (  # CORRECCIÓN 1
            resultado[j] < actual if descendente else resultado[j] > actual  # CORRECCIÓN 3
        ):
            resultado[j + 1] = resultado[j]
            j -= 1
        resultado[j + 1] = actual
    return resultado


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert insercion([5, 2, 4, 6, 1, 3]) == [1, 2, 3, 4, 5, 6], insercion([5, 2, 4, 6, 1, 3])

    datos = [5, 2, 4]
    insercion(datos)
    assert datos == [5, 2, 4], f"La lista original cambió: {datos}"

    assert insercion([5, 2, 4], descendente=True) == [5, 4, 2], insercion([5, 2, 4], descendente=True)

    print("Todas las pruebas pasaron")
