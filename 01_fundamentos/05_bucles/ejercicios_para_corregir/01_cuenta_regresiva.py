"""
Ejercicio para corregir 01 - Cuenta regresiva
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    cuenta_regresiva(n) retorna una lista de n hasta 1.

        cuenta_regresiva(5) -> [5, 4, 3, 2, 1]

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


def cuenta_regresiva(n):
    resultado = []
    for i in range(n, 0):
        numero = i
    resultado.append(numero)
    return resultado


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert cuenta_regresiva(5) == [5, 4, 3, 2, 1], cuenta_regresiva(5)
    assert cuenta_regresiva(1) == [1]
    assert cuenta_regresiva(0) == []

    print("Todas las pruebas pasaron")
