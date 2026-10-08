"""
Ejercicio para corregir 01 - Mayor de edad
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    La función retorna "Mayor de edad" si la persona tiene 18 años o más, y
    "Menor de edad" en otro caso.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


def verificar_edad(edad):
    if edad > 18:
    return "Mayor de edad"
    else:
        return "Menor de edad"


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert verificar_edad(30) == "Mayor de edad"
    assert verificar_edad(18) == "Mayor de edad", "18 años ya es mayor de edad"
    assert verificar_edad(17) == "Menor de edad"

    print("Todas las pruebas pasaron")
