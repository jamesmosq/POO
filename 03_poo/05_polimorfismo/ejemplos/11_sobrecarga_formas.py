
# 2. Polimorfismo de sobrecarga de métodos

from abc import ABC, abstractmethod


class Forma(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto


class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14159 * self.radio ** 2


# Usando el polimorfismo
formas = [Rectangulo(5, 3), Circulo(4)]

for forma in formas:
    print(f"Área: {forma.area()}")