class A:
    def metodo(self):
        print("Método de A")

class B(A):
    def metodo(self):
        print("Método de B")

class C(A):
    def metodo(self):
        print("Método de C")

class D(B, C):
    pass

# Veamos el MRO de la clase D
print(D.mro())

# Creamos una instancia de D y llamamos al método
d = D()
d.metodo()

