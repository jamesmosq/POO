# Ejercicio 3: Creador de formas geométricas

from abc import ABC, abstractmethod
import math

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

class CreadorFormas:
    def crear_forma(self, tipo, *args):
        if tipo == "circulo":
            return Circulo(*args)
        elif tipo == "rectangulo":
            return Rectangulo(*args)
        else:
            raise ValueError("Tipo de forma no reconocido")

# Uso:
creador = CreadorFormas()
circulo = creador.crear_forma("circulo", 5)
rectangulo = creador.crear_forma("rectangulo", 4, 6)
print(circulo.area())     # 78.53981633974483
print(rectangulo.area())  # 24

