"""
Ejercicio propuesto 05 - Boletín de notas
Nivel: avanzado

Tienes dos listas paralelas: en la posición i de nombres está el
estudiante cuya nota está en la posición i de notas.

Requisitos:
1. boletin(nombres, notas): retorna una lista de textos con este formato,
   numerados desde 1:
       "1. Ana: 4.5 (Aprobado)"
       "2. Luis: 2.8 (Reprobado)"
   Se aprueba con 3.0 o más. Usa enumerate(..., start=1) y zip() en el
   mismo for.
2. mejor_estudiante(nombres, notas): retorna el nombre con la nota más
   alta. Si hay empate, gana el primero que aparece.
3. Las dos funciones lanzan ValueError si las listas tienen distinto largo.

Conceptos: zip, enumerate, desempaquetar en el for, validación.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    nombres = ["Ana", "Luis", "Eva"]
    notas = [4.5, 2.8, 4.5]

    assert boletin(nombres, notas) == [
        "1. Ana: 4.5 (Aprobado)",
        "2. Luis: 2.8 (Reprobado)",
        "3. Eva: 4.5 (Aprobado)",
    ]
    assert boletin([], []) == []
    assert mejor_estudiante(nombres, notas) == "Ana"
    assert mejor_estudiante(["Luis", "Eva"], [3.0, 3.1]) == "Eva"

    for funcion in (boletin, mejor_estudiante):
        try:
            funcion(["Ana", "Luis"], [4.0])
            raise AssertionError(f"{funcion.__name__} debe lanzar ValueError")
        except ValueError:
            pass

    print("Todas las pruebas pasaron")
