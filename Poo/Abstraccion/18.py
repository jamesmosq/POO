from abc import ABC, abstractmethod

class Instrumentos_Musicales(ABC):
    def __init__(self, nombre, material, tipo, marca, precio):
        self.nombre = nombre
        self.material = material
        self.tipo = tipo
        self.marca = marca
        self.precio = precio

    @abstractmethod
    def tocar(self):
        pass

    @abstractmethod
    def afinar(self):
        pass

    @abstractmethod
    def comprar(self):
        pass


class guitarra(Instrumentos_Musicales):
    def __init__(self, nombre, material, tipo, marca, precio):
        super().__init__(nombre, material, tipo, marca, precio)


    def tocar(self):
        return f"Tocando la guitarra {self.nombre} de marca {self.marca}"

    def afinar(self):
        return f"Afinando la guitarra {self.nombre}"

    def comprar(self):
        return f"Comprando la guitarra {self.nombre} por {self.precio} dólares"

g1 = guitarra("Gibson Les Paul", "Madera", "Eléctrica", "Gibson", 2500)
print(g1.tocar())

g1 = guitarra("Fender Stratocaster", "Madera", "Eléctrica", "Fender", 1500)
print(g1.afinar())

class piano(Instrumentos_Musicales):
    def __init__(self, nombre, material, tipo, marca, precio):
        super().__init__(nombre, material, tipo, marca, precio)

    def tocar(self):
        return f"Tocando el piano {self.nombre} de marca {self.marca}"

    def afinar(self):
        return f"Afinando el piano {self.nombre}"

    def comprar(self):
        return f"Comprando el piano {self.nombre} por {self.precio} dólares"

    def escuchando(self):
        return f"Escuchando el sonido del piano {self.nombre}"

p1 = piano("Yamaha U1", "Madera", "Acústico", "Yamaha", 5000)
p2= piano("Steinway & Sons Model D", "Madera", "Acústico", "Steinway", 150000)
print(p1.tocar())
print(p2.afinar())