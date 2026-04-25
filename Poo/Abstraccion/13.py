"""
Ejercicio 9: Personal Médico
Situación: Un hospital tiene doctores, enfermeras, cirujanos y especialistas.
Tu tarea:
•	Abstrae las características comunes de cualquier personal médico
•	Define responsabilidades que todo el personal debe cumplir
•	Crea clase abstracta PersonalMedico con:
o	Atributos: nombre, cedula_profesional, anos_experiencia, turno
o	Métodos abstractos: atender_paciente(), realizar_procedimiento(), generar_reporte()
•	Implementa Doctor y Enfermera
Pista: Todo el personal médico atiende pacientes, hace procedimientos y documenta su trabajo.


"""
from abc import ABC, abstractmethod


class PersonalMedico(ABC):
    def __init__(self, nombre, cedula_profesional, anos_experiencia, turno):
        self.nombre = nombre
        self.cedula_profesional = cedula_profesional
        self.anos_experiencia = anos_experiencia
        self.turno = turno

    @abstractmethod
    def atender_paciente(self):
        pass

    @abstractmethod
    def realizar_procedimiento(self):
        pass

    @abstractmethod
    def generar_reporte(self):
        pass

class Doctor(PersonalMedico):
    def atender_paciente(self):
        return f"Doctor {self.nombre} está atendiendo al paciente."

    def realizar_procedimiento(self):
        return f"Doctor {self.nombre} está realizando un procedimiento médico."

    def generar_reporte(self):
        return f"Doctor {self.nombre} ha generado un reporte de su atención."

class Enfermera(PersonalMedico):
    def atender_paciente(self):
        return f"Enfermera {self.nombre} está atendiendo al paciente."

    def realizar_procedimiento(self):
        return f"Enfermera {self.nombre} está asistiendo en un procedimiento médico."

    def generar_reporte(self):
        return f"Enfermera {self.nombre} ha generado un reporte de su atención."

d1 = Doctor("Dr. Juan Pérez", "123456", 10, "Mañana")
e1 = Enfermera("Enf. Ana Gómez", "654321", 5, "Tarde")

print(" ====== Doctor ====== ")
print(d1.atender_paciente())
print(d1.realizar_procedimiento())
print(d1.generar_reporte())
print(" ")
print(" ====== Enfermera ===== ")
print(e1.atender_paciente())
print(e1.realizar_procedimiento())
print(e1.generar_reporte())