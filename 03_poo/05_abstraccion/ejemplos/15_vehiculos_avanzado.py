from abc import ABC, abstractmethod
import random


# Clase base abstracta
class Vehiculo(ABC):
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.velocidad_actual = 0
        self.combustible_actual = 100  # Porcentaje de combustible

    @abstractmethod
    def acelerar(self, incremento):
        """Método abstracto para acelerar el vehículo"""
        pass

    @abstractmethod
    def frenar(self, decremento):
        """Método abstracto para frenar el vehículo"""
        pass

    @abstractmethod
    def calcular_consumo_combustible(self, distancia):
        """Método abstracto para calcular consumo de combustible por distancia"""
        pass

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"

    def obtener_info_basica(self):
        return {
            'vehiculo': str(self),
            'velocidad': self.velocidad_actual,
            'combustible': self.combustible_actual
        }


# Subclase Automóvil
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, num_puertas, tipo_combustible="Gasolina"):
        super().__init__(marca, modelo, año)
        self.num_puertas = num_puertas
        self.tipo_combustible = tipo_combustible
        self.velocidad_maxima = 180

        # Factor de eficiencia según tipo de combustible
        self.factor_eficiencia = {
            "Gasolina": 1.0,
            "Diesel": 0.8,
            "Híbrido": 0.6,
            "Eléctrico": 0.3
        }.get(tipo_combustible, 1.0)

    def acelerar(self, incremento):
        nueva_velocidad = min(self.velocidad_actual + incremento, self.velocidad_maxima)
        aceleracion_real = nueva_velocidad - self.velocidad_actual
        self.velocidad_actual = nueva_velocidad

        return {
            'accion': 'Aceleración',
            'incremento_solicitado': incremento,
            'aceleracion_real': aceleracion_real,
            'velocidad_actual': self.velocidad_actual,
            'mensaje': f"Automóvil acelerando suavemente a {self.velocidad_actual} km/h"
        }

    def frenar(self, decremento):
        nueva_velocidad = max(self.velocidad_actual - decremento, 0)
        frenado_real = self.velocidad_actual - nueva_velocidad
        self.velocidad_actual = nueva_velocidad

        return {
            'accion': 'Frenado',
            'decremento_solicitado': decremento,
            'frenado_real': frenado_real,
            'velocidad_actual': self.velocidad_actual,
            'mensaje': f"Automóvil frenando gradualmente a {self.velocidad_actual} km/h"
        }

    def calcular_consumo_combustible(self, distancia):
        # Consumo base: 8 litros por 100km para gasolina
        consumo_base = 8.0

        # Ajustes según características del automóvil
        factor_puertas = 1.1 if self.num_puertas > 4 else 1.0
        factor_edad = 1.0 + (2024 - self.año) * 0.02  # 2% más consumo por año

        consumo_total = (consumo_base * factor_puertas * factor_edad *
                         self.factor_eficiencia * distancia) / 100

        costo_por_litro = {
            "Gasolina": 1.45,
            "Diesel": 1.35,
            "Híbrido": 1.45,
            "Eléctrico": 0.12
        }.get(self.tipo_combustible, 1.45)

        return {
            'consumo_litros': round(consumo_total, 2),
            'costo_combustible': round(consumo_total * costo_por_litro, 2),
            'tipo_combustible': self.tipo_combustible,
            'eficiencia': f"{round(consumo_total / distancia * 100, 1)} L/100km",
            'detalles': {
                'factor_puertas': factor_puertas,
                'factor_edad': round(factor_edad, 2),
                'factor_eficiencia': self.factor_eficiencia
            }
        }


