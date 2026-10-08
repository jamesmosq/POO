"""
Ejercicio para corregir 03 - Número mayor
Nivel: intermedio
Errores a encontrar: 2

Qué debería hacer el programa:
    mayor(numeros) recorre la lista y retorna el número más grande, sin usar
    la función max(). Debe funcionar también con números negativos.

        mayor([3, 9, 2])     -> 9
        mayor([-5, -2, -8])  -> -2

Ojo: el programa no lanza errores. Los dos fallos solo aparecen con
ciertas listas. Piensa qué listas dejarían en evidencia cada uno.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


def mayor(numeros):
    resultado = 0
    for i in range(len(numeros) - 1):
        if numeros[i] > resultado:
            resultado = numeros[i]
    return resultado


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert mayor([3, 9, 2]) == 9
    assert mayor([3, 2, 9]) == 9, f"mayor([3, 2, 9]) retornó {mayor([3, 2, 9])}"
    assert mayor([-5, -2, -8]) == -2, f"mayor([-5, -2, -8]) retornó {mayor([-5, -2, -8])}"
    assert mayor([7]) == 7

    print("Todas las pruebas pasaron")
