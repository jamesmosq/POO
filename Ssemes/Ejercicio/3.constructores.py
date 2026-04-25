class Ejemplo:
    def __new__(cls, *args, **kwargs):
        print("1. Se llama a __new__")
        # Crea y retorna la nueva instancia
        instance = super().__new__(cls)
        return instance

    def __init__(self, valor):
        print("2. Se llama a __init__")
        self.valor = valor

# Uso
obj = Ejemplo(42)
print(f"3. Objeto creado con valor: {obj.valor}")

# Ejemplo de Singleton usando __new__
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creando la instancia de Singleton")
            cls._instance = super().__new__(cls)
        return cls._instance

# Uso del Singleton
s1 = Singleton()
s2 = Singleton()
print(f"¿Son el mismo objeto?: {s1 is s2}")