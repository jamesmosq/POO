"""Descuentos de la tienda."""


def aplicar_descuento(valor, porcentaje):
    if not 0 <= porcentaje <= 100:
        raise ValueError("El porcentaje debe estar entre 0 y 100")
    return valor - valor * porcentaje / 100
