"""
Ejercicio propuesto 02 - Acumuladores y contadores
Nivel: básico

Requisitos:
1. suma_pares(limite): suma los números pares desde 1 hasta limite
   (incluido) usando un for.
       suma_pares(10) -> 2 + 4 + 6 + 8 + 10 = 30
2. contar_vocales(texto): cuenta cuántas vocales tiene un texto, sin
   importar mayúsculas ni tildes (a, e, i, o, u, á, é, í, ó, ú).
       contar_vocales("Programación") -> 5

Un acumulador empieza en 0 y en cada vuelta se le suma algo:
    total = 0
    for ...:
        total += ...

Conceptos: for, range con paso, recorrer un texto, acumuladores, in.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert suma_pares(10) == 30
    assert suma_pares(11) == 30
    assert suma_pares(1) == 0
    assert suma_pares(2) == 2

    assert contar_vocales("Programación") == 5
    assert contar_vocales("PYTHON") == 1
    assert contar_vocales("xyz") == 0
    assert contar_vocales("") == 0

    print("Todas las pruebas pasaron")
