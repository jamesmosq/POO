"""
Solución - Ejercicio propuesto 04 - Ordenamiento por inserción
"""

def debe_ir_antes(a, b, descendente):
    return a > b if descendente else a < b


def insercion(lista, descendente=False):
    datos = lista.copy()
    for i in range(1, len(datos)):
        actual = datos[i]
        j = i - 1
        # Se corren a la derecha los elementos que deben ir después de actual.
        while j >= 0 and debe_ir_antes(actual, datos[j], descendente):
            datos[j + 1] = datos[j]
            j -= 1
        datos[j + 1] = actual
    return datos


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    datos = [5, 2, 4, 6, 1, 3]
    assert insercion(datos) == [1, 2, 3, 4, 5, 6]
    assert insercion(datos, descendente=True) == [6, 5, 4, 3, 2, 1]
    assert datos == [5, 2, 4, 6, 1, 3], "No debe modificar la original"
    assert insercion([]) == []
    assert insercion([1]) == [1]
    assert insercion([3, 1, 2, 1]) == [1, 1, 2, 3]

    fuente = open(__file__, encoding="utf-8").read().split("# Pruebas")[0]
    assert "sorted(" not in fuente and ".sort(" not in fuente, "No uses sort() ni sorted()"

    print("Todas las pruebas pasaron")
