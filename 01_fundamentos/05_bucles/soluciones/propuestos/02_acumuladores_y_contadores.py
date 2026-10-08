"""
Solución - Ejercicio propuesto 02 - Acumuladores y contadores
"""

VOCALES = "aeiouáéíóú"


def suma_pares(limite):
    total = 0
    for numero in range(2, limite + 1, 2):  # empieza en 2 y avanza de 2 en 2
        total += numero
    return total


def contar_vocales(texto):
    contador = 0
    for letra in texto.lower():
        if letra in VOCALES:
            contador += 1
    return contador


# ----------------------------------------------------------------------
# Pruebas
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
