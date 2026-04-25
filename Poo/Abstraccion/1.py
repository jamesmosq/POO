# EJEMPLO 1: CLASE ABSTRACTA BÁSICA - ANIMALES
# ==============================================

from abc import ABC, abstractmethod


class Animal(ABC):
    """Clase abstracta que define la estructura básica de un animal"""

    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def hacer_sonido(self):
        """Método abstracto - DEBE ser implementado por las subclases"""
        pass

    @abstractmethod
    def moverse(self):
        """Método abstracto - DEBE ser implementado por las subclases"""
        pass

    # Método concreto - puede ser usado directamente
    def dormir(self):
        print(f"{self.nombre} está durmiendo... 😴")


# Subclases que implementan los métodos abstractos
class Perro(Animal):
    def hacer_sonido(self):
        return f"{self.nombre} dice: ¡Guau!"

    def moverse(self):
        return f"{self.nombre} corre con cuatro patas"


class Pajaro(Animal):
    def hacer_sonido(self):
        return f"{self.nombre} dice: ¡Pío pío!"

    def moverse(self):
        return f"{self.nombre} vuela con sus alas"


# USO DEL EJEMPLO 1
print("=" * 50)
print("EJEMPLO 1: ANIMALES")
print("=" * 50)

# Crear instancias
perro = Perro("Max")
pajaro = Pajaro("Tweety")

# Usar métodos abstractos implementados
print(perro.hacer_sonido())
print(perro.moverse())
perro.dormir()

print()
print(pajaro.hacer_sonido())
print(pajaro.moverse())
pajaro.dormir()

# Esto daría ERROR - no se puede instanciar una clase abstracta:
# animal = Animal("Genérico")  # TypeError!

print("\n" + "=" * 50)


# EJEMPLO 2: CALCULADORA ABSTRACTA
# ================================

class Calculadora(ABC):
    """Clase abstracta para diferentes tipos de calculadoras"""

    @abstractmethod
    def sumar(self, a, b):
        pass

    @abstractmethod
    def restar(self, a, b):
        pass

    # Método concreto compartido
    def mostrar_resultado(self, operacion, a, b, resultado):
        print(f"{operacion}: {a} y {b} = {resultado}")


class CalculadoraBasica(Calculadora):
    """Calculadora que solo hace operaciones básicas"""

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b


class CalculadoraCientifica(Calculadora):
    """Calculadora con funciones adicionales"""

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def potencia(self, base, exponente):
        return base ** exponente


# USO DEL EJEMPLO 2
print("EJEMPLO 2: CALCULADORAS")
print("=" * 50)

calc_basica = CalculadoraBasica()
calc_cientifica = CalculadoraCientifica()

# Usar métodos abstractos
resultado1 = calc_basica.sumar(5, 3)
calc_basica.mostrar_resultado("Suma básica", 5, 3, resultado1)

resultado2 = calc_cientifica.restar(10, 4)
calc_cientifica.mostrar_resultado("Resta científica", 10, 4, resultado2)

# Método adicional de la calculadora científica
resultado3 = calc_cientifica.potencia(2, 3)
print(f"Potencia: 2^3 = {resultado3}")

print("\n" + "=" * 50)


# EJEMPLO 3: FIGURAS GEOMÉTRICAS
# ===============================

class Figura(ABC):
    """Clase abstracta para figuras geométricas"""

    def __init__(self, color="sin color"):
        self.color = color

    @abstractmethod
    def area(self):
        """Calcular el área - debe ser implementado"""
        pass

    @abstractmethod
    def perimetro(self):
        """Calcular el perímetro - debe ser implementado"""
        pass

    # Método concreto
    def pintar(self, nuevo_color):
        self.color = nuevo_color
        print(f"Figura pintada de color {self.color}")


class Rectangulo(Figura):
    def __init__(self, ancho, alto, color="sin color"):
        super().__init__(color)
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)


class Circulo(Figura):
    def __init__(self, radio, color="sin color"):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return 3.14159 * (self.radio ** 2)

    def perimetro(self):
        return 2 * 3.14159 * self.radio


# USO DEL EJEMPLO 3
print("EJEMPLO 3: FIGURAS GEOMÉTRICAS")
print("=" * 50)

