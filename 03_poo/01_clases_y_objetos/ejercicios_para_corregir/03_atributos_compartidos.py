"""
Ejercicio para corregir 03 - Atributos compartidos
Nivel: intermedio
Errores a encontrar: 2

Qué debería hacer el programa:
    - Cada Curso tiene su PROPIA lista de estudiantes.
    - Curso.total_cursos cuenta cuántos cursos se han creado en total.

        poo = Curso("POO"); bd = Curso("BD")
        poo.inscribir("Ana")
        poo.estudiantes -> ["Ana"]
        bd.estudiantes  -> []
        Curso.total_cursos -> 2

Ojo: el programa no lanza errores. Los dos fallos tienen que ver con la
diferencia entre atributos de clase y atributos de instancia.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class Curso:
    total_cursos = 0
    estudiantes = []

    def __init__(self, nombre):
        self.nombre = nombre
        self.total_cursos += 1

    def inscribir(self, estudiante):
        self.estudiantes.append(estudiante)


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
