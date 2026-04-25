from abc import ABC, abstractmethod

# 2. Abstracción con Propiedades Abstractas
class Vehiculo(ABC):
    """Abstracción de vehículo con propiedades y métodos abstractos"""

    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._velocidad = 0

    @property
    @abstractmethod
    def velocidad_maxima(self):
        """Propiedad abstracta para la velocidad máxima"""
        pass

    @property
    @abstractmethod
    def tipo_combustible(self):
        """Propiedad abstracta para el tipo de combustible"""
        pass

    @abstractmethod
    def acelerar(self, incremento):
        """Método abstracto para acelerar"""
        pass

    @abstractmethod
    def frenar(self, decremento):
        """Método abstracto para frenar"""
        pass

    def mostrar_estado(self):
        """Método concreto disponible para todas las subclases"""
        print(f"Vehículo: {self._marca} {self._modelo}")
        print(f"Velocidad actual: {self._velocidad} km/h")
        print(f"Velocidad máxima: {self.velocidad_maxima} km/h")
        print(f"Combustible: {self.tipo_combustible}")


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self._cilindrada = cilindrada

    @property
    def velocidad_maxima(self):
        return 180 + (self._cilindrada / 100)  # Velocidad basada en cilindrada

    @property
    def tipo_combustible(self):
        return "Gasolina"

    def acelerar(self, incremento):
        nueva_velocidad = self._velocidad + incremento
        if nueva_velocidad <= self.velocidad_maxima:
            self._velocidad = nueva_velocidad
            print(f"Acelerando a {self._velocidad} km/h")
        else:
            self._velocidad = self.velocidad_maxima
            print(f"Velocidad máxima alcanzada: {self._velocidad} km/h")

    def frenar(self, decremento):
        self._velocidad = max(0, self._velocidad - decremento)
        print(f"Frenando a {self._velocidad} km/h")


class BicicletaElectrica(Vehiculo):
    def __init__(self, marca, modelo, potencia_motor):
        super().__init__(marca, modelo)
        self._potencia_motor = potencia_motor  # en watts

    @property
    def velocidad_maxima(self):
        return min(45, 20 + (self._potencia_motor / 50))  # Limitada por ley

    @property
    def tipo_combustible(self):
        return "Eléctrico"

    def acelerar(self, incremento):
        nueva_velocidad = self._velocidad + incremento
        if nueva_velocidad <= self.velocidad_maxima:
            self._velocidad = nueva_velocidad
            print(f"Pedaleando con asistencia eléctrica: {self._velocidad} km/h")
        else:
            self._velocidad = self.velocidad_maxima
            print(f"Velocidad máxima de asistencia: {self._velocidad} km/h")

    def frenar(self, decremento):
        self._velocidad = max(0, self._velocidad - decremento)
        print(f"Frenando con regeneración: {self._velocidad} km/h")


# Uso
auto = Automovil("Toyota", "Corolla", 1600)
bici = BicicletaElectrica("Trek", "Verve+", 250)

print("=== Automóvil ===")
auto.mostrar_estado()
auto.acelerar(50)
auto.acelerar(100)  # Intentará superar el límite
auto.frenar(30)

print("\n=== Bicicleta Eléctrica ===")
bici.mostrar_estado()
bici.acelerar(20)
bici.acelerar(30)  # Intentará superar el límite
bici.frenar(10)