"""
Solución - Ejercicio para corregir 01 - Convertir número

CORRECCIÓN 1 (SyntaxError: expected 'except' or 'finally' block): un try
siempre debe ir acompañado de al menos un except o un finally.

CORRECCIÓN 2 (ValueError sin atrapar): int("hola") lanza ValueError, no
TypeError. El except solo atrapa el tipo de error que se le indica. Para
saber cuál es, ejecuta el código que falla y lee la última línea del
mensaje.
"""

def convertir(texto):
    try:
        return int(texto)
    except ValueError:  # CORRECCIÓN 2
        return "Entrada inválida"


def convertir_o_cero(texto):
    try:
        return int(texto)
    except ValueError:  # CORRECCIÓN 1
        return 0


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert convertir("15") == 15
    assert convertir("hola") == "Entrada inválida"
    assert convertir_o_cero("8") == 8
    assert convertir_o_cero("x") == 0

    print("Todas las pruebas pasaron")