# Subclase Motocicleta
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada, peso=150):
        super().__init__(marca, modelo, año)
        self.cilindrada = cilindrada
        self.peso = peso
        self.velocidad_maxima = 220

    def acelerar(self, incremento):
        # Las motocicletas aceleran más rápido
        aceleracion_efectiva = incremento * 1.3
        nueva_velocidad = min(self.velocidad_actual + aceleracion_efectiva, self.velocidad_maxima)
        aceleracion_real = nueva_velocidad - self.velocidad_actual
        self.velocidad_actual = nueva_velocidad

        return {
            'accion': 'Aceleración',
            'incremento_solicitado': incremento,
            'aceleracion_real': round(aceleracion_real, 1),
            'velocidad_actual': round(self.velocidad_actual, 1),
            'mensaje': f"Motocicleta acelerando rápidamente a {self.velocidad_actual:.1f} km/h"
        }

    def frenar(self, decremento):
        # Las motocicletas frenan más eficientemente pero con más riesgo
        frenado_efectivo = decremento * 1.2
        nueva_velocidad = max(self.velocidad_actual - frenado_efectivo, 0)
        frenado_real = self.velocidad_actual - nueva_velocidad
        self.velocidad_actual = nueva_velocidad

        return {
            'accion': 'Frenado',
            'decremento_solicitado': decremento,
            'frenado_real': round(frenado_real, 1),
            'velocidad_actual': round(self.velocidad_actual, 1),
            'mensaje': f"Motocicleta frenando ágilmente a {self.velocidad_actual:.1f} km/h"
        }

    def calcular_consumo_combustible(self, distancia):
        # Consumo base según cilindrada
        if self.cilindrada <= 150:
            consumo_base = 2.5
        elif self.cilindrada <= 300:
            consumo_base = 3.5
        elif self.cilindrada <= 600:
            consumo_base = 4.5
        else:
            consumo_base = 6.0

        # Factor de peso (motocicletas más pesadas consumen más)
        factor_peso = self.peso / 150
        factor_edad = 1.0 + (2024 - self.año) * 0.015

        consumo_total = (consumo_base * factor_peso * factor_edad * distancia) / 100
        costo_combustible = consumo_total * 1.45  # Precio gasolina

        return {
            'consumo_litros': round(consumo_total, 2),
            'costo_combustible': round(costo_combustible, 2),
            'tipo_combustible': 'Gasolina',
            'eficiencia': f"{round(consumo_total / distancia * 100, 1)} L/100km",
            'detalles': {
                'cilindrada': self.cilindrada,
                'factor_peso': round(factor_peso, 2),
                'factor_edad': round(factor_edad, 2)
            }
        }


# Subclase Camión
class Camion(Vehiculo):
    def __init__(self, marca, modelo, año, capacidad_carga, carga_actual=0):
        super().__init__(marca, modelo, año)
        self.capacidad_carga = capacidad_carga  # en toneladas
        self.carga_actual = carga_actual
        self.velocidad_maxima = 90

    def acelerar(self, incremento):
        # Los camiones aceleran más lento, especialmente con carga
        factor_carga = 1.0 - (self.carga_actual / self.capacidad_carga) * 0.4
        aceleracion_efectiva = incremento * factor_carga * 0.6
        nueva_velocidad = min(self.velocidad_actual + aceleracion_efectiva, self.velocidad_maxima)
        aceleracion_real = nueva_velocidad - self.velocidad_actual
        self.velocidad_actual = nueva_velocidad

        return {
            'accion': 'Aceleración',
            'incremento_solicitado': incremento,
            'aceleracion_real': round(aceleracion_real, 1),
            'velocidad_actual': round(self.velocidad_actual, 1),
            'mensaje': f"Camión acelerando lentamente a {self.velocidad_actual:.1f} km/h (Carga: {self.carga_actual}t)"
        }

    def frenar(self, decremento):
        # Los camiones necesitan más distancia para frenar
        factor_carga = 1.0 + (self.carga_actual / self.capacidad_carga) * 0.5
        frenado_efectivo = decremento / factor_carga * 0.8
        nueva_velocidad = max(self.velocidad_actual - frenado_efectivo, 0)
        frenado_real = self.velocidad_actual - nueva_velocidad
        self.velocidad_actual = nueva_velocidad

        return {
            'accion': 'Frenado',
            'decremento_solicitado': decremento,
            'frenado_real': round(frenado_real, 1),
            'velocidad_actual': round(self.velocidad_actual, 1),
            'mensaje': f"Camión frenando gradualmente a {self.velocidad_actual:.1f} km/h (Carga: {self.carga_actual}t)"
        }

    def calcular_consumo_combustible(self, distancia):
        # Consumo base alto para camiones (diesel)
        consumo_base = 25.0  # litros por 100km sin carga

        # Factor de carga (más carga = más consumo)
        factor_carga = 1.0 + (self.carga_actual / self.capacidad_carga) * 0.8
        factor_capacidad = 1.0 + (self.capacidad_carga / 20) * 0.3  # Camiones más grandes consumen más
        factor_edad = 1.0 + (2024 - self.año) * 0.03

        consumo_total = (consumo_base * factor_carga * factor_capacidad *
                         factor_edad * distancia) / 100

        costo_combustible = consumo_total * 1.35  # Precio diesel

        return {
            'consumo_litros': round(consumo_total, 2),
            'costo_combustible': round(costo_combustible, 2),
            'tipo_combustible': 'Diesel',
            'eficiencia': f"{round(consumo_total / distancia * 100, 1)} L/100km",
            'detalles': {
                'capacidad_carga': self.capacidad_carga,
                'carga_actual': self.carga_actual,
                'factor_carga': round(factor_carga, 2),
                'factor_capacidad': round(factor_capacidad, 2),
                'factor_edad': round(factor_edad, 2)
            }
        }


