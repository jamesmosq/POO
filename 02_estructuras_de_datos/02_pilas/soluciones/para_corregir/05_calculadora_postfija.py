"""
Solución - Ejercicio para corregir 05 - Calculadora postfija

CORRECCIÓN 1 (ValueError: invalid literal for int() with base 10: '1.5'):
int() no convierte textos con decimales. Se usa float().

CORRECCIÓN 2 (10 2 - daba -8): el primer número que sale de la pila es el
operando de la DERECHA. Con a = derecha y b = izquierda, la resta debe ser
b - a. Lo mismo pasa con la división. Con + y * no se notaba porque el
orden no cambia el resultado.

CORRECCIÓN 3: al terminar, en la pila debe quedar exactamente un número.
Si quedan más, sobraron operandos y la expresión es inválida.
"""

def evaluar(expresion):
    pila = []
    for elemento in expresion.split():
        if elemento in "+-*/":
            if len(pila) < 2:
                raise ValueError("Expresión inválida")
            a = pila.pop()  # operando derecho
            b = pila.pop()  # operando izquierdo
            if elemento == "+":
                pila.append(b + a)
            elif elemento == "-":
                pila.append(b - a)  # CORRECCIÓN 2
            elif elemento == "*":
                pila.append(b * a)
            else:
                pila.append(b / a)  # CORRECCIÓN 2
        else:
            pila.append(float(elemento))  # CORRECCIÓN 1
    if len(pila) != 1:  # CORRECCIÓN 3
        raise ValueError("Expresión inválida")
    return pila.pop()


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert evaluar("3 4 + 2 *") == 14
    assert evaluar("1.5 2 *") == 3.0
    assert evaluar("10 2 -") == 8, f"evaluar('10 2 -') retornó {evaluar('10 2 -')}"
    assert evaluar("8 2 /") == 4

    try:
        evaluar("1 2")
        raise AssertionError("'1 2' no es una expresión completa: debe lanzar ValueError")
    except ValueError:
        pass

    print("Todas las pruebas pasaron")
