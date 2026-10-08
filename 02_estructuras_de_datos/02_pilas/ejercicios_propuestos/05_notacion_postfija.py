"""
Ejercicio propuesto 05 - Notación postfija y cambio de base
Nivel: avanzado

En notación postfija (o polaca inversa) los operadores van DESPUÉS de los
operandos y no se necesitan paréntesis:
    infija:   (3 + 4) * 2
    postfija: 3 4 + 2 *

Se evalúa con una pila:
    - Si el elemento es un número, se apila.
    - Si es un operador, se desapilan dos números, se opera y se apila el
      resultado. Ojo con el orden: el PRIMERO que se desapila es el
      operando de la DERECHA.

Requisitos:
1. evaluar_postfija(expresion): los elementos vienen separados por
   espacios. Soporta + - * / y números decimales. Lanza
   ValueError("Expresión inválida") si faltan operandos o si al final no
   queda exactamente un número en la pila.
2. a_base(numero, base): convierte un entero no negativo a otra base (2 a
   16) usando una pila con los residuos de dividir sucesivamente.
       a_base(10, 2)  -> "1010"
       a_base(255, 16) -> "FF"

Conceptos: pila como evaluador, orden de operandos, conversión de bases.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
