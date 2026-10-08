"""
Ejemplo 02 - El problema del diamante

Se forma un "diamante" cuando dos clases heredan de una misma base y una
cuarta clase hereda de las dos:

                Clase1
               /      \\
          Clase2      Clase3
               \\      /
                Clase4

La pregunta es: si varias clases definen el mismo método, ¿cuál usa
Clase4? Python lo resuelve con el MRO, que en este caso es:

    Clase4 -> Clase2 -> Clase3 -> Clase1 -> object

Observa que Clase1 va al FINAL, después de sus dos hijas, aunque aparezca
"antes" en el dibujo. Python lo calcula con un algoritmo llamado
linealización C3, que garantiza dos cosas:
    - una clase siempre aparece antes que sus padres;
    - se respeta el orden en que se escribieron los padres.
"""


# Caso 1: el método está en los dos padres intermedios -> gana el primero.
class Clase1:
    def m(self):
        return "Clase1"


class Clase2(Clase1):
    def m(self):
        return "Clase2"


class Clase3(Clase1):
    def m(self):
        return "Clase3"


class Clase4(Clase2, Clase3):
    pass


print("Caso 1:", Clase4().m())  # Clase2
print("MRO:", [c.__name__ for c in Clase4.mro()])


# Caso 2: solo el padre de la DERECHA lo sobrescribe.
# Python no se detiene en Clase1 al revisar Clase2: primero mira Clase3,
# porque Clase1 va al final del MRO.
class B1:
    def m(self):
        return "B1"


class B2(B1):
    pass


class B3(B1):
    def m(self):
        return "B3"


class B4(B2, B3):
    pass


print("Caso 2:", B4().m())  # B3, no B1


# Caso 3: la clase de abajo también lo define -> gana ella.
# Aun así, se puede llamar la versión de un padre concreto escribiendo su
# nombre y pasando el objeto.
class C4(Clase2, Clase3):
    def m(self):
        return "C4"


objeto = C4()
print("Caso 3:", objeto.m())        # C4
print("  Clase2.m:", Clase2.m(objeto))  # Clase2
print("  Clase3.m:", Clase3.m(objeto))  # Clase3
print("  Clase1.m:", Clase1.m(objeto))  # Clase1


# Caso 4: ningún intermedio lo define -> se usa el de la base.
class D2(Clase1):
    pass


class D3(Clase1):
    pass


class D4(D2, D3):
    pass


print("Caso 4:", D4().m())  # Clase1