# SIMULADOR DE VIAJE - POLIMORFISMO EN ACCIÓN
class SimuladorViaje:
    def __init__(self):
        self.vehiculos = []
        self.historial_simulaciones = []

    def agregar_vehiculo(self, vehiculo):
        """Agrega un vehículo al simulador"""
        self.vehiculos.append(vehiculo)

    def simular_viaje(self, distancia, mostrar_detalles=True):
        """
        Simula un viaje con todos los vehículos registrados
        POLIMORFISMO: Usa el mismo método calcular_consumo_combustible()
        sin conocer el tipo específico de cada vehículo
        """
        print(f"\nSIMULADOR DE VIAJE - DISTANCIA: {distancia} km")
        print("=" * 70)

        resultados = []

        for i, vehiculo in enumerate(self.vehiculos, 1):
            print(f"\n[{i}] {vehiculo}")
            print("-" * 50)

            # POLIMORFISMO: El mismo método, comportamiento diferente
            consumo_info = vehiculo.calcular_consumo_combustible(distancia)

            resultado = {
                'vehiculo': str(vehiculo),
                'tipo': type(vehiculo).__name__,
                'consumo_litros': consumo_info['consumo_litros'],
                'costo': consumo_info['costo_combustible'],
                'eficiencia': consumo_info['eficiencia'],
                'combustible': consumo_info['tipo_combustible']
            }

            if mostrar_detalles:
                print(f"Tipo: {type(vehiculo).__name__}")
                print(f"Combustible: {consumo_info['tipo_combustible']}")
                print(f"Consumo: {consumo_info['consumo_litros']} litros")
                print(f"Costo: ${consumo_info['costo_combustible']}")
                print(f"Eficiencia: {consumo_info['eficiencia']}")

                if 'detalles' in consumo_info:
                    print(f"Factores: {consumo_info['detalles']}")

            resultados.append(resultado)

        # Análisis comparativo
        self._mostrar_analisis_comparativo(resultados, distancia)

        # Guardar simulación
        simulacion = {
            'distancia': distancia,
            'vehiculos_count': len(self.vehiculos),
            'resultados': resultados
        }
        self.historial_simulaciones.append(simulacion)

        return resultados

    def _mostrar_analisis_comparativo(self, resultados, distancia):
        """Muestra análisis comparativo de la simulación"""
        print(f"\nANÁLISIS COMPARATIVO - {distancia} km")
        print("=" * 70)

        # Ordenar por eficiencia (menor consumo es mejor)
        resultados_ordenados = sorted(resultados, key=lambda x: x['consumo_litros'])

        print("\nRANKING DE EFICIENCIA:")
        for i, resultado in enumerate(resultados_ordenados, 1):
            print(f"{i}. {resultado['vehiculo']} - {resultado['eficiencia']}")

        print(f"\nRANKING DE COSTO:")
        resultados_por_costo = sorted(resultados, key=lambda x: x['costo'])
        for i, resultado in enumerate(resultados_por_costo, 1):
            print(f"{i}. {resultado['vehiculo']} - ${resultado['costo']}")

        # Estadísticas generales
        total_consumo = sum(r['consumo_litros'] for r in resultados)
        total_costo = sum(r['costo'] for r in resultados)
        promedio_consumo = total_consumo / len(resultados)

        print(f"\nESTADÍSTICAS GENERALES:")
        print(f"Consumo total: {total_consumo:.2f} litros")
        print(f"Costo total: ${total_costo:.2f}")
        print(f"Consumo promedio: {promedio_consumo:.2f} litros")
        print(f"Eficiencia promedio: {promedio_consumo / distancia * 100:.1f} L/100km")

    def simular_manejo_dinamico(self, vehiculo, distancia_segmentos):
        """Simula manejo dinámico con aceleración y frenado"""
        print(f"\nSIMULACIÓN DINÁMICA: {vehiculo}")
        print("=" * 50)

        for i, distancia in enumerate(distancia_segmentos, 1):
            print(f"\nSegmento {i} ({distancia} km):")

            # Acelerar
            aceleracion = random.randint(20, 60)
            resultado_acel = vehiculo.acelerar(aceleracion)
            print(f"  {resultado_acel['mensaje']}")

            # Calcular consumo del segmento
            consumo = vehiculo.calcular_consumo_combustible(distancia)
            print(f"  Consumo segmento: {consumo['consumo_litros']} L")

            # Frenar ocasionalmente
            if random.random() > 0.5:
                frenado = random.randint(10, 30)
                resultado_fren = vehiculo.frenar(frenado)
                print(f"  {resultado_fren['mensaje']}")


