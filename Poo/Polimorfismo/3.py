class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

class Pato( Animal):
    def hacer_sonido(self):
        return "Cuak"
# Mismo método, diferentes comportamientos
animales = [Perro(), Gato(),Pato()]
for animal in animales:
    print(animal.hacer_sonido())

print("-" * 50)

class Vehiculo:
    def arrancar(self):
        return "🚙 El vehículo arranca"

class Coche(Vehiculo):
    def arrancar(self):
        return "🚗 El coche arranca con llave"

class Moto(Vehiculo):
    def arrancar(self):
        return "🏍️ La moto arranca con botón"

# Uso polimórfico
vehiculos = [Coche(), Moto()]
for vehiculo in vehiculos:
    print(vehiculo.arrancar())

print("-" * 25)
print("-" * 25)