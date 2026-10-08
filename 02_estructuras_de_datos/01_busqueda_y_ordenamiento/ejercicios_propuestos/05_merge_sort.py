"""
Ejercicio propuesto 05 - Merge sort y ordenamiento por criterios
Nivel: avanzado

Merge sort divide la lista en dos mitades, ordena cada una (llamándose a
sí mismo) y luego las mezcla. Es mucho más rápido que burbuja o inserción
en listas grandes.

Requisitos:
1. mezclar(izquierda, derecha, key): recibe dos listas YA ordenadas y
   retorna una sola lista ordenada. Compara key(elemento) de cada lado.
   Si hay empate, toma primero el de la izquierda (así el ordenamiento es
   "estable": respeta el orden original entre elementos iguales).
2. merge_sort(lista, key=None): ordena usando recursión.
   - Caso base: una lista de 0 o 1 elementos ya está ordenada.
   - Si key es None, usa la identidad: lambda x: x.
3. ordenar_estudiantes(estudiantes): los estudiantes son tuplas
   (nombre, nota). Retorna la lista ordenada por nota de MAYOR a menor y,
   si hay empate, por nombre alfabéticamente. Aquí sí puedes usar sorted()
   con una key que retorne una tupla.

Conceptos: recursión, divide y vencerás, estabilidad, key.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import random

    assert mezclar([1, 4, 9], [2, 3, 10], key=lambda x: x) == [1, 2, 3, 4, 9, 10]
    assert merge_sort([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82]
    assert merge_sort([]) == []

    aleatorios = [random.randint(-1000, 1000) for _ in range(500)]
    assert merge_sort(aleatorios) == sorted(aleatorios)

    personas = [("Ana", 3), ("Luis", 1), ("Eva", 3), ("Beto", 1)]
    assert merge_sort(personas, key=lambda p: p[1]) == [("Luis", 1), ("Beto", 1), ("Ana", 3), ("Eva", 3)], (
        "Con notas iguales se debe conservar el orden original"
    )

    estudiantes = [("Eva", 4.5), ("Ana", 3.8), ("Luis", 4.5), ("Beto", 3.8)]
    assert ordenar_estudiantes(estudiantes) == [("Eva", 4.5), ("Luis", 4.5), ("Ana", 3.8), ("Beto", 3.8)]

    print("Todas las pruebas pasaron")
