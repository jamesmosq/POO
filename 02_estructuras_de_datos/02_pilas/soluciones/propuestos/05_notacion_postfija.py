"""
Solución - Ejercicio propuesto 05 - Notación postfija y cambio de base
"""

DIGITOS = "0123456789ABCDEF"


def evaluar_postfija(expresion):
    pila = []
    for elemento in expresion.split():
        if elemento in ("+", "-", "*", "/"):
            if len(pila) < 2:
                raise ValueError("Expresión inválida")
            derecha = pila.pop()  # el primero que sale es el de la derecha
            izquierda = pila.pop()
            if elemento == "+":
                pila.append(izquierda + derecha)
            elif elemento == "-":
                pila.append(izquierda - derecha)
            elif elemento == "*":
                pila.append(izquierda * derecha)
            else:
                pila.append(izquierda / derecha)
        else:
            pila.append(float(elemento))
    if len(pila) != 1:
        raise ValueError("Expresión inválida")
    return pila[0]


def a_base(numero, base):
    if numero == 0:
        return "0"
    pila = []
    while numero > 0:
        pila.append(DIGITOS[numero % base])
        numero //= base
    # Los residuos salen del último al primero: justo el orden de una pila.
    resultado = ""
    while pila:
        resultado += pila.pop()
    return resultado


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert evaluar_postfija("3 4 + 2 *") == 14
    assert evaluar_postfija("10 2 -") == 8, "El primero que se desapila es el de la derecha"
    assert evaluar_postfija("9 3 /") == 3
    assert evaluar_postfija("2.5 2 *") == 5
    assert evaluar_postfija("5 1 2 + 4 * + 3 -") == 14

    for invalida in ["3 +", "1 2", "", "+"]:
        try:
            evaluar_postfija(invalida)
            raise AssertionError(f"{invalida!r} debe lanzar ValueError")
        except ValueError as error:
            assert str(error) == "Expresión inválida"

    assert a_base(10, 2) == "1010"
    assert a_base(255, 16) == "FF"
    assert a_base(0, 2) == "0"
    assert a_base(64, 8) == "100"

    print("Todas las pruebas pasaron")
