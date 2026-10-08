# Ejemplo 2: Figura geométrica con características múltiples
class FiguraGeometrica:
    def describir(self):
        return "Soy una figura geométrica."

class Coloreable:
    def colorear(self, color):
        return f"Coloreado con {color}."

class Dibujable:
    def dibujar(self):
        return "Dibujando la figura."

class Cuadrado(FiguraGeometrica, Coloreable, Dibujable):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return f"Área: {self.lado ** 2}"

# Uso del Ejemplo 2
mi_cuadrado = Cuadrado(5)
print(mi_cuadrado.describir())
print(mi_cuadrado.colorear("rojo"))
print(mi_cuadrado.dibujar())
print(mi_cuadrado.area())
