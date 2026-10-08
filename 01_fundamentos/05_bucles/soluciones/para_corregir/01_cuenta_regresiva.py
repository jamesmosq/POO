"""
Solución - Ejercicio para corregir 01 - Cuenta regresiva

CORRECCIÓN 1 (UnboundLocalError con 'numero'): range(n, 0) va de n hacia
arriba hasta 0, así que no produce ningún número y el ciclo nunca se
ejecuta. Para contar hacia atrás hay que indicar el paso: range(n, 0, -1).

CORRECCIÓN 2 (solo quedaba el último número): append estaba fuera del
ciclo, por la indentación, y se ejecutaba una sola vez al final. Debe ir
dentro del for.
"""

def cuenta_regresiva(n):
    resultado = []
    for i in range(n, 0, -1):  # CORRECCIÓN 1
        resultado.append(i)  # CORRECCIÓN 2
    return resultado


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert cuenta_regresiva(5) == [5, 4, 3, 2, 1], cuenta_regresiva(5)
    assert cuenta_regresiva(1) == [1]
    assert cuenta_regresiva(0) == []

    print("Todas las pruebas pasaron")
