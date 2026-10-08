"""
Solución - Ejercicio para corregir 03 - Búsqueda binaria

CORRECCIÓN 1 (TypeError: list indices must be integers or slices, not
float): / siempre da un float, y los índices deben ser enteros. Se usa la
división entera //.

CORRECCIÓN 2: con while inicio < fin, el ciclo termina cuando queda UN
solo elemento sin revisarlo. Por eso fallaba con [4] y con algunos
extremos. La condición correcta es inicio <= fin.
"""

def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:  # CORRECCIÓN 2
        medio = (inicio + fin) // 2  # CORRECCIÓN 1
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    datos = [2, 5, 8, 12, 16, 23, 38]
    for i, valor in enumerate(datos):
        assert busqueda_binaria(datos, valor) == i, f"{valor}: se esperaba {i}, se obtuvo {busqueda_binaria(datos, valor)}"
    assert busqueda_binaria(datos, 7) == -1
    assert busqueda_binaria([4], 4) == 0
    assert busqueda_binaria([], 4) == -1

    print("Todas las pruebas pasaron")
