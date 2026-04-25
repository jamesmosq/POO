# 1. Polimorfismo de tiempo de ejecución (Duck Typing)

class Pato:
    def hablar(self):
        return "Cuac!"


class Perro:
    def hablar(self):
        return "Guau!"


class Gato:
    def hablar(self):
        return "Miau!"


def hacer_hablar(animal):
    print(animal.hablar())


# Usando el polimorfismo
pato = Pato()
perro = Perro()
gato = Gato()

hacer_hablar(pato)  # Salida: Cuac!
hacer_hablar(perro)  # Salida: Guau!
hacer_hablar(gato)  # Salida: Miau!
