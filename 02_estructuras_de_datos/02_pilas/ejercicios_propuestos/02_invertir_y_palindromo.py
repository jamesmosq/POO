"""
Ejercicio propuesto 02 - Invertir textos y palíndromos
Nivel: básico

Como el último en entrar es el primero en salir, una pila sirve para
invertir cualquier secuencia.

Requisitos. Usa una lista como pila (append para apilar, pop para
desapilar). No uses texto[::-1] ni reversed(): el objetivo es practicar la
pila.
1. invertir(texto): apila todos los caracteres y luego desapílalos para
   construir el texto invertido.
       invertir("Hola") -> "aloH"
2. es_palindromo(texto): True si se lee igual al derecho y al revés,
   ignorando mayúsculas y espacios. Reutiliza invertir().
       es_palindromo("Anita lava la tina") -> True

Conceptos: pila con lista, LIFO, normalizar texto.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
