"""
Solución - Ejercicio propuesto 04 - Curso y estudiantes (composición)
"""

class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota


class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []  # en __init__: cada curso tiene su propia lista

    def inscribir(self, estudiante):
        for inscrito in self.estudiantes:
            if inscrito.nombre == estudiante.nombre:
                raise ValueError(f"{estudiante.nombre} ya está inscrito")
        self.estudiantes.append(estudiante)

    def promedio(self):
        if not self.estudiantes:
            return 0
        return sum(e.nota for e in self.estudiantes) / len(self.estudiantes)

    def mejor_estudiante(self):
        if not self.estudiantes:
            return None
        return max(self.estudiantes, key=lambda e: e.nota)

    def aprobados(self):
        return [e.nombre for e in self.estudiantes if e.nota >= 3.0]


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    poo = Curso("POO")
    bd = Curso("Bases de datos")
    assert poo.promedio() == 0
    assert poo.mejor_estudiante() is None

    poo.inscribir(Estudiante("Ana", 4.5))
    poo.inscribir(Estudiante("Luis", 2.5))
    poo.inscribir(Estudiante("Eva", 4.0))

    assert len(bd.estudiantes) == 0, "Cada curso debe tener su propia lista"
    assert round(poo.promedio(), 2) == 3.67
    assert poo.mejor_estudiante().nombre == "Ana"
    assert poo.aprobados() == ["Ana", "Eva"]

    try:
        poo.inscribir(Estudiante("Ana", 5.0))
        raise AssertionError("No se puede inscribir dos veces a la misma persona")
    except ValueError:
        pass

    print("Todas las pruebas pasaron")
