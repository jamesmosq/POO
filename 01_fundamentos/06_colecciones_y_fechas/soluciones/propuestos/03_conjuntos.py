"""
Solución - Ejercicio propuesto 03 - Conjuntos
"""

def en_ambos(curso_a, curso_b):
    return set(curso_a) & set(curso_b)


def solo_en_a(curso_a, curso_b):
    return set(curso_a) - set(curso_b)


def todos(curso_a, curso_b):
    return set(curso_a) | set(curso_b)


def palabras_unicas(texto):
    # split() sin argumentos separa por espacios y descarta los vacíos.
    return set(texto.lower().split())


# ----------------------------------------------------------------------
# Pruebas
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
