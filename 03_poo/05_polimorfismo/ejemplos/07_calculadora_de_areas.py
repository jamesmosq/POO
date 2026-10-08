# Ejercicio 2: Calculadora de áreas

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2


class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return 0.5 * self.base * self.altura


def imprimir_area(figura):
    print(f"El área es: {figura.calcular_area()}")


# Uso:
cuadrado = Cuadrado(5)
triangulo = Triangulo(4, 3)

imprimir_area(cuadrado)
imprimir_area(triangulo)


