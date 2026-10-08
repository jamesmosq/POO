"""
Ejercicio propuesto 04 - Ordenamiento por inserción
Nivel: intermedio

El ordenamiento por inserción funciona como ordenar cartas en la mano:
se toma un elemento y se desplazan hacia la derecha los mayores que él,
hasta encontrar su lugar.

    [5, 2, 4]  -> toma el 2, el 5 se corre: [2, 5, 4]
               -> toma el 4, el 5 se corre: [2, 4, 5]

Requisitos. Escribe insercion(lista, descendente=False), que:
1. Retorne una lista NUEVA ordenada (no modifiques la original).
2. Ordene de menor a mayor, o de mayor a menor si descendente es True.
3. No use sort() ni sorted().

Conceptos: ordenamiento por inserción, desplazamiento, parámetros por
defecto.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    datos = [5, 2, 4, 6, 1, 3]
    assert insercion(datos) == [1, 2, 3, 4, 5, 6]
    assert insercion(datos, descendente=True) == [6, 5, 4, 3, 2, 1]
    assert datos == [5, 2, 4, 6, 1, 3], "No debe modificar la original"
    assert insercion([]) == []
    assert insercion([1]) == [1]
    assert insercion([3, 1, 2, 1]) == [1, 1, 2, 3]

    fuente = open(__file__, encoding="utf-8").read().split("# Pruebas")[0]
    assert "sorted(" not in fuente and ".sort(" not in fuente, "No uses sort() ni sorted()"

    print("Todas las pruebas pasaron")
