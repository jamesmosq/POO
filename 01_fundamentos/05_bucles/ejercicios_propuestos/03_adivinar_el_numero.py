"""
Ejercicio propuesto 03 - Adivinar el número
Nivel: intermedio

En un juego real los intentos llegarían con input(). Para poder probarlo,
aquí llegan en una lista.

Requisitos. Escribe adivinar(secreto, intentos, maximo=5):
1. Recorre los intentos con un ciclo while, usando una variable de
   posición.
2. Si un intento es igual al secreto, retorna "Adivinaste en N intentos"
   (con N el número del intento: el primero es 1).
3. Se juega hasta acertar, hasta agotar los intentos de la lista o hasta
   llegar a maximo intentos, lo que ocurra primero.
4. Si no acierta, retorna "Perdiste, el número era S".

Para jugar de verdad, al final puedes escribir una versión con input()
dentro de if __name__ == "__main__", después de las pruebas.

Conceptos: while, condición compuesta, break o return dentro del ciclo.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert adivinar(7, [3, 9, 7]) == "Adivinaste en 3 intentos"
    assert adivinar(7, [7]) == "Adivinaste en 1 intentos"
    assert adivinar(7, [1, 2]) == "Perdiste, el número era 7"
    assert adivinar(7, [1, 2, 3, 4, 5, 7]) == "Perdiste, el número era 7", "Solo hay 5 intentos"
    assert adivinar(7, [1, 7], maximo=1) == "Perdiste, el número era 7"
    assert adivinar(4, []) == "Perdiste, el número era 4"

    print("Todas las pruebas pasaron")
