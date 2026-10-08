"""
Ejercicio propuesto 04 - Estudiantes (herencia multinivel)
Nivel: intermedio

Vas a construir una cadena de tres clases: Persona -> Estudiante ->
EstudianteBecado. Cada nivel agrega información y amplía lo que hace el
nivel anterior sin copiar su código.

Requisitos:
1. Persona(nombre, documento)
   - presentarse(): "Soy Ana, documento 123"
2. Estudiante(nombre, documento, programa), hija de Persona
   - Atributo de clase VALOR_MATRICULA = 1500000
   - presentarse(): agrega al texto del padre ", estudio Sistemas"
   - valor_matricula(): retorna VALOR_MATRICULA
3. EstudianteBecado(nombre, documento, programa, porcentaje_beca), hija de
   Estudiante
   - Lanza ValueError si porcentaje_beca no está entre 0 y 100.
   - presentarse(): agrega al texto del padre " y tengo beca del 50%"
   - valor_matricula(): aplica el descuento sobre el valor del padre.
     Con 50% de beca el resultado es 750000.

Cada presentarse() debe llamar a super().presentarse(). Si cambias el texto
de Persona, el cambio debe verse en las tres clases.

Conceptos: herencia multinivel, super(), atributos de clase, isinstance.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