rectangulo = Rectangulo(5, 3, "azul")
circulo = Circulo(4, "rojo")

print(f"Rectángulo {rectangulo.color}:")
print(f"  Área: {rectangulo.area()}")
print(f"  Perímetro: {rectangulo.perimetro()}")

print(f"\nCírculo {circulo.color}:")
print(f"  Área: {circulo.area():.2f}")
print(f"  Perímetro: {circulo.perimetro():.2f}")

# Cambiar color usando método concreto
rectangulo.pintar("verde")

print("\n" + "=" * 50)


# EJEMPLO 4: PROCESADOR DE ARCHIVOS
# ==================================

class ProcesadorArchivo(ABC):
    """Clase abstracta para procesar diferentes tipos de archivos"""

    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    @abstractmethod
    def leer(self):
        """Leer el archivo - implementación específica por tipo"""
        pass

    @abstractmethod
    def escribir(self, contenido):
        """Escribir al archivo - implementación específica por tipo"""
        pass

    # Método concreto para todas las subclases
    def mostrar_info(self):
        print(f"Procesando archivo: {self.nombre_archivo}")


class ProcesadorTexto(ProcesadorArchivo):
    def leer(self):
        return f"Leyendo texto plano de {self.nombre_archivo}"

    def escribir(self, contenido):
        return f"Escribiendo texto '{contenido}' en {self.nombre_archivo}"


class ProcesadorJSON(ProcesadorArchivo):
    def leer(self):
        return f"Parseando JSON de {self.nombre_archivo}"

    def escribir(self, contenido):
        return f"Serializando a JSON '{contenido}' en {self.nombre_archivo}"


# USO DEL EJEMPLO 4
print("EJEMPLO 4: PROCESADORES DE ARCHIVO")
print("=" * 50)

proc_texto = ProcesadorTexto("documento.txt")
proc_json = ProcesadorJSON("datos.json")

# Usar métodos
proc_texto.mostrar_info()
print(proc_texto.leer())
print(proc_texto.escribir("Hola mundo"))

print()
proc_json.mostrar_info()
print(proc_json.leer())
print(proc_json.escribir({"nombre": "Juan", "edad": 30}))

print("\n" + "=" * 50)


# EJEMPLO 5: VEHÍCULOS SIMPLE
# ============================

class Vehiculo(ABC):
    """Ejemplo muy simple de vehículo abstracto"""

    def __init__(self, marca):
        self.marca = marca

    @abstractmethod
    def arrancar(self):
        pass

    @abstractmethod
    def detener(self):
        pass


class Coche(Vehiculo):
    def arrancar(self):
        return f"El coche {self.marca} arranca con llave"

    def detener(self):
        return f"El coche {self.marca} se detiene con frenos"


class Bicicleta(Vehiculo):
    def arrancar(self):
        return f"La bicicleta {self.marca} arranca pedaleando"

    def detener(self):
        return f"La bicicleta {self.marca} se detiene con frenos de mano"


# USO DEL EJEMPLO 5
print("EJEMPLO 5: VEHÍCULOS SIMPLE")
print("=" * 50)

coche = Coche("Toyota")
bici = Bicicleta("Trek")

print(coche.arrancar())
print(coche.detener())
print()
print(bici.arrancar())
print(bici.detener())

print("\n" + "=" * 50)

# DEMOSTRACIÓN DE ERROR
# =====================
print("DEMOSTRACIÓN DE ERROR:")
print("=" * 50)

try:
    # Esto causará un TypeError porque Animal es abstracta
    animal = Animal("Genérico")
except TypeError as e:
    print(f"ERROR al intentar crear Animal directamente: {e}")


# Clase incompleta - falta implementar método abstracto
class GatoIncompleto(Animal):
    def hacer_sonido(self):
        return "Miau"
    # ¡Falta implementar moverse()!


try:
    # Esto también causará error porque no implementa todos los métodos abstractos
    gato_malo = GatoIncompleto("Michi")
except TypeError as e:
    print(f"ERROR al crear clase incompleta: {e}")

print("\n¡Los ejemplos funcionan correctamente! ✅")