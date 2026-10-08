"""
Ejercicio para corregir 03 - Paréntesis balanceados
Nivel: intermedio
Errores a encontrar: 2

Qué debería hacer el programa:
    balanceado(expresion) retorna True si los ( ) [ ] { } están bien
    abiertos y cerrados, en el orden correcto.

        balanceado("([])")  -> True
        balanceado("(]")    -> False
        balanceado("((")    -> False

Ojo: el programa no lanza errores; algunas expresiones mal escritas se
aceptan como correctas.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""

PAREJAS = {")": "(", "]": "[", "}": "{"}


def balanceado(expresion):
    pila = []
    for caracter in expresion:
        if caracter in "([{":
            pila.append(caracter)
        elif caracter in ")]}":
            if not pila:
                return False
            pila.pop()
    return True


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert balanceado("([])") is True
    assert balanceado("{[()]}") is True
    assert balanceado(")") is False
    assert balanceado("((") is False, "Quedaron paréntesis sin cerrar"
    assert balanceado("(]") is False, "Un ( no se cierra con ]"
    assert balanceado("([)]") is False

    print("Todas las pruebas pasaron")
