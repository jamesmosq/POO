"""
Solución - Ejercicio propuesto 03 - Paréntesis balanceados
"""

PAREJAS = {")": "(", "]": "[", "}": "{"}


def balanceado(expresion):
    pila = []
    for caracter in expresion:
        if caracter in "([{":
            pila.append(caracter)
        elif caracter in PAREJAS:
            if not pila or pila[-1] != PAREJAS[caracter]:
                return False
            pila.pop()
    return len(pila) == 0  # no deben quedar aperturas sin cerrar


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    for correcta in ["", "()", "([]{})", "{[()()]}", "f(x) = [a + b] * {c}"]:
        assert balanceado(correcta) is True, f"{correcta!r} está balanceada"
    for incorrecta in ["(", ")", "(]", "([)]", "((())", "{[}]", "())("]:
        assert balanceado(incorrecta) is False, f"{incorrecta!r} NO está balanceada"

    print("Todas las pruebas pasaron")
