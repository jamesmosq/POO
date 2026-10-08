from abc import ABC, abstractmethod


class Forma(ABC):
    """Clase abstracta que define la interfaz para formas geométricas"""

    @abstractmethod
    def calcular_area(self):
        """Método abstracto que debe ser implementado por las subclases"""
        pass

    @abstractmethod
    def calcular_perimetro(self):
        """Método abstracto que debe ser implementado por las subclases"""
        pass

    def mostrar_info(self):
        """Método concreto que puede ser usado por todas las subclases"""
        print(f"Forma: {self.__class__.__name__}")
        print(f"Área: {self.calcular_area()}")
        print(f"Perímetro: {self.calcular_perimetro()}")


class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)


class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
        self.pi = 3.14159

    def calcular_area(self):
        return self.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * self.pi * self.radio


class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        # Asumiendo un triángulo equilátero para simplificar
        return 3 * self.base


# Uso
rectangulo = Rectangulo(5, 3)
circulo = Circulo(4)
triangulo = Triangulo(6, 4)

print("Información del rectángulo:")
rectangulo.mostrar_info()

print("\nInformación del círculo:")
circulo.mostrar_info()

print("\nInformación del triángulo:")
triangulo.mostrar_info()

# Esto causaría un error: TypeError: Can't instantiate abstract class
# forma = Forma()  # ¡No se puede instanciar!
