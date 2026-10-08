"""
Ejercicio para corregir 02 - Áreas con if
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    area_total(figuras) suma el área de cualquier lista de figuras. Hay
    rectángulos, cuadrados (que son rectángulos) y círculos.

        area_total([Rectangulo(2, 3), Cuadrado(2), Circulo(1)]) -> 13.14

Ojo: quien escribió area_total no aprovechó el polimorfismo. Uno de los
errores se arregla eliminando código, no agregándolo.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)


class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * radio ** 2


def area_total(figuras):
    total = 0
    for figura in figuras:
        if type(figura) == Rectangulo:
            total += figura.base * figura.altura
        elif type(figura) == Circulo:
            total += figura.area()
    return total


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    figuras = [Rectangulo(2, 3), Cuadrado(2), Circulo(1)]
    assert round(area_total(figuras), 2) == 13.14, round(area_total(figuras), 2)

    print("Todas las pruebas pasaron")
