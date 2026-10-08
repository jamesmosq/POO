"""
Solución - Ejercicio para corregir 02 - Invertir con pila

CORRECCIÓN 1 (TypeError: unsupported operand type(s) for +:
'builtin_function_or_method' and 'str'): pila.pop sin paréntesis es el
método, no su resultado. Para ejecutarlo hacen falta los paréntesis.

CORRECCIÓN 2 (el texto salía igual): la pila ya entrega los caracteres en
orden inverso. Al ponerlos además ADELANTE del resultado se invertía dos
veces y se volvía al texto original. Se agregan al final.
"""

def invertir(texto):
    pila = []
    for caracter in texto:
        pila.append(caracter)

    resultado = ""
    while pila:
        caracter = pila.pop()  # CORRECCIÓN 1
        resultado = resultado + caracter  # CORRECCIÓN 2
    return resultado


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert invertir("Hola") == "aloH", invertir("Hola")
    assert invertir("") == ""
    assert invertir("abc") == "cba"

    print("Todas las pruebas pasaron")
