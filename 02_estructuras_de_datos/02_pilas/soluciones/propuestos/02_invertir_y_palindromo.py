"""
Solución - Ejercicio propuesto 02 - Invertir textos y palíndromos
"""

def invertir(texto):
    pila = []
    for caracter in texto:
        pila.append(caracter)
    resultado = ""
    while pila:
        resultado += pila.pop()  # sale primero el último que entró
    return resultado


def es_palindromo(texto):
    limpio = texto.lower().replace(" ", "")
    return limpio == invertir(limpio)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert invertir("Hola") == "aloH"
    assert invertir("") == ""
    assert invertir("a") == "a"

    assert es_palindromo("Anita lava la tina") is True
    assert es_palindromo("reconocer") is True
    assert es_palindromo("Python") is False

    fuente = open(__file__, encoding="utf-8").read().split("# Pruebas")[0]
    assert "[::-1]" not in fuente and "reversed(" not in fuente, "Usa una pila, no [::-1] ni reversed()"

    print("Todas las pruebas pasaron")
