"""
Solución - Ejercicio para corregir 04 - Área y perímetro de un círculo

CORRECCIÓN 1 (TypeError con str): radio llega como texto y hay que
convertirlo a número con float() antes de calcular.

CORRECCIÓN 2 (TypeError: unsupported operand type(s) for ^): en Python ^ no
es potencia, es el operador XOR de bits. La potencia se escribe **.

CORRECCIÓN 3 (NameError: name 'Radio' is not defined): la variable se llama
radio, en minúscula.
"""

PI = 3.1416
radio = float("5")  # CORRECCIÓN 1

area = round(PI * radio ** 2, 2)  # CORRECCIÓN 2
perimetro = round(2 * PI * radio, 2)  # CORRECCIÓN 3

print(f"Área: {area}")
print(f"Perímetro: {perimetro}")


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert area == 78.54, f"area vale {area}"
    assert perimetro == 31.42, f"perimetro vale {perimetro}"

    print("Todas las pruebas pasaron")
