"""
Ejercicio para corregir 02 - Lista de precios
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    - precio_de(precios, producto): retorna el precio; si el producto no
      existe, retorna 0.
    - reporte(precios): retorna una lista de textos "producto: $precio".

        precios = {"café": 3500, "té": 2800}
        precio_de(precios, "café")  -> 3500
        precio_de(precios, "jugo")  -> 0
        reporte(precios)            -> ["café: $3500", "té: $2800"]

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


def precio_de(precios, producto):
    return precios[producto]


def reporte(precios):
    lineas = []
    for producto, precio in precios:
        lineas.append(f"{producto}: ${precio}")
    return lineas


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    precios = {"café": 3500, "té": 2800}
    assert precio_de(precios, "café") == 3500
    assert precio_de(precios, "jugo") == 0
    assert reporte(precios) == ["café: $3500", "té: $2800"]

    print("Todas las pruebas pasaron")
