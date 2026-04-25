from abc import ABC, abstractmethod


# Clase abstracta
class AplicacionMovil(ABC):
    def __init__(self, nombre, version, tamaño, rating):
        self.nombre = nombre
        self.version = version
        self.tamaño = tamaño
        self.rating = rating

    @abstractmethod
    def instalar(self):
        pass

    @abstractmethod
    def ejecutar(self):
        pass

    @abstractmethod
    def mostrar_interfaz(self):
        pass


# App de juego
class AppJuego(AplicacionMovil):
    def instalar(self):
        print(f"Instalando juego {self.nombre}")

    def ejecutar(self):
        print(f"Ejecutando juego {self.nombre}")

    def mostrar_interfaz(self):
        print("Interfaz de juego: [JUGAR] [PAUSA] [SALIR]")


# App de red social
class AppRedSocial(AplicacionMovil):
    def instalar(self):
        print(f"Instalando red social {self.nombre}")

    def ejecutar(self):
        print(f"Ejecutando red social {self.nombre}")

    def mostrar_interfaz(self):
        print("Interfaz red social: [PERFIL] [AMIGOS] [PUBLICAR]")

class Entretenimiento(AplicacionMovil):
    def instalar(self):
        print(f"Instalando app de entretenimiento {self.nombre}")

    def ejecutar(self):
        print(f"Ejecutando app de entretenimiento {self.nombre}")

    def mostrar_interfaz(self):
        print("Interfaz de entretenimiento: [VIDEOS] [MÚSICA] [JUEGOS]")


# Ejemplo
juego = AppJuego("Tetris", "1.0", 25, 4.5)
red_social = AppRedSocial("Facebook", "2.0", 100, 4.0)

print("=== JUEGO ===")
juego.instalar()
juego.ejecutar()
juego.mostrar_interfaz()

print("\n=== RED SOCIAL ===")
red_social.instalar()
red_social.ejecutar()
red_social.mostrar_interfaz()