"""
Solución - Ejercicio propuesto 04 - __init__ cooperativo
"""

class Persona:
    creadas = 0

    def __init__(self, nombre, documento, **kwargs):
        super().__init__(**kwargs)
        Persona.creadas += 1
        self.nombre = nombre
        self.documento = documento


class Empleado(Persona):
    def __init__(self, salario, **kwargs):
        super().__init__(**kwargs)
        self.salario = salario


class Estudiante(Persona):
    def __init__(self, programa, semestre, **kwargs):
        super().__init__(**kwargs)
        self.programa = programa
        self.semestre = semestre


class Monitor(Empleado, Estudiante):
    def __init__(self, asignatura, **kwargs):
        # Cada clase toma lo suyo y pasa el resto. El orden es el del MRO:
        # Monitor -> Empleado -> Estudiante -> Persona -> object.
        super().__init__(**kwargs)
        self.asignatura = asignatura

    def ficha(self):
        return (f"{self.nombre} (CC {self.documento}) - {self.programa} sem. {self.semestre}"
                f" - monitor de {self.asignatura} - ${self.salario:,}")


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    Persona.creadas = 0
    ana = Monitor(nombre="Ana", documento="123", salario=800000, programa="Sistemas", semestre=5, asignatura="POO")
    assert (ana.nombre, ana.documento, ana.salario) == ("Ana", "123", 800000)
    assert (ana.programa, ana.semestre, ana.asignatura) == ("Sistemas", 5, "POO")
    assert ana.ficha() == "Ana (CC 123) - Sistemas sem. 5 - monitor de POO - $800,000", ana.ficha()
    assert Persona.creadas == 1, f"Persona.__init__ se ejecutó {Persona.creadas} veces"

    luis = Empleado(nombre="Luis", documento="456", salario=1500000)
    assert luis.nombre == "Luis" and not hasattr(luis, "programa")
    eva = Estudiante(nombre="Eva", documento="789", programa="Diseño", semestre=2)
    assert eva.semestre == 2

    assert Monitor.__bases__ == (Empleado, Estudiante)
    assert [c.__name__ for c in Monitor.mro()] == ["Monitor", "Empleado", "Estudiante", "Persona", "object"]

    try:
        Monitor(nombre="X", documento="0", salario=1, programa="P", semestre=1, asignatura="A", sobra=True)
        raise AssertionError("Un argumento que nadie usa debe producir TypeError")
    except TypeError:
        pass

    print("Todas las pruebas pasaron")
