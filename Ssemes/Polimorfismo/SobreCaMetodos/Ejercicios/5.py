# Ejercicio 5: Gestor de base de datos

class BaseDatos:
    def __init__(self):
        self.datos = {}

    def insertar(self, tabla, **kwargs):
        if tabla not in self.datos:
            self.datos[tabla] = []
        self.datos[tabla].append(kwargs)

    def buscar(self, tabla, **kwargs):
        if tabla not in self.datos:
            return []
        return [item for item in self.datos[tabla] if all(item.get(k) == v for k, v in kwargs.items())]

# Uso:
db = BaseDatos()
db.insertar("usuarios", nombre="Juan", edad=30)
db.insertar("usuarios", nombre="Ana", edad=25)
print(db.buscar("usuarios", nombre="Juan"))  # [{'nombre': 'Juan', 'edad': 30}]
print(db.buscar("usuarios", edad=25))        # [{'nombre': 'Ana', 'edad': 25}]