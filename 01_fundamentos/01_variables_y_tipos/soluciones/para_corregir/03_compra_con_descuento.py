"""
Solución - Ejercicio para corregir 03 - Compra con descuento

CORRECCIÓN 1 (TypeError: unsupported operand type(s) for -: 'str' and
'str'): precio es texto. "15000" * 2 no falla, pero repite el texto
("1500015000"), y el error aparece más adelante, al restar. Hay que
convertir el texto a número antes de operar.

CORRECCIÓN 2 (resultado incorrecto): total * 10 multiplica por 10, no
calcula el 10 %. El 10 % es total * 10 / 100 (o total * 0.10).
"""

precio = int("15000")  # CORRECCIÓN 1
cantidad = 2

total = precio * cantidad
descuento = total * 10 / 100  # CORRECCIÓN 2
total_con_descuento = total - descuento

print("Total con descuento:", total_con_descuento)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert total == 30000, f"total vale {total!r}"
    assert total_con_descuento == 27000, f"total_con_descuento vale {total_con_descuento!r}"

    print("Todas las pruebas pasaron")
