"""
Ejemplo 03 - Llamar a los padres por nombre o usar super()

En un diamante, cuando cada clase quiere ejecutar también el método de sus
padres, hay dos formas de hacerlo. Solo una es correcta.
"""


# FORMA 1 (problemática): llamar a cada padre por su nombre.
class Base:
    def iniciar(self):
        print("  Base.iniciar")


class Izquierda(Base):
    def iniciar(self):
        print("  Izquierda.iniciar")
        Base.iniciar(self)


class Derecha(Base):
    def iniciar(self):
        print("  Derecha.iniciar")
        Base.iniciar(self)


class Abajo(Izquierda, Derecha):
    def iniciar(self):
        print("  Abajo.iniciar")
        Izquierda.iniciar(self)
        Derecha.iniciar(self)


print("Llamando a los padres por nombre:")
Abajo().iniciar()
# Base.iniciar se ejecuta DOS veces, una por cada camino del diamante.
# Si Base abriera una conexión, cobrara un pago o sumara un contador, lo
# haría dos veces.


# FORMA 2 (correcta): super() en todas las clases.
class BaseS:
    def iniciar(self):
        print("  BaseS.iniciar")


class IzquierdaS(BaseS):
    def iniciar(self):
        print("  IzquierdaS.iniciar")
        super().iniciar()


class DerechaS(BaseS):
    def iniciar(self):
        print("  DerechaS.iniciar")
        super().iniciar()


class AbajoS(IzquierdaS, DerechaS):
    def iniciar(self):
        print("  AbajoS.iniciar")
        super().iniciar()


print("\nUsando super():")
AbajoS().iniciar()
# Cada método se ejecuta UNA vez, en el orden del MRO:
print("MRO:", [c.__name__ for c in AbajoS.mro()])

# Lo más importante: super() NO significa "mi padre". Significa "la
# siguiente clase en el MRO del objeto". Dentro de IzquierdaS, super()
# llevó a DerechaS (que no es su padre), porque el objeto es un AbajoS.
# Por eso funciona: cada clase le pasa el turno a la siguiente.
print("\nCon un objeto IzquierdaS solo, super() va directo a BaseS:")
IzquierdaS().iniciar()
