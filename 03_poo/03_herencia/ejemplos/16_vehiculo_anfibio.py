# Primero, se definimos las clases
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mover(self):
        print(f"El {self.marca} {self.modelo} se está moviendo.")

class Acuatico:
    def nadar(self):
        print("Este vehículo puede nadar en el agua.")

class Terrestre:
    def conducir(self):
        print("Este vehículo puede conducirse en tierra.")

class VehiculoAnfibio(Vehiculo, Acuatico, Terrestre):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def mover_tierra_agua(self):
        print(f"El {self.marca} {self.modelo} puede moverse en tierra y agua.")

# Ahora, creamos una instancia de VehiculoAnfibio
anfibio = VehiculoAnfibio("AquaCar", "X2000")

# Llamamos a los diferentes métodos para ver cómo funciona la herencia múltiple
print("Demostracion de herencia multiple:")
print("---------------------------------")

# Método de la clase Vehiculo
anfibio.mover()

# Método de la clase Acuatico
anfibio.nadar()

# Método de la clase Terrestre
anfibio.conducir()

# Método propio de VehiculoAnfibio
anfibio.mover_tierra_agua()

# Demostramos que podemos acceder a los atributos heredados
print(f"\nDetalles del vehículo: {anfibio.marca} {anfibio.modelo}")

# Mostramos el MRO (Method Resolution Order)
print("\nOrden de resolución de métodos (MRO):")
print(VehiculoAnfibio.__mro__)

