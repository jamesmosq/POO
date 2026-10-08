from abc import ABC,abstractmethod

class Eletrodomestico(ABC):
    def __init__(self,marca,modelo,consumoEnergia):
        self.marca = marca
        self.modelo = modelo
        self.consumoEnergia = consumoEnergia


    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

    @abstractmethod
    def usar(self):
        pass

class Lavadora(Eletrodomestico):
    def encender(self):
        return f" La lavadora {self.marca} y de modelo {self.modelo} se ha encendido."

    def apagar(self):
        return f" La lavadora {self.marca} y de modelo {self.modelo} se ha apagado."

    def usar(self):
        return f" La lavadora {self.marca} y de modelo {self.modelo} se está usando para lavar la ropa."
class Refrigerador(Eletrodomestico):
    def encender(self):
        return f" El refrigerador {self.marca} y de modelo {self.modelo} se ha encendido."

    def apagar(self):
        return f" El refrigerador {self.marca} y de modelo {self.modelo} se ha apagado."

    def usar(self):
        return f" El refrigerador {self.marca} y de modelo {self.modelo} se está usando para enfriar los alimentos."

r1 = Refrigerador("Samsung", "RT38K5032S8", 200)
l1 = Lavadora("LG", "TWINWash", 1500)

print(" ====== Refrigerador ====== ")
print(r1.encender())
print(r1.usar())
print(r1.apagar())

print(" ")
print(" ====== Lavadora ====== ")
print(l1.encender())
print(l1.usar())
print(l1.apagar())