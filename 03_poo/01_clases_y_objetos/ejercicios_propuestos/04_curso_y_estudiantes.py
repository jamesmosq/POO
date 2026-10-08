"""
Ejercicio propuesto 04 - Curso y estudiantes (composición)
Nivel: intermedio

Composición: un objeto contiene a otros objetos. Un Curso TIENE
Estudiantes.

Requisitos:
1. Clase Estudiante(nombre, nota).
2. Clase Curso(nombre):
   - Cada curso tiene su propia lista de estudiantes (créala en __init__).
   - inscribir(estudiante): agrega un Estudiante. Lanza ValueError si ya
     hay un estudiante con el mismo nombre en el curso.
   - promedio(): promedio de las notas; 0 si no hay estudiantes.
   - mejor_estudiante(): el Estudiante con la nota más alta, o None.
   - aprobados(): lista de NOMBRES de quienes tienen 3.0 o más.

Conceptos: composición, listas de objetos, recorrer objetos.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
