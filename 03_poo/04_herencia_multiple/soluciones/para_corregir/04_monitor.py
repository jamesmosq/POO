"""
Solución - Ejercicio para corregir 04 - Monitor

CORRECCIÓN 1 (Monitor): super().__init__(kwargs) pasa el diccionario como
UN argumento posicional. Para pasar sus elementos como argumentos por
nombre se desempaqueta: super().__init__(**kwargs).

CORRECCIÓN 2 (Empleado): Persona.__init__(self, ...) salta directo a
Persona y se salta a Estudiante, que es el siguiente en el MRO de Monitor.
Por eso el constructor de Estudiante nunca se ejecutaba (y el argumento
carrera terminaba llegando a object). En herencia múltiple, siempre super().

CORRECCIÓN 3 (Estudiante): el mismo error que el 1: faltaban los ** al
pasar kwargs.
"""

class Persona:
    def __init__(self, nombre, **kwargs):
        super().__init__(**kwargs)
        self.nombre = nombre


class Empleado(Persona):
    def __init__(self, salario, **kwargs):
        super().__init__(**kwargs)  # CORRECCIÓN 2
        self.salario = salario


class Estudiante(Persona):
    def __init__(self, carrera, **kwargs):
        super().__init__(**kwargs)  # CORRECCIÓN 3
        self.carrera = carrera


class Monitor(Empleado, Estudiante):
    def __init__(self, horas, **kwargs):
        super().__init__(**kwargs)  # CORRECCIÓN 1
        self.horas = horas


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    ana = Monitor(nombre="Ana", salario=800000, carrera="Sistemas", horas=20)
    assert ana.horas == 20 and ana.salario == 800000
    assert ana.nombre == "Ana"
    assert getattr(ana, "carrera", None) == "Sistemas", "El constructor de Estudiante no se ejecutó"

    eva = Estudiante(nombre="Eva", carrera="Diseño")
    assert (eva.nombre, eva.carrera) == ("Eva", "Diseño")

    print("Todas las pruebas pasaron")
