"""
Ejercicio para corregir 05 - Ciclos anidados
Nivel: avanzado
Errores a encontrar: 3

Qué debería hacer el programa:
    - parejas_que_suman(numeros, objetivo): retorna las parejas de números
      (en posiciones distintas) que suman el objetivo, cada pareja una sola
      vez y en el orden en que aparecen.
          parejas_que_suman([1, 2, 3, 4], 5) -> [(1, 4), (2, 3)]
    - aplanar(matriz): convierte una lista de listas en una sola lista.
          aplanar([[1, 2], [3]]) -> [1, 2, 3]
    - transponer(matriz): cambia filas por columnas.
          transponer([[1, 2, 3], [4, 5, 6]]) -> [[1, 4], [2, 5], [3, 6]]

Ojo: uno de los errores es muy difícil de ver a simple vista. Si una fila
cambia "sola" cuando modificas otra, investiga qué hace [lista] * n.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


def parejas_que_suman(numeros, objetivo):
    parejas = []
    for i in range(len(numeros)):
        for j in range(len(numeros)):
            if numeros[i] + numeros[j] == objetivo:
                parejas.append((numeros[i], numeros[j]))
    return parejas


def aplanar(matriz):
    resultado = []
    for fila in matriz:
        resultado.append(fila)
    return resultado


def transponer(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    transpuesta = [[0] * filas] * columnas
    for i in range(filas):
        for j in range(columnas):
            transpuesta[j][i] = matriz[i][j]
    return transpuesta


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert parejas_que_suman([1, 2, 3, 4], 5) == [(1, 4), (2, 3)], parejas_que_suman([1, 2, 3, 4], 5)
    assert parejas_que_suman([5, 5], 10) == [(5, 5)]
    assert parejas_que_suman([1, 2], 10) == []

    assert aplanar([[1, 2], [3], []]) == [1, 2, 3], aplanar([[1, 2], [3], []])

    assert transponer([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]], transponer([[1, 2, 3], [4, 5, 6]])
    assert transponer([[1]]) == [[1]]

    print("Todas las pruebas pasaron")
