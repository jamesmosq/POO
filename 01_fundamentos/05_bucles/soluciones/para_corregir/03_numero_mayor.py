"""
Solución - Ejercicio para corregir 03 - Número mayor

CORRECCIÓN 1: empezar en 0 falla si todos los números son negativos, porque
ninguno supera al 0. Se empieza con el primer elemento de la lista.

CORRECCIÓN 2: range(len(numeros) - 1) no llega al último elemento. Es un
error "de uno" (off by one). Recorrer la lista directamente evita el
problema.
"""

def mayor(numeros):
    resultado = numeros[0]  # CORRECCIÓN 1
    for n in numeros:  # CORRECCIÓN 2
        if n > resultado:
            resultado = n
    return resultado


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert mayor([3, 9, 2]) == 9
    assert mayor([3, 2, 9]) == 9, f"mayor([3, 2, 9]) retornó {mayor([3, 2, 9])}"
    assert mayor([-5, -2, -8]) == -2, f"mayor([-5, -2, -8]) retornó {mayor([-5, -2, -8])}"
    assert mayor([7]) == 7

    print("Todas las pruebas pasaron")
