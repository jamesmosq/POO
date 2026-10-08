"""
Solución - Ejercicio propuesto 03 - Factura simple
"""

precio_unitario = 12500
cantidad = 3
PORCENTAJE_IVA = 19

subtotal = precio_unitario * cantidad
iva = subtotal * PORCENTAJE_IVA / 100
total = subtotal + iva

# :,.2f -> separador de miles y dos decimales
print(f"Subtotal: ${subtotal:,.2f}")
print(f"IVA:      ${iva:,.2f}")
print(f"Total:    ${total:,.2f}")


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert subtotal == 37500, f"subtotal vale {subtotal}"
    assert iva == 7125, f"iva vale {iva}"
    assert total == 44625, f"total vale {total}"

    print("Todas las pruebas pasaron")
