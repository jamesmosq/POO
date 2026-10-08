"""
Solución - Ejercicio propuesto 05 - Impuesto progresivo
"""

def impuesto(ingreso):
    if ingreso < 0:
        raise ValueError("El ingreso no puede ser negativo")
    if ingreso <= 10_000_000:
        return 0
    elif ingreso <= 30_000_000:
        return (ingreso - 10_000_000) * 10 / 100
    else:
        # 2.000.000 corresponde al tramo 2 completo: (30M - 10M) * 10 %
        return 2_000_000 + (ingreso - 30_000_000) * 20 / 100


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert impuesto(0) == 0
    assert impuesto(5_000_000) == 0
    assert impuesto(10_000_000) == 0
    assert impuesto(20_000_000) == 1_000_000
    assert impuesto(30_000_000) == 2_000_000
    assert impuesto(40_000_000) == 4_000_000
    assert impuesto(100_000_000) == 16_000_000

    try:
        impuesto(-1)
        raise AssertionError("Un ingreso negativo debe lanzar ValueError")
    except ValueError:
        pass

    print("Todas las pruebas pasaron")
