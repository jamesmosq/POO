"""
Ejercicio para corregir 05 - Calculadora postfija
Nivel: avanzado
Errores a encontrar: 3

Qué debería hacer el programa:
    evaluar(expresion) evalúa una expresión en notación postfija, con los
    elementos separados por espacios. Acepta decimales. Si la expresión
    está incompleta o sobran números, lanza ValueError("Expresión inválida").

        evaluar("3 4 + 2 *")  -> 14
        evaluar("10 2 -")     -> 8
        evaluar("1.5 2 *")    -> 3.0
        evaluar("1 2")        -> ValueError

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


def evaluar(expresion):
    pila = []
    for elemento in expresion.split():
        if elemento in "+-*/":
            if len(pila) < 2:
                raise ValueError("Expresión inválida")
            a = pila.pop()
            b = pila.pop()
            if elemento == "+":
                pila.append(a + b)
            elif elemento == "-":
                pila.append(a - b)
            elif elemento == "*":
                pila.append(a * b)
            else:
                pila.append(a / b)
        else:
            pila.append(int(elemento))
    return pila.pop()


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
