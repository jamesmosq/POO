"""
Solución - Ejercicio para corregir 03 - Atributos compartidos

CORRECCIÓN 1: estudiantes = [] escrito en el cuerpo de la clase es UNA
sola lista compartida por todos los cursos. Lo que es de cada objeto se
crea en __init__ con self.

CORRECCIÓN 2: self.total_cursos += 1 lee el valor de la clase, pero al
asignar crea un atributo NUEVO en el objeto; el de la clase sigue en 0.
Para modificar el atributo de clase se usa el nombre de la clase.
"""

class Curso:
    total_cursos = 0

    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []  # CORRECCIÓN 1
        Curso.total_cursos += 1  # CORRECCIÓN 2

    def inscribir(self, estudiante):
        self.estudiantes.append(estudiante)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    Curso.total_cursos = 0
    poo = Curso("POO")
    bd = Curso("BD")
    poo.inscribir("Ana")

    assert poo.estudiantes == ["Ana"]
    assert bd.estudiantes == [], f"bd tiene estudiantes de otro curso: {bd.estudiantes}"
    assert Curso.total_cursos == 2, f"Curso.total_cursos vale {Curso.total_cursos}"

    print("Todas las pruebas pasaron")
