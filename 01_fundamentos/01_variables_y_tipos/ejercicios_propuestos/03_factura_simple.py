"""
Ejercicio propuesto 03 - Factura simple
Nivel: básico

Una tienda vende un producto con IVA del 19 %.

Requisitos:
1. Usa las variables precio_unitario, cantidad y PORCENTAJE_IVA.
2. Calcula:
       subtotal -> precio_unitario por cantidad
       iva      -> el 19 % del subtotal
       total    -> subtotal más iva
3. Imprime una factura como esta (usa f-strings y :,.2f para el formato):
       Subtotal: $37,500.00
       IVA:      $7,125.00
       Total:    $44,625.00

Pista: el 19 % de un valor es valor * 19 / 100.

Conceptos: operaciones aritméticas, constantes, formato de números.
"""

precio_unitario = 12500
cantidad = 3
PORCENTAJE_IVA = 19

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert subtotal == 37500, f"subtotal vale {subtotal}"
    assert iva == 7125, f"iva vale {iva}"
    assert total == 44625, f"total vale {total}"

    print("Todas las pruebas pasaron")
