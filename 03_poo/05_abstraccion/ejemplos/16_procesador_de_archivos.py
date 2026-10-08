
from abc import ABC, abstractmethod
import math

print("\n" + "=" * 60)
print("EJEMPLO 3: PROCESADORES DE ARCHIVOS")
print("=" * 60)


class ProcesadorArchivo(ABC):
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.datos = []

    # Método concreto - mismo para todos
    def obtener_info_archivo(self):
        return f"Procesando: {self.nombre_archivo}"

    # Métodos abstractos - cada tipo de archivo se procesa diferente
    @abstractmethod
    def leer_archivo(self):
        """Cada procesador debe saber leer su tipo de archivo"""
        pass

    @abstractmethod
    def validar_datos(self):
        """Cada procesador debe validar según su formato"""
        pass

    @abstractmethod
    def procesar_datos(self):
        """Cada procesador debe procesar según su tipo"""
        pass


class ProcesadorCSV(ProcesadorArchivo):
    def leer_archivo(self):
        # Simulación de lectura CSV
        self.datos = [
            ["Juan", "25", "Ingeniero"],
            ["Ana", "30", "Doctora"],
            ["Carlos", "28", "Profesor"]
        ]
        return f"CSV leído: {len(self.datos)} filas"

    def validar_datos(self):
        errores = []
        for i, fila in enumerate(self.datos):
            if len(fila) != 3:
                errores.append(f"Fila {i + 1}: número incorrecto de columnas")
        return "Datos válidos" if not errores else f"Errores: {errores}"

    def procesar_datos(self):
        resultado = []
        for fila in self.datos:
            persona = {
                'nombre': fila[0],
                'edad': int(fila[1]),
                'profesion': fila[2]
            }
            resultado.append(persona)
        return f"Procesados {len(resultado)} registros de personas"


class ProcesadorJSON(ProcesadorArchivo):
    def leer_archivo(self):
        # Simulación de lectura JSON
        self.datos = {
            "productos": [
                {"id": 1, "nombre": "Laptop", "precio": 1200},
                {"id": 2, "nombre": "Mouse", "precio": 25}
            ]
        }
        return f"JSON leído: {len(self.datos['productos'])} productos"

    def validar_datos(self):
        productos = self.datos.get('productos', [])
        for producto in productos:
            required_fields = ['id', 'nombre', 'precio']
            if not all(field in producto for field in required_fields):
                return "Faltan campos requeridos en productos"
        return "Estructura JSON válida"

    def procesar_datos(self):
        productos = self.datos['productos']
        total_valor = sum(p['precio'] for p in productos)
        return f"Inventario procesado: ${total_valor} en {len(productos)} productos"


# Demostración
procesadores = [
    ProcesadorCSV("empleados.csv"),
    ProcesadorJSON("inventario.json")
]

print("PROCESANDO ARCHIVOS CON MÉTODOS ABSTRACTOS:")
for procesador in procesadores:
    print(f"\n{procesador.obtener_info_archivo()}")
    print(f"  1. {procesador.leer_archivo()}")
    print(f"  2. {procesador.validar_datos()}")
    print(f"  3. {procesador.procesar_datos()}")