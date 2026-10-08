"""
Solución - Ejercicio propuesto 03 - Adivinar el número
"""

def adivinar(secreto, intentos, maximo=5):
    posicion = 0
    while posicion < len(intentos) and posicion < maximo:
        if intentos[posicion] == secreto:
            return f"Adivinaste en {posicion + 1} intentos"
        posicion += 1
    return f"Perdiste, el número era {secreto}"


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert adivinar(7, [3, 9, 7]) == "Adivinaste en 3 intentos"
    assert adivinar(7, [7]) == "Adivinaste en 1 intentos"
    assert adivinar(7, [1, 2]) == "Perdiste, el número era 7"
    assert adivinar(7, [1, 2, 3, 4, 5, 7]) == "Perdiste, el número era 7", "Solo hay 5 intentos"
    assert adivinar(7, [1, 7], maximo=1) == "Perdiste, el número era 7"
    assert adivinar(4, []) == "Perdiste, el número era 4"

    print("Todas las pruebas pasaron")
