"""
Ejercicio para corregir 02 - Invertir con pila
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    invertir(texto) usa una lista como pila para invertir el texto.

        invertir("Hola") -> "aloH"

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


def invertir(texto):
    pila = []
    for caracter in texto:
        pila.append(caracter)

    resultado = ""
    while pila:
        caracter = pila.pop
        resultado = caracter + resultado
    return resultado


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert invertir("Hola") == "aloH", invertir("Hola")
    assert invertir("") == ""
    assert invertir("abc") == "cba"

    print("Todas las pruebas pasaron")
