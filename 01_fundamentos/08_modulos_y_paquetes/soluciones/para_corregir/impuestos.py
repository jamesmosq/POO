"""
Módulo auxiliar del ejercicio para corregir 03 (versión corregida).
Calcula impuestos con las tasas definidas en TASAS.
"""

TASAS = {"iva": 19, "consumo": 8}


def calcular_impuesto(valor, tipo):
    return valor * TASAS[tipo] / 100


# CORRECCIÓN 1: la prueba rápida va protegida para que no se ejecute al
# importar el módulo. Además, ya no modifica TASAS.
if __name__ == "__main__":
    print("Prueba de impuestos:", calcular_impuesto(1000, "iva"))
