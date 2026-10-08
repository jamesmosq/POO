"""
Solución - Ejercicio para corregir 02 - Lista de precios

CORRECCIÓN 1 (KeyError: 'jugo'): acceder con [] a una clave que no existe
lanza error. get(clave, valor_por_defecto) retorna el valor por defecto si
la clave no está.

CORRECCIÓN 2 (ValueError: too many values to unpack): recorrer un
diccionario directamente entrega solo las claves. Para recibir clave y
valor juntos se usa .items().
"""

def precio_de(precios, producto):
    return precios.get(producto, 0)  # CORRECCIÓN 1


def reporte(precios):
    lineas = []
    for producto, precio in precios.items():  # CORRECCIÓN 2
        lineas.append(f"{producto}: ${precio}")
    return lineas


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    precios = {"café": 3500, "té": 2800}
    assert precio_de(precios, "café") == 3500
    assert precio_de(precios, "jugo") == 0
    assert reporte(precios) == ["café: $3500", "té: $2800"]

    print("Todas las pruebas pasaron")
