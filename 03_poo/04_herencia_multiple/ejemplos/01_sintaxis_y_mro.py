"""
Ejemplo 01 - Sintaxis de la herencia múltiple y el MRO

Una clase puede heredar de varias clases a la vez:

    class Hija(Padre1, Padre2):
        ...

La hija recibe los atributos y métodos de TODOS sus padres. Cuando busca un
método, Python sigue un orden fijo llamado MRO (Method Resolution Order,
orden de resolución de métodos): primero la propia clase, luego los padres
de izquierda a derecha, y al final object.
"""


class Volador:
    def volar(self):
        return "Estoy volando"

    def moverse(self):
        return "Me muevo volando"


class Nadador:
    def nadar(self):
        return "Estoy nadando"

    def moverse(self):
        return "Me muevo nadando"


class Pato(Volador, Nadador):
    """Un pato vuela y nada: hereda de las dos clases."""

    def graznar(self):
        return "Cuac"


pato = Pato()

# 1. La hija tiene los métodos de los dos padres y los suyos.
print(pato.volar())
print(pato.nadar())
print(pato.graznar())

# 2. Los dos padres definen moverse(). ¿Cuál se usa?
#    El del primer padre en la lista: Volador.
print(pato.moverse())  # Me muevo volando

# 3. El MRO se puede consultar de dos formas:
#    Clase.mro()    -> retorna una LISTA
#    Clase.__mro__  -> es una TUPLA (un atributo, sin paréntesis)
print(Pato.mro())
print(Pato.__mro__)
print([clase.__name__ for clase in Pato.mro()])  # ['Pato', 'Volador', 'Nadador', 'object']

# 4. Si se invierte el orden de los padres, cambia el MRO y cambia el resultado.
class PatoNadadorPrimero(Nadador, Volador):
    pass


print(PatoNadadorPrimero().moverse())  # Me muevo nadando

# 5. isinstance funciona con cualquiera de los padres.
print(isinstance(pato, Volador), isinstance(pato, Nadador))  # True True

# 6. ¿En qué clase está definido realmente un método?
#    Se recorre el MRO y se busca en el __dict__ de cada clase.
for clase in Pato.mro():
    if "moverse" in clase.__dict__:
        print(f"moverse() se toma de {clase.__name__}")
        break
