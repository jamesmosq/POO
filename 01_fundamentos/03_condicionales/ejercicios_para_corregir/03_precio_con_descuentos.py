"""
Ejercicio para corregir 03 - Precio con descuentos
Nivel: intermedio
Errores a encontrar: 2

Qué debería hacer el programa:
    Calcular el precio final de una compra con descuentos que se SUMAN:
        - Los socios tienen 10 %.
        - El cupón "PROMO20" da 20 % adicional.
        - El cupón "PROMO5" da 5 % adicional.
    El cupón puede escribirse en mayúsculas o minúsculas.

        precio_final(100000, True, "PROMO20")  -> 70000.0  (10 % + 20 %)
        precio_final(100000, False, "promo5")  -> 95000.0
        precio_final(100000, True, "")         -> 90000.0

Ojo: el programa no lanza errores, pero da resultados incorrectos.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


def precio_final(precio, es_socio, cupon):
    descuento = 0
    if es_socio:
        descuento = 10
    if cupon == "PROMO20":
        descuento = 20
    elif cupon == "PROMO5":
        descuento = 5
    return precio * (1 - descuento / 100)


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert precio_final(100000, True, "") == 90000
    assert precio_final(100000, False, "PROMO20") == 80000
    assert precio_final(100000, True, "PROMO20") == 70000, "Los descuentos se suman"
    assert precio_final(100000, False, "promo5") == 95000, "El cupón no distingue mayúsculas"
    assert precio_final(100000, False, "OTRO") == 100000

    print("Todas las pruebas pasaron")
