"""
Ejercicio para corregir 01 - Importar math
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    perimetro_circulo(radio) retorna 2 * pi * radio, redondeado a 2
    decimales, usando la constante pi del módulo math.

        perimetro_circulo(1) -> 6.28

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""
import Math


def perimetro_circulo(radio):
    return round(2 * Math.PI * radio, 2)


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert perimetro_circulo(1) == 6.28
    assert perimetro_circulo(10) == 62.83

    print("Todas las pruebas pasaron")
