"""
Ejercicio propuesto 03 - Conjuntos
Nivel: intermedio

Un conjunto (set) guarda elementos sin repetir y permite operaciones como
las de matemáticas: unión, intersección y diferencia.

Requisitos. Recibes dos listas de estudiantes inscritos en dos cursos:
1. en_ambos(curso_a, curso_b): conjunto de los inscritos en los dos.
2. solo_en_a(curso_a, curso_b): conjunto de los que están en A pero no en B.
3. todos(curso_a, curso_b): conjunto de todos los estudiantes, sin repetir.
4. palabras_unicas(texto): conjunto de palabras distintas del texto, en
   minúscula. Las palabras están separadas por espacios.
       "Hola hola mundo" -> {"hola", "mundo"}

Usa los operadores de conjuntos: & (intersección), - (diferencia),
| (unión). Recuerda que un conjunto vacío se crea con set(), no con {}.

Conceptos: set, operaciones de conjuntos, split, eliminar duplicados.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    a = ["Ana", "Luis", "Eva", "Ana"]
    b = ["Eva", "Pedro", "Luis"]

    assert en_ambos(a, b) == {"Luis", "Eva"}
    assert solo_en_a(a, b) == {"Ana"}
    assert todos(a, b) == {"Ana", "Luis", "Eva", "Pedro"}
    assert en_ambos([], b) == set()

    assert palabras_unicas("Hola hola mundo") == {"hola", "mundo"}
    assert palabras_unicas("") == set()
    assert len(palabras_unicas("el perro y el gato y el loro")) == 5

    print("Todas las pruebas pasaron")
