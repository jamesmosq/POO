"""
Solución - Ejercicio para corregir 05 - Ciclos anidados

CORRECCIÓN 1: el ciclo interno empezaba en 0, entonces cada número se
sumaba consigo mismo y cada pareja aparecía dos veces, (1, 4) y (4, 1). Si
j empieza en i + 1, solo se revisan los números que están después de i.

CORRECCIÓN 2: append(fila) agrega la lista completa como un solo
elemento. Para agregar sus elementos uno a uno se usa extend(fila) o un
segundo ciclo.

CORRECCIÓN 3: [[0] * filas] * columnas NO crea columnas listas distintas:
crea una lista con la MISMA lista repetida. Al escribir en una fila se
"modifican" todas. Cada fila debe crearse por separado.
"""

def parejas_que_suman(numeros, objetivo):
    parejas = []
    for i in range(len(numeros)):
        for j in range(i + 1, len(numeros)):  # CORRECCIÓN 1
            if numeros[i] + numeros[j] == objetivo:
                parejas.append((numeros[i], numeros[j]))
    return parejas


def aplanar(matriz):
    resultado = []
    for fila in matriz:
        resultado.extend(fila)  # CORRECCIÓN 2
    return resultado


def transponer(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    transpuesta = []
    for _ in range(columnas):  # CORRECCIÓN 3
        transpuesta.append([0] * filas)
    for i in range(filas):
        for j in range(columnas):
            transpuesta[j][i] = matriz[i][j]
    return transpuesta


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert parejas_que_suman([1, 2, 3, 4], 5) == [(1, 4), (2, 3)], parejas_que_suman([1, 2, 3, 4], 5)
    assert parejas_que_suman([5, 5], 10) == [(5, 5)]
    assert parejas_que_suman([1, 2], 10) == []

    assert aplanar([[1, 2], [3], []]) == [1, 2, 3], aplanar([[1, 2], [3], []])

    assert transponer([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]], transponer([[1, 2, 3], [4, 5, 6]])
    assert transponer([[1]]) == [[1]]

    print("Todas las pruebas pasaron")
