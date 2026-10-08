"""
Solución - Ejercicio para corregir 05 - Impuesto progresivo

CORRECCIÓN 1: ValueError("...") solo crea el objeto de error; para lanzarlo
falta raise. Sin raise, la función sigue como si nada.

CORRECCIÓN 2: en el tramo 2 el 10 % se cobra solo sobre lo que pasa de 10
millones, no sobre todo el ingreso.

CORRECCIÓN 3: en el tramo 3 faltaban los 2.000.000 del tramo 2 completo.
"""

def impuesto(ingreso):
    if ingreso < 0:
        raise ValueError("El ingreso no puede ser negativo")  # CORRECCIÓN 1
    if ingreso <= 10_000_000:
        return 0
    elif ingreso <= 30_000_000:
        return (ingreso - 10_000_000) * 10 / 100  # CORRECCIÓN 2
    else:
        return 2_000_000 + (ingreso - 30_000_000) * 20 / 100  # CORRECCIÓN 3


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert impuesto(10_000_000) == 0
    assert impuesto(20_000_000) == 1_000_000, f"20M: {impuesto(20_000_000)}"
    assert impuesto(30_000_000) == 2_000_000, f"30M: {impuesto(30_000_000)}"
    assert impuesto(40_000_000) == 4_000_000, f"40M: {impuesto(40_000_000)}"

    try:
        impuesto(-1)
        raise AssertionError("Un ingreso negativo debe lanzar ValueError")
    except ValueError:
        pass

    print("Todas las pruebas pasaron")
