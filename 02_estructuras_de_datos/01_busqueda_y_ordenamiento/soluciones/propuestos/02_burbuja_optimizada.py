"""
Solución - Ejercicio propuesto 02 - Burbuja optimizada
"""

def burbuja(lista):
    datos = lista.copy()
    n = len(datos)
    pasadas = 0
    for i in range(n - 1):
        pasadas += 1
        hubo_intercambio = False
        # Los últimos i elementos ya están en su lugar.
        for j in range(n - 1 - i):
            if datos[j] > datos[j + 1]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]
                hubo_intercambio = True
        if not hubo_intercambio:
            break
    return datos, pasadas


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    datos = [5, 1, 4, 2, 8]
    ordenada, pasadas = burbuja(datos)
    assert ordenada == [1, 2, 4, 5, 8]
    assert datos == [5, 1, 4, 2, 8], "No debe modificar la lista original"

    _, pasadas = burbuja([1, 2, 3, 4, 5])
    assert pasadas == 1, f"Una lista ya ordenada necesita una sola pasada, hizo {pasadas}"

    _, pasadas = burbuja([5, 4, 3, 2, 1])
    assert pasadas <= 5

    assert burbuja([])[0] == []
    assert burbuja(["pera", "Uva", "manzana"])[0] == ["Uva", "manzana", "pera"]

    print("Todas las pruebas pasaron")
