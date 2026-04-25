"""
 Ejercicio 5: Comidas
Situación: Un restaurante sirve pizzas, hamburguesas, ensaladas y postres.
Tu tarea:
•	Piensa: ¿qué tiene en común cualquier comida?
•	¿Qué acciones se hacen con cualquier platillo?
•	Crea clase abstracta Comida con:
o	Atributos: nombre, precio, ingredientes, tiempo_preparacion
o	Métodos abstractos: preparar(), calcular_calorias()
•	Implementa Pizza e Hamburguesa
Pista: Toda comida se prepara y tiene cierto contenido calórico.

"""

from abc import ABC, abstractmethod


class Comida(ABC):
    def __init__(self, nombre, precio, ingredientes, tiempo_preparacion):
        self.nombre = nombre
        self.precio = precio
        self.ingredientes = ingredientes
        self.tiempo_preparacion = tiempo_preparacion

    @abstractmethod
    def preparar(self):
        pass

    @abstractmethod
    def calcular_calorias(self):
        pass


class Pizza(Comida):
    def __init__(self, nombre, precio, ingredientes, tiempo_preparacion, tipo_masa):
        super().__init__(nombre, precio, ingredientes, tiempo_preparacion)
        self.tipo_masa = tipo_masa

    def preparar(self):
        return f"Preparando la pizza {self.nombre} con masa {self.tipo_masa}."

    def calcular_calorias(self):
        calorias = 200 + len(self.ingredientes) * 50  # Ejemplo simple de cálculo
        return f"La pizza {self.nombre} tiene aproximadamente {calorias} calorías."


class Hamburguesa(Comida):
    def __init__(self, nombre, precio, ingredientes, tiempo_preparacion, tipo_pan):
        super().__init__(nombre, precio, ingredientes, tiempo_preparacion)
        self.tipo_pan = tipo_pan

    def preparar(self):
        return f"Preparando la hamburguesa {self.nombre} con pan {self.tipo_pan}."

    def calcular_calorias(self):
        calorias = 300 + len(self.ingredientes) * 40  # Ejemplo simple de cálculo
        return f"La hamburguesa {self.nombre} tiene aproximadamente {calorias} calorías."


h1 = Hamburguesa("Cheeseburger", 8.99, ["carne", "queso", "lechuga"], 10, "sesame")
p1 = Pizza("Margarita", 10.99, ["tomate", "queso", "albahaca"], 15, "delgada")

print("=== Hamburguesa ===")
print(h1.preparar())
print(h1.calcular_calorias())

print("")

print("=== Pizza ===")
print(p1.preparar())
print(p1.calcular_calorias())
