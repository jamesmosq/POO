"""
Ejercicio para corregir 04 - Monitor
Nivel: intermedio
Errores a encontrar: 3

Qué debería hacer el programa:
    Monitor hereda de Empleado y de Estudiante, que a su vez heredan de
    Persona. Cada constructor toma sus propios datos por nombre y pasa el
    resto con **kwargs a super().__init__(), de forma que TODOS los
    constructores se ejecutan, cada uno una sola vez.

        Monitor(nombre="Ana", salario=800000, carrera="Sistemas", horas=20)
        -> nombre, salario, carrera y horas quedan guardados.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class Persona:
    def __init__(self, nombre, **kwargs):
        super().__init__(**kwargs)
        self.nombre = nombre


class Empleado(Persona):
    def __init__(self, salario, **kwargs):
        Persona.__init__(self, **kwargs)
        self.salario = salario


class Estudiante(Persona):
    def __init__(self, carrera, **kwargs):
        super().__init__(kwargs)
        self.carrera = carrera


class Monitor(Empleado, Estudiante):
    def __init__(self, horas, **kwargs):
        super().__init__(kwargs)
        self.horas = horas


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    ana = Monitor(nombre="Ana", salario=800000, carrera="Sistemas", horas=20)
    assert ana.horas == 20 and ana.salario == 800000
    assert ana.nombre == "Ana"
    assert getattr(ana, "carrera", None) == "Sistemas", "El constructor de Estudiante no se ejecutó"

    eva = Estudiante(nombre="Eva", carrera="Diseño")
    assert (eva.nombre, eva.carrera) == ("Eva", "Diseño")

    print("Todas las pruebas pasaron")
