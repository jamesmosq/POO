"""
Solución - Ejercicio propuesto 04 - Estudiantes (herencia multinivel)
"""


class Persona:
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    def presentarse(self):
        return f"Soy {self.nombre}, documento {self.documento}"


class Estudiante(Persona):
    VALOR_MATRICULA = 1500000

    def __init__(self, nombre, documento, programa):
        super().__init__(nombre, documento)
        self.programa = programa

    def presentarse(self):
        return f"{super().presentarse()}, estudio {self.programa}"

    def valor_matricula(self):
        return self.VALOR_MATRICULA


class EstudianteBecado(Estudiante):
    def __init__(self, nombre, documento, programa, porcentaje_beca):
        if not 0 <= porcentaje_beca <= 100:
            raise ValueError("El porcentaje de beca debe estar entre 0 y 100")
        super().__init__(nombre, documento, programa)
        self.porcentaje_beca = porcentaje_beca

    def presentarse(self):
        return f"{super().presentarse()} y tengo beca del {self.porcentaje_beca}%"

    def valor_matricula(self):
        descuento = super().valor_matricula() * self.porcentaje_beca / 100
        return super().valor_matricula() - descuento


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    p = Persona("Ana", "123")
    assert p.presentarse() == "Soy Ana, documento 123"

    e = Estudiante("Luis", "456", "Sistemas")
    assert e.presentarse() == "Soy Luis, documento 456, estudio Sistemas"
    assert e.valor_matricula() == 1500000

    b = EstudianteBecado("Eva", "789", "Diseño", 50)
    assert b.presentarse() == "Soy Eva, documento 789, estudio Diseño y tengo beca del 50%"
    assert b.valor_matricula() == 750000
    assert isinstance(b, Persona)

    try:
        EstudianteBecado("Error", "000", "Sistemas", 120)
        raise AssertionError("Debe lanzar ValueError con porcentaje 120")
    except ValueError:
        pass

    nombres = [clase.__name__ for clase in EstudianteBecado.__mro__]
    assert nombres == ["EstudianteBecado", "Estudiante", "Persona", "object"]

    print("Todas las pruebas pasaron")
