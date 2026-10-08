"""
Solución - Ejercicio para corregir 01 - Tuplas e índices

CORRECCIÓN 1 (TypeError: 'tuple' object does not support item
assignment): las tuplas son inmutables; no se pueden cambiar después de
creadas. Se construye una tupla nueva con los valores calculados.

CORRECCIÓN 2 (IndexError: list index out of range): los índices van de 0 a
len - 1, así que notas[len(notas)] siempre está fuera de rango. El último
elemento es notas[-1] (o notas[len(notas) - 1]).
"""

def mover_en_x(punto, desplazamiento):
    x, y = punto
    return (x + desplazamiento, y)  # CORRECCIÓN 1


def ultima_nota(notas):
    return notas[-1]  # CORRECCIÓN 2


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    origen = (1, 2)
    assert mover_en_x(origen, 5) == (6, 2)
    assert origen == (1, 2)

    assert ultima_nota([3.0, 4.5, 4.0]) == 4.0
    assert ultima_nota([5]) == 5

    print("Todas las pruebas pasaron")
