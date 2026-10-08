"""
Ejercicio para corregir 04 - Quitar pares y buscar
Nivel: intermedio
Errores a encontrar: 3

Qué debería hacer el programa:
    - quitar_pares(numeros) retorna una lista NUEVA sin los números pares.
      La lista original no debe cambiar.
          quitar_pares([1, 2, 4, 5]) -> [1, 5]
    - buscar_posicion(lista, objetivo) retorna la posición del objetivo en
      la lista, o -1 si no está.
          buscar_posicion(["a", "b", "c"], "c") -> 2

Ojo: uno de los errores es un clásico. Modificar una lista mientras se
recorre con un for hace que el ciclo se salte elementos.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


def quitar_pares(numeros):
    for n in numeros:
        if n % 2 == 0:
            numeros.remove(n)
    return numeros


def buscar_posicion(lista, objetivo):
    for i, elemento in enumerate(lista):
        if elemento == objetivo:
            return i
        else:
            return -1


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    datos = [1, 2, 4, 5, 6, 8]
    assert quitar_pares(datos) == [1, 5], f"quitar_pares retornó {quitar_pares([1, 2, 4, 5, 6, 8])}"
    assert datos == [1, 2, 4, 5, 6, 8], f"La lista original cambió: {datos}"

    assert buscar_posicion(["a", "b", "c"], "a") == 0
    assert buscar_posicion(["a", "b", "c"], "c") == 2
    assert buscar_posicion(["a", "b", "c"], "z") == -1
    assert buscar_posicion([], "a") == -1

    print("Todas las pruebas pasaron")
