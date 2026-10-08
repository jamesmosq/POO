"""
Ejercicio propuesto 04 - Matrices
Nivel: intermedio

Una matriz se representa como una lista de filas, y cada fila es una
lista:
    m = [[1, 2],
         [3, 4]]       m[0][1] es 2 (fila 0, columna 1)

Requisitos (sin usar NumPy):
1. dimensiones(m): retorna la tupla (filas, columnas).
2. sumar(a, b): retorna una matriz NUEVA con la suma posición a posición.
   Si las dimensiones no coinciden, lanza ValueError.
3. diagonal(m): retorna la lista de la diagonal principal (m[0][0],
   m[1][1], ...). Si la matriz no es cuadrada, lanza ValueError.
4. por_escalar(m, k): retorna una matriz nueva con cada elemento
   multiplicado por k.

Conceptos: listas anidadas, índices dobles, ciclos anidados.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