# DEMOSTRACIÓN COMPLETA
def main():
    print("SISTEMA DE VEHÍCULOS CON POLIMORFISMO")
    print("=" * 80)

    # Crear simulador
    simulador = SimuladorViaje()

    # Crear diferentes tipos de vehículos
    vehiculos = [
        # Automóviles
        Automovil("Toyota", "Corolla", 2020, 4, "Gasolina"),
        Automovil("Toyota", "Prius", 2022, 4, "Híbrido"),
        Automovil("Tesla", "Model 3", 2023, 4, "Eléctrico"),
        Automovil("BMW", "X7", 2019, 7, "Gasolina"),

        # Motocicletas
        Motocicleta("Honda", "CBR250R", 2021, 250, 140),
        Motocicleta("Yamaha", "R1", 2020, 1000, 190),
        Motocicleta("Harley-Davidson", "Street 750", 2018, 750, 220),

        # Camiones
        Camion("Volvo", "FH16", 2019, 25, 15),  # 15t de carga actual
        Camion("Mercedes-Benz", "Actros", 2021, 18, 8),
        Camion("Scania", "R450", 2017, 30, 20)
    ]

    # Agregar vehículos al simulador
    for vehiculo in vehiculos:
        simulador.agregar_vehiculo(vehiculo)

    # POLIMORFISMO EN ACCIÓN: Simular viajes de diferentes distancias
    distancias_prueba = [50, 200, 500]

    for distancia in distancias_prueba:
        simulador.simular_viaje(distancia)
        print("\n" + "=" * 80)

    # Demostración de manejo dinámico
    print("\nDEMOSTRACIÓN DE MANEJO DINÁMICO")
    print("=" * 80)

    vehiculo_prueba = vehiculos[0]  # Toyota Corolla
    segmentos = [25, 30, 45, 20]  # Diferentes segmentos de viaje
    simulador.simular_manejo_dinamico(vehiculo_prueba, segmentos)

    # Mostrar polimorfismo explícitamente
    print(f"\nDEMOSTRACIÓN EXPLÍCITA DE POLIMORFISMO")
    print("=" * 80)
    print("El mismo método 'calcular_consumo_combustible()' funciona diferente:")

    vehiculos_muestra = [vehiculos[0], vehiculos[4], vehiculos[7]]  # Auto, Moto, Camión
    distancia_prueba = 100

    for vehiculo in vehiculos_muestra:
        consumo = vehiculo.calcular_consumo_combustible(distancia_prueba)
        print(f"\n{type(vehiculo).__name__}: {vehiculo}")
        print(f"  → Consumo: {consumo['consumo_litros']} L")
        print(f"  → Eficiencia: {consumo['eficiencia']}")
        print(f"  → Combustible: {consumo['tipo_combustible']}")


if __name__ == "__main__":
    main()