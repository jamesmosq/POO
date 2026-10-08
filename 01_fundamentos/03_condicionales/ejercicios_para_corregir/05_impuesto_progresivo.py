"""
Ejercicio para corregir 05 - Impuesto progresivo
Nivel: avanzado
Errores a encontrar: 3

Qué debería hacer el programa:
    Calcular un impuesto por tramos:
        Hasta 10.000.000              -> 0 %
        De 10.000.000 a 30.000.000    -> 10 % sobre lo que pase de 10 millones
        Más de 30.000.000             -> 2.000.000 fijos (el tramo anterior
                                         completo) más 20 % sobre lo que pase
                                         de 30 millones
    Un ingreso negativo debe lanzar ValueError.

        impuesto(20_000_000) -> 1_000_000
        impuesto(40_000_000) -> 4_000_000

Ojo: ningún error lanza una excepción por sí solo. Calcula a mano un caso
de cada tramo y compáralo con lo que retorna la función.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


def impuesto(ingreso):
    if ingreso < 0:
        ValueError("El ingreso no puede ser negativo")
    if ingreso <= 10_000_000:
        return 0
    elif ingreso <= 30_000_000:
        return ingreso * 0.10
    else:
        return (ingreso - 30_000_000) * 0.20


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert impuesto(10_000_000) == 0
    assert impuesto(20_000_000) == 1_000_000, f"20M: {impuesto(20_000_000)}"
    assert impuesto(30_000_000) == 2_000_000, f"30M: {impuesto(30_000_000)}"
    assert impuesto(40_000_000) == 4_000_000, f"40M: {impuesto(40_000_000)}"

    try:
        impuesto(-1)
        raise AssertionError("Un ingreso negativo debe lanzar ValueError")
    except ValueError:
        pass

    print("Todas las pruebas pasaron")
