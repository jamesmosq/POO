from abc import ABC, abstractmethod


# Clase abstracta
class AplicacionMovil(ABC):
    def __init__(self, nombre, version, tamano, rating,versionN):
        self.nombre = nombre
        self.version = version
        self.tamano = tamano
        self.rating = rating
        self.versionN = versionN

    @abstractmethod
    def instalar(self):
        pass

    @abstractmethod
    def ejecutar(self):
        pass

    @abstractmethod
    def mostrar_interfaz(self):
        pass

    @abstractmethod
    def actualizar(self):
        print(f"Actualizando {self.nombre} a la versión {self.version}")

# App de juego
class AppJuego(AplicacionMovil):
    def instalar(self):
        print(f"Instalando juego {self.nombre}")

    def ejecutar(self):
        print(f"Ejecutando juego {self.nombre}")

    def mostrar_interfaz(self):
        print("Interfaz de juego: [JUGAR] [PAUSA] [SALIR]")

    def actualizar(self):
        print(f"Actualizando juego {self.nombre} a la versión {self.version}")


# App de red social
class AppRedSocial(AplicacionMovil):
    def instalar(self):
        print(f"Instalando red social {self.nombre}")

    def ejecutar(self):
        print(f"Ejecutando red social {self.nombre}")

    def mostrar_interfaz(self):
        print("Interfaz red social: [PERFIL] [AMIGOS] [PUBLICAR]")

    def actualizar(self):
        print(f"Actualizando red social {self.nombre} a la versión {self.version}")
class ProductividadApp(AplicacionMovil):
    def instalar(self):
        print(f"Instalando app de productividad {self.nombre}")

    def ejecutar(self):
        print(f"Ejecutando app de productividad {self.nombre}")

    def mostrar_interfaz(self):
        print("Interfaz de productividad: [TAREAS] [CALENDARIO] [NOTAS]")

    def actualizar(self):
        print(f"Actualizando de productividad {self.nombre} a la versión {self.version}")

class EntretenimientoApp(AplicacionMovil):
    def instalar(self):
        print(f"Instalando app de entretenimiento {self.nombre}")

    def ejecutar(self):
        print(f"Ejecutando app de entretenimiento {self.nombre}")

    def mostrar_interfaz(self):
        print("Interfaz de entretenimiento: [VIDEOS] [MÚSICA] [JUEGOS]")

    def actualizar(self):
        print(f"Actualizando de entretenimiento {self.nombre} a la versión {self.version} la nueva versión es {self.versionN}")


juego = AppJuego("Tetris", "1.0", 25, 4.5)
red_social = AppRedSocial("Facebook", "2.0", 100, 4.0)
productividad = ProductividadApp("TodoList", "1.0", 30, 4.8)
entretenimiento = EntretenimientoApp("Netflix", "3.0", 200, 4.9)

print("=== JUEGO ===")
juego.instalar()
juego.ejecutar()
juego.mostrar_interfaz()

print("\n=== RED SOCIAL ===")
red_social.instalar()
red_social.ejecutar()
red_social.mostrar_interfaz()

print("\n=== PRODUCTIVIDAD ===")
productividad.instalar()
productividad.ejecutar()
productividad.mostrar_interfaz()

print("\n=== ENTRETENIMIENTO ===")
entretenimiento.instalar()
entretenimiento.ejecutar()
entretenimiento.mostrar_interfaz()