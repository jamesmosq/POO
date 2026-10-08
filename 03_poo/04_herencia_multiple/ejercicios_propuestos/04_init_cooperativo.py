"""
Ejercicio propuesto 04 - __init__ cooperativo
Nivel: intermedio

En una universidad, un Monitor es al mismo tiempo Empleado y Estudiante.
Cada clase necesita datos distintos en su constructor.

Requisitos (revisa antes el ejemplo 04 de este tema):
1. Persona(nombre, documento)
2. Empleado(salario, ...) hija de Persona
3. Estudiante(programa, semestre, ...) hija de Persona
4. Monitor(asignatura, ...) hija de Empleado y de Estudiante, en ese orden
5. Cada __init__ recibe SOLO sus propios parámetros por nombre y **kwargs
   con el resto, y llama a super().__init__(**kwargs). Persona también
   llama a super().__init__(**kwargs) (le llega vacío).
6. Atributo de clase Persona.creadas = 0, que suma 1 en Persona.__init__:
   al crear un Monitor debe sumar 1, no 2.
7. Monitor.ficha(): "Ana (CC 123) - Sistemas sem. 5 - monitor de POO - $800,000"

Los objetos se crean con argumentos por nombre:
    Monitor(nombre="Ana", documento="123", salario=800000,
            programa="Sistemas", semestre=5, asignatura="POO")

Conceptos: herencia múltiple con constructores distintos, **kwargs,
super() cooperativo.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
