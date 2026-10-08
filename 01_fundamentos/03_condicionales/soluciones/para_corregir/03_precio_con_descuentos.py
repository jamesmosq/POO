"""
Solución - Ejercicio para corregir 03 - Precio con descuentos

CORRECCIÓN 1: descuento = 20 reemplazaba el 10 % de socio en lugar de
sumarse. Para acumular se usa +=.

CORRECCIÓN 2: "promo5" no es igual a "PROMO5"; la comparación de textos
distingue mayúsculas. Se normaliza el cupón con .upper() antes de comparar.
"""

def precio_final(precio, es_socio, cupon):
    descuento = 0
    if es_socio:
        descuento += 10
    cupon = cupon.upper()  # CORRECCIÓN 2
    if cupon == "PROMO20":
        descuento += 20  # CORRECCIÓN 1
    elif cupon == "PROMO5":
        descuento += 5  # CORRECCIÓN 1
    return precio * (1 - descuento / 100)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert precio_final(100000, True, "") == 90000
    assert precio_final(100000, False, "PROMO20") == 80000
    assert precio_final(100000, True, "PROMO20") == 70000, "Los descuentos se suman"
    assert precio_final(100000, False, "promo5") == 95000, "El cupón no distingue mayúsculas"
    assert precio_final(100000, False, "OTRO") == 100000

    print("Todas las pruebas pasaron")
