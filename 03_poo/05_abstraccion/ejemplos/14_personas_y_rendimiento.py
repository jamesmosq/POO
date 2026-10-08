from abc import ABC, abstractmethod


# Clase base abstracta
class Persona(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @abstractmethod
    def evaluar_rendimiento(self):
        """Método abstracto que debe ser implementado por las subclases"""
        pass

    def __str__(self):
        return f"{self.nombre} ({self.edad} años)"


# Clase Estudiante que hereda de Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera, promedio):
        super().__init__(nombre, edad)
        self.carrera = carrera
        self.promedio = promedio

    def __str__(self):
        return f"{super().__str__()} - {self.carrera} (Promedio: {self.promedio})"


# Subclase EstudianteRegular
class EstudianteRegular(Estudiante):
    def evaluar_rendimiento(self):
        if self.promedio >= 7.0:
            estado = "APROBADO"
            mensaje = "Cumple con los requisitos académicos básicos"
        else:
            estado = "REPROBADO"
            mensaje = "Necesita mejorar su rendimiento académico"

        return {
            'estado': estado,
            'criterio': 'Promedio ≥ 7.0',
            'mensaje': mensaje,
            'tipo': 'Estudiante Regular'
        }


# Subclase EstudianteInternacional
class EstudianteInternacional(Estudiante):
    def __init__(self, nombre, edad, carrera, promedio, adaptacion_cultural=True):
        super().__init__(nombre, edad, carrera, promedio)
        self.adaptacion_cultural = adaptacion_cultural

    def evaluar_rendimiento(self):
        # Criterios más estrictos para estudiantes internacionales
        promedio_aprobado = self.promedio >= 7.5

        if promedio_aprobado and self.adaptacion_cultural:
            estado = "APROBADO"
            mensaje = "Excelente rendimiento académico y buena adaptación cultural"
        elif promedio_aprobado and not self.adaptacion_cultural:
            estado = "APROBADO CON OBSERVACIONES"
            mensaje = "Buen rendimiento académico, pero requiere apoyo en adaptación cultural"
        else:
            estado = "REPROBADO"
            mensaje = "No cumple con los estándares académicos para estudiantes internacionales"

        return {
            'estado': estado,
            'criterio': 'Promedio ≥ 7.5 + Adaptación Cultural',
            'mensaje': mensaje,
            'tipo': 'Estudiante Internacional',
            'adaptacion': 'Sí' if self.adaptacion_cultural else 'No'
        }


# Subclase EstudianteBecado
class EstudianteBecado(Estudiante):
    def __init__(self, nombre, edad, carrera, promedio, tipo_beca="Académica"):
        super().__init__(nombre, edad, carrera, promedio)
        self.tipo_beca = tipo_beca

    def evaluar_rendimiento(self):
        if self.promedio >= 8.0:
            estado = "APROBADO - BECA MANTENIDA"
            mensaje = f"Excelente rendimiento. Mantiene beca {self.tipo_beca}"
        elif self.promedio >= 7.0:
            estado = "APROBADO - BECA EN RIESGO"
            mensaje = f"Rendimiento aceptable pero debe mejorar para mantener beca {self.tipo_beca}"
        else:
            estado = "REPROBADO - BECA PERDIDA"
            mensaje = f"Rendimiento insuficiente. Pierde beca {self.tipo_beca}"

        return {
            'estado': estado,
            'criterio': 'Promedio ≥ 8.0 para mantener beca',
            'mensaje': mensaje,
            'tipo': 'Estudiante Becado',
            'beca': self.tipo_beca
        }


# Función para mostrar evaluación de manera formateada
def mostrar_evaluacion(estudiante):
    print(f"\n{'=' * 60}")
    print(f"EVALUACIÓN DE: {estudiante}")
    print(f"{'=' * 60}")

    evaluacion = estudiante.evaluar_rendimiento()

    print(f"Tipo: {evaluacion['tipo']}")
    print(f"Criterio: {evaluacion['criterio']}")
    print(f"Estado: {evaluacion['estado']}")
    print(f"Observaciones: {evaluacion['mensaje']}")

    # Información adicional según el tipo de estudiante
    if 'adaptacion' in evaluacion:
        print(f"Adaptación Cultural: {evaluacion['adaptacion']}")
    if 'beca' in evaluacion:
        print(f"Tipo de Beca: {evaluacion['beca']}")


# DEMOSTRACIÓN DEL POLIMORFISMO
def main():
    print("🎓 SISTEMA DE EVALUACIÓN DE ESTUDIANTES 🎓")
    print("Demostración de Polimorfismo en Python")

    # Crear lista con diferentes tipos de estudiantes
    estudiantes = [
        EstudianteRegular("Ana García", 20, "Ingeniería Civil", 7.8),
        EstudianteRegular("Carlos López", 19, "Medicina", 6.5),

        EstudianteInternacional("Yuki Tanaka", 21, "Informática", 8.2, True),
        EstudianteInternacional("Pierre Dubois", 22, "Arquitectura", 7.6, False),
        EstudianteInternacional("Emma Wilson", 20, "Psicología", 7.2, True),

        EstudianteBecado("María Rodríguez", 19, "Química", 8.5, "Excelencia Académica"),
        EstudianteBecado("Diego Morales", 21, "Física", 7.3, "Deportiva"),
        EstudianteBecado("Sofía Hernández", 20, "Matemáticas", 6.8, "Socioeconómica")
    ]

    # POLIMORFISMO EN ACCIÓN:
    # El mismo método evaluar_rendimiento() se comporta diferente según el tipo
    for estudiante in estudiantes:
        mostrar_evaluacion(estudiante)

    # Estadísticas generales
    print(f"\n{'=' * 60}")
    print("📊 ESTADÍSTICAS GENERALES")
    print(f"{'=' * 60}")

    total = len(estudiantes)
    aprobados = 0

    for estudiante in estudiantes:
        evaluacion = estudiante.evaluar_rendimiento()
        if "APROBADO" in evaluacion['estado']:
            aprobados += 1

    print(f"Total de estudiantes evaluados: {total}")
    print(f"Estudiantes aprobados: {aprobados}")
    print(f"Estudiantes reprobados: {total - aprobados}")
    print(f"Porcentaje de aprobación: {(aprobados / total) * 100:.1f}%")


if __name__ == "__main__":
    main()