"""
Ejercicio propuesto 05 - Impuesto progresivo
Nivel: avanzado

En un impuesto progresivo cada tramo del ingreso paga una tasa distinta.
Solo se cobra la tasa más alta sobre la parte que supera el límite, no
sobre todo el ingreso.

    Tramo 1: de 0 a 10.000.000            -> 0 %
    Tramo 2: de 10.000.000 a 30.000.000   -> 10 % sobre lo que pase de 10 millones
    Tramo 3: más de 30.000.000            -> 20 % sobre lo que pase de 30 millones,
                                             más los 2.000.000 del tramo 2 completo

Ejemplos:
    20.000.000 -> (20M - 10M) * 10 %                  = 1.000.000
    40.000.000 -> 2.000.000 + (40M - 30M) * 20 %      = 4.000.000

Completa impuesto(ingreso). Si el ingreso es negativo, lanza un error con:
    raise ValueError("El ingreso no puede ser negativo")

Pista: en Python puedes escribir 10_000_000 para que el número sea legible.

Conceptos: condicionales en cascada, límites, raise.
"""


def impuesto(ingreso):
    # Escribe tu solución aquí
    pass


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
