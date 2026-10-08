"""
Solución - Ejercicio propuesto 04 - Matrices
"""

def dimensiones(m):
    return len(m), len(m[0])


def sumar(a, b):
    if dimensiones(a) != dimensiones(b):
        raise ValueError("Las matrices deben tener las mismas dimensiones")
    filas, columnas = dimensiones(a)
    resultado = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(a[i][j] + b[i][j])
        resultado.append(fila)
    return resultado


def diagonal(m):
    filas, columnas = dimensiones(m)
    if filas != columnas:
        raise ValueError("La matriz debe ser cuadrada")
    return [m[i][i] for i in range(filas)]


def por_escalar(m, k):
    return [[valor * k for valor in fila] for fila in m]


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[10, 20, 30], [40, 50, 60]]
    cuadrada = [[1, 2], [3, 4]]

    assert dimensiones(a) == (2, 3)
    assert sumar(a, b) == [[11, 22, 33], [44, 55, 66]]
    assert a == [[1, 2, 3], [4, 5, 6]], "sumar() no debe modificar las matrices"
    assert diagonal(cuadrada) == [1, 4]
    assert por_escalar(cuadrada, 3) == [[3, 6], [9, 12]]

    for funcion, argumentos in [(sumar, (a, cuadrada)), (diagonal, (a,))]:
        try:
            funcion(*argumentos)
            raise AssertionError(f"{funcion.__name__} debe lanzar ValueError")
        except ValueError:
            pass

    print("Todas las pruebas pasaron")
