"""
Ejercicio para corregir 02 - Clima
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    Clasificar una temperatura en grados Celsius:
        más de 25        -> "Caluroso"
        de 11 a 25       -> "Templado"
        10 o menos       -> "Frío"

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


def clima(temperatura):
    if temperatura > 10:
        return "Templado"
    else if temperatura > 25:
        return "Caluroso"
    else:
        return "Frío"


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert clima(30) == "Caluroso", f"clima(30) retornó {clima(30)!r}"
    assert clima(26) == "Caluroso"
    assert clima(25) == "Templado"
    assert clima(11) == "Templado"
    assert clima(10) == "Frío"
    assert clima(-3) == "Frío"

    print("Todas las pruebas pasaron")
