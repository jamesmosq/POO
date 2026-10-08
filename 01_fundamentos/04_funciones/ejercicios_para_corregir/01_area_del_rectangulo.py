"""
Ejercicio para corregir 01 - Área del rectángulo
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    La función area_rectangulo(base, altura) retorna el área. El programa
    calcula el área de un rectángulo de 3 x 4 y la guarda en resultado.

        resultado -> 12

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""

resultado = area_rectangulo(3, 4)


def area_rectangulo(base, altura):
    print(base * altura)


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert area_rectangulo(2, 5) == 10, "La función debe RETORNAR el área"
    assert resultado == 12, f"resultado vale {resultado!r}"

    print("Todas las pruebas pasaron")
