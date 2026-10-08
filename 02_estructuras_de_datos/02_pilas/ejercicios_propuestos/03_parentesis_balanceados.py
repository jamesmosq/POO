"""
Ejercicio propuesto 03 - Paréntesis balanceados
Nivel: intermedio

Los editores de código y los compiladores usan una pila para revisar que
los paréntesis, corchetes y llaves estén bien cerrados.

Algoritmo:
    - Recorre la expresión carácter por carácter.
    - Si es de apertura ( [ {  -> apílalo.
    - Si es de cierre ) ] }    -> la pila no puede estar vacía y la cima
                                  debe ser su pareja de apertura;
                                  si es así, desapila.
    - Ignora cualquier otro carácter.
    - Al final, la pila debe quedar vacía.

Requisitos. Escribe balanceado(expresion), que retorne True o False.

Pista: un diccionario {")": "(", "]": "[", "}": "{"} da la pareja de cada
cierre.

Conceptos: pila, validación de estructura, diccionarios.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    for correcta in ["", "()", "([]{})", "{[()()]}", "f(x) = [a + b] * {c}"]:
        assert balanceado(correcta) is True, f"{correcta!r} está balanceada"
    for incorrecta in ["(", ")", "(]", "([)]", "((())", "{[}]", "())("]:
        assert balanceado(incorrecta) is False, f"{incorrecta!r} NO está balanceada"

    print("Todas las pruebas pasaron")
