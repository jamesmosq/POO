"""
Módulo auxiliar del ejercicio para corregir 03.
Calcula impuestos con las tasas definidas en TASAS.
"""

TASAS = {"iva": 19, "consumo": 8}


def calcular_impuesto(valor, tipo):
    return valor * TASAS[tipo] / 100


# Prueba rápida del módulo
TASAS["iva"] = 0
print("Prueba de impuestos:", calcular_impuesto(1000, "iva"))
