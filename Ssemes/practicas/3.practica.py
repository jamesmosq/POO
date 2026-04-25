
# Ejemplo 3: Dispositivo electrónico multifunción
class Telefono:
    def llamar(self):
        return "Haciendo una llamada."

class Camara:
    def tomar_foto(self):
        return "Tomando una foto."

class Reproductor:
    def reproducir_musica(self):
        return "Reproduciendo música."

class SmartPhone(Telefono, Camara, Reproductor):
    def __init__(self, modelo):
        self.modelo = modelo

    def describir(self):
        return f"Soy un {self.modelo} con múltiples funciones."

# Uso del Ejemplo 3
mi_telefono = SmartPhone("iPhone 12")
print(mi_telefono.describir())
print(mi_telefono.llamar())
print(mi_telefono.tomar_foto())
print(mi_telefono.reproducir_musica())