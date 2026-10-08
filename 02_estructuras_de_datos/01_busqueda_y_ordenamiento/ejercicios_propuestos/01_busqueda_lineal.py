"""
Ejercicio propuesto 01 - Búsqueda lineal
Nivel: básico

La búsqueda lineal revisa los elementos uno por uno, desde el principio,
hasta encontrar el objetivo o llegar al final.

Requisitos:
1. busqueda_lineal(lista, objetivo): retorna una tupla
   (posicion, comparaciones):
       - posicion: índice donde está el objetivo, o -1 si no está.
       - comparaciones: cuántos elementos se revisaron.
   No uses lista.index() ni el operador in: el objetivo es implementarlo.
2. buscar_todas(lista, objetivo): retorna la lista de TODAS las posiciones
   donde aparece el objetivo.

Pregunta para pensar (respóndela en un comentario): si la lista tiene
1.000.000 de elementos y el objetivo no está, ¿cuántas comparaciones hace
la búsqueda lineal?

Conceptos: recorrido secuencial, contadores, peor caso.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    datos = [7, 3, 9, 3, 5]
    assert busqueda_lineal(datos, 7) == (0, 1)
    assert busqueda_lineal(datos, 9) == (2, 3)
    assert busqueda_lineal(datos, 3) == (1, 2), "Retorna la primera aparición"
    assert busqueda_lineal(datos, 8) == (-1, 5)
    assert busqueda_lineal([], 1) == (-1, 0)

    assert buscar_todas(datos, 3) == [1, 3]
    assert buscar_todas(datos, 8) == []
    assert buscar_todas(["a", "b", "a"], "a") == [0, 2]

    print("Todas las pruebas pasaron")
