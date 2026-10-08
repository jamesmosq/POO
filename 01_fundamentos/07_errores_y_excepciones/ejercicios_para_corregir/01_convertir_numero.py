"""
Ejercicio para corregir 01 - Convertir número
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    - convertir(texto) retorna el número entero, o el texto
      "Entrada inválida" si no se puede convertir.
    - convertir_o_cero(texto) retorna el número entero, o 0 si no se puede
      convertir.

        convertir("15")         -> 15
        convertir("hola")       -> "Entrada inválida"
        convertir_o_cero("x")   -> 0

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


def convertir(texto):
    try:
        return int(texto)
    except TypeError:
        return "Entrada inválida"


def convertir_o_cero(texto):
    try:
        return int(texto)
    return 0


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert convertir("15") == 15
    assert convertir("hola") == "Entrada inválida"
    assert convertir_o_cero("8") == 8
    assert convertir_o_cero("x") == 0

    print("Todas las pruebas pasaron")
