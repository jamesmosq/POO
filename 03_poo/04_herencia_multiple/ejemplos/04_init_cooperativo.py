"""
Ejemplo 04 - __init__ cooperativo con **kwargs

Problema: en herencia múltiple, cada padre necesita parámetros distintos.
Si todos usan super().__init__(), ¿cómo recibe cada uno los suyos?

Solución: cada __init__ toma los argumentos que le interesan POR NOMBRE y
le pasa el resto (**kwargs) a la siguiente clase del MRO. Al final de la
cadena, la última clase llama a object.__init__() sin argumentos.

Regla práctica: al crear el objeto, pasa todos los argumentos por nombre.
"""


class Persona:
    def __init__(self, nombre, **kwargs):
        super().__init__(**kwargs)  # kwargs ya debe estar vacío al llegar a object
        self.nombre = nombre


class Empleado(Persona):
    def __init__(self, salario, **kwargs):
        super().__init__(**kwargs)
        self.salario = salario


class Estudiante(Persona):
    def __init__(self, carrera, **kwargs):
        super().__init__(**kwargs)
        self.carrera = carrera


class Monitor(Empleado, Estudiante):
    """Estudiante que además trabaja como monitor: es Empleado y Estudiante."""

    def __init__(self, horas, **kwargs):
        super().__init__(**kwargs)
        self.horas = horas

    def ficha(self):
        return f"{self.nombre} ({self.carrera}) - {self.horas} h - ${self.salario:,}"


ana = Monitor(nombre="Ana", salario=800_000, carrera="Sistemas", horas=20)
print(ana.ficha())
print("MRO:", [c.__name__ for c in Monitor.mro()])

# Recorrido de los argumentos:
#   Monitor    toma horas      y pasa {nombre, salario, carrera}
#   Empleado   toma salario    y pasa {nombre, carrera}
#   Estudiante toma carrera    y pasa {nombre}
#   Persona    toma nombre     y pasa {}
#   object     recibe {}       y termina
# Persona.__init__ se ejecutó una sola vez.

# Si sobra un argumento, el error lo da object.__init__:
try:
    Monitor(nombre="Luis", salario=1, carrera="Redes", horas=5, color="azul")
except TypeError as error:
    print("Error esperado:", error)
