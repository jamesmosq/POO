"""
Solución - Ejercicio para corregir 03 - Usar un módulo propio

CORRECCIÓN 1 (en impuestos.py): el módulo tenía código de prueba suelto al
final. Ese código se ejecuta CADA VEZ que alguien importa el módulo: ponía
el IVA en 0 e imprimía un mensaje. Las pruebas de un módulo van dentro de
if __name__ == "__main__":. Revisa impuestos.py en esta carpeta.

CORRECCIÓN 2 (ImportError: cannot import name 'calcular_iva'): el módulo
no tiene ninguna función con ese nombre. La función es calcular_impuesto y
recibe el tipo de impuesto.
"""

from impuestos import calcular_impuesto  # CORRECCIÓN 2


def total_con_iva(valor):
    return valor + calcular_impuesto(valor, "iva")  # CORRECCIÓN 2


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import impuestos

    assert impuestos.TASAS == {"iva": 19, "consumo": 8}, f"Las tasas cambiaron al importar: {impuestos.TASAS}"
    assert total_con_iva(1000) == 1190.0, total_con_iva(1000)

    print("Todas las pruebas pasaron")
