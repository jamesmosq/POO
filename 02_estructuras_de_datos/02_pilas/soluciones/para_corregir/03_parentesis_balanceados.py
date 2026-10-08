"""
Solución - Ejercicio para corregir 03 - Paréntesis balanceados

CORRECCIÓN 1: al terminar el recorrido, la pila debe estar vacía. Si
quedan aperturas sin cerrar, como en "((", la expresión no está balanceada.

CORRECCIÓN 2: al cerrar, no basta con que haya algo en la pila: la cima
debe ser la pareja de apertura de ese cierre. Si no, "(]" se aceptaba.
"""

PAREJAS = {")": "(", "]": "[", "}": "{"}


def balanceado(expresion):
    pila = []
    for caracter in expresion:
        if caracter in "([{":
            pila.append(caracter)
        elif caracter in ")]}":
            if not pila or pila[-1] != PAREJAS[caracter]:  # CORRECCIÓN 2
                return False
            pila.pop()
    return len(pila) == 0  # CORRECCIÓN 1


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert balanceado("([])") is True
    assert balanceado("{[()]}") is True
    assert balanceado(")") is False
    assert balanceado("((") is False, "Quedaron paréntesis sin cerrar"
    assert balanceado("(]") is False, "Un ( no se cierra con ]"
    assert balanceado("([)]") is False

    print("Todas las pruebas pasaron")
