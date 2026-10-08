"""
Solución - Ejercicio para corregir 05 - Catálogo con lambdas

CORRECCIÓN 1: p[1] * porcentaje / 100 calcula cuánto se descuenta, no el
precio final. El precio rebajado es p[1] * (1 - porcentaje / 100).

CORRECCIÓN 2: p[0] es el nombre; ordenaba alfabéticamente. El precio está
en la posición 1.

CORRECCIÓN 3: el enunciado pide "menor o igual", así que es <=. Con < se
perdía el producto que cuesta exactamente el límite.
"""

def aplicar_descuento(productos, porcentaje):
    return list(map(lambda p: p[1] * (1 - porcentaje / 100), productos))  # CORRECCIÓN 1


def ordenar_por_precio(productos):
    return sorted(productos, key=lambda p: p[1])  # CORRECCIÓN 2


def filtrar_baratos(productos, limite):
    return list(filter(lambda p: p[1] <= limite, productos))  # CORRECCIÓN 3


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    catalogo = [("Teclado", 80000), ("Mouse", 30000), ("Audífonos", 50000)]

    assert aplicar_descuento(catalogo, 10) == [72000, 27000, 45000], aplicar_descuento(catalogo, 10)
    assert ordenar_por_precio(catalogo) == [("Mouse", 30000), ("Audífonos", 50000), ("Teclado", 80000)]
    assert filtrar_baratos(catalogo, 50000) == [("Mouse", 30000), ("Audífonos", 50000)]

    print("Todas las pruebas pasaron")
