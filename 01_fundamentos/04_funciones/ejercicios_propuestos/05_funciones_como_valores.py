"""
Ejercicio propuesto 05 - Funciones como valores
Nivel: avanzado

En Python una función es un valor más: se puede guardar en una variable,
pasar como argumento o retornar desde otra función.

Requisitos:
1. aplicar_varias_veces(funcion, valor, veces): aplica la función al valor
   tantas veces como indique veces y retorna el resultado.
       aplicar_varias_veces(lambda x: x * 2, 1, 3)   -> 8   (1 -> 2 -> 4 -> 8)
   Puedes resolverlo con recursión (que la función se llame a sí misma
   con veces - 1) o esperar al tema de bucles y volver después.
2. componer(f, g): retorna una NUEVA función que recibe x y calcula f(g(x)).
       sumar_uno_y_duplicar = componer(lambda x: x * 2, lambda x: x + 1)
       sumar_uno_y_duplicar(3)   -> 8   ((3 + 1) * 2)
3. crear_multiplicador(n): retorna una función que multiplica por n.
       triple = crear_multiplicador(3)
       triple(5)   -> 15

Conceptos: lambda, funciones de orden superior, clausuras, recursión.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert aplicar_varias_veces(lambda x: x * 2, 1, 3) == 8
    assert aplicar_varias_veces(lambda x: x + 10, 5, 0) == 5
    assert aplicar_varias_veces(str.upper, "hola", 1) == "HOLA"

    sumar_uno_y_duplicar = componer(lambda x: x * 2, lambda x: x + 1)
    assert sumar_uno_y_duplicar(3) == 8
    duplicar_y_sumar_uno = componer(lambda x: x + 1, lambda x: x * 2)
    assert duplicar_y_sumar_uno(3) == 7

    triple = crear_multiplicador(3)
    doble = crear_multiplicador(2)
    assert triple(5) == 15
    assert doble(5) == 10
    assert componer(triple, doble)(1) == 6

    print("Todas las pruebas pasaron")
