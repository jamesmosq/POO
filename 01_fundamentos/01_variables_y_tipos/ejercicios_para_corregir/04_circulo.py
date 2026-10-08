"""
Ejercicio para corregir 04 - Área y perímetro de un círculo
Nivel: intermedio
Errores a encontrar: 3

Qué debería hacer el programa:
    Calcular el área (pi * r al cuadrado) y el perímetro (2 * pi * r) de un
    círculo de radio 5. El radio llega como texto, como lo entregaría input().

        area      -> 78.54  (redondeado a 2 decimales)
        perimetro -> 31.42  (redondeado a 2 decimales)

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""

PI = 3.1416
radio = "5"

area = round(PI * radio ^ 2, 2)
perimetro = round(2 * PI * Radio, 2)

print(f"Área: {area}")
print(f"Perímetro: {perimetro}")


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert area == 78.54, f"area vale {area}"
    assert perimetro == 31.42, f"perimetro vale {perimetro}"

    print("Todas las pruebas pasaron")
