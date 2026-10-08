class altura:
    def alt(self):
        return f"esta es mi altura:6."

class base:
    def bas(self):
        return f"esta es mi base: 8."

class triangulo(altura,base):
    def _init_(self,color):
        self.color = color

    def color(self):
        return f"mi color es {self.color}."

mi_triangulo = triangulo("verde")
print(mi_triangulo.alt())
print(mi_triangulo.bas())
print(mi_triangulo.color())



class Altura:
    def alt(self):
        return "Esta es mi altura: 6"

class Base:
    def bas(self):
        return "Esta es mi base: 8"

class Triangulo(Altura, Base):
    def __init__(self, color):
        self.color = color

    def mostrar_color(self):
        return f"Mi color es {self.color}"

mi_triangulo = Triangulo("verde")
print(mi_triangulo.alt())
print(mi_triangulo.bas())
print(mi_triangulo.mostrar_color())