"""
Solución - Ejercicio para corregir 02 - Áreas con if

CORRECCIÓN 1 (NameError: name 'radio' is not defined): dentro del método,
el radio del objeto es self.radio.

CORRECCIÓN 2 (el cuadrado no se sumaba): type(figura) == Rectangulo es
False para un Cuadrado, aunque herede de Rectangulo. Además, cada nueva
figura obligaría a agregar otro elif. La solución es eliminar los if y
llamar a figura.area(): cada objeto sabe calcular su propia área. Eso es
polimorfismo.
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
        return 3.1416 * self.radio ** 2  # CORRECCIÓN 1


def area_total(figuras):
    return sum(figura.area() for figura in figuras)  # CORRECCIÓN 2


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    figuras = [Rectangulo(2, 3), Cuadrado(2), Circulo(1)]
    assert round(area_total(figuras), 2) == 13.14, round(area_total(figuras), 2)

    print("Todas las pruebas pasaron")
