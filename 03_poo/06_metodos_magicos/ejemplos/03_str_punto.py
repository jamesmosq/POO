"""
2.	__str__: En la clase Punto, definimos __str__ para dar una representación en cadena del punto.
Esto nos permite imprimir el punto directamente y obtener una representación legible.
"""

# 2. __str__
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


punto = Punto('ana', 4)
print(punto)  # Salida: (3, 4)