"""
Solución - Ejercicio propuesto 03 - Búsqueda binaria
"""

def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1
    pasos = 0
    while inicio <= fin:
        medio = (inicio + fin) // 2
        pasos += 1
        if lista[medio] == objetivo:
            return medio, pasos
        elif lista[medio] < objetivo:
            inicio = medio + 1  # el objetivo está a la derecha
        else:
            fin = medio - 1  # el objetivo está a la izquierda
    return -1, pasos


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    datos = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    for i, valor in enumerate(datos):
        posicion, _ = busqueda_binaria(datos, valor)
        assert posicion == i, f"{valor} está en la posición {i}, se obtuvo {posicion}"

    assert busqueda_binaria(datos, 23)[0] == 5
    assert busqueda_binaria(datos, 4)[0] == -1
    assert busqueda_binaria(datos, 100)[0] == -1
    assert busqueda_binaria([], 1)[0] == -1

    grande = list(range(1_000_000))
    posicion, pasos = busqueda_binaria(grande, 999_999)
    assert posicion == 999_999
    assert pasos <= 20, f"Hizo {pasos} pasos; la búsqueda binaria no debería pasar de 20"

    print("Todas las pruebas pasaron")
