"""
Solución - Ejercicio propuesto 02 - Figuras geométricas
"""
import math


class Figura:
    def __init__(self, nombre):
        self.nombre = nombre

    def area(self):
        return 0

    def describir(self):
        # self.area() llama a la versión de la clase hija: por eso este método
        # se escribe una sola vez y sirve para todas las figuras.
        return f"{self.nombre} con área {self.area():.2f}"


class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2


class Cuadrado(Rectangulo):
    def __init__(self, lado):
        # Un cuadrado es un rectángulo con base y altura iguales.
        super().__init__(lado, lado)
        self.nombre = "Cuadrado"


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert Figura("Genérica").area() == 0

    r = Rectangulo(4, 5)
    assert r.area() == 20
    assert r.describir() == "Rectángulo con área 20.00"

    c = Circulo(1)
    assert c.describir() == "Círculo con área 3.14"

    q = Cuadrado(3)
    assert q.area() == 9
    assert q.describir() == "Cuadrado con área 9.00"
    assert isinstance(q, Rectangulo), "Cuadrado debe heredar de Rectangulo"
    assert "area" not in Cuadrado.__dict__, "Cuadrado no debe redefinir area()"

    print("Todas las pruebas pasaron")
