"""
Solución - Ejercicio para corregir 01 - Mayor de edad

CORRECCIÓN 1 (IndentationError: expected an indented block after 'if'):
el bloque que pertenece al if debe ir indentado (4 espacios). En Python la
indentación no es estética: define qué instrucciones están dentro del if.

CORRECCIÓN 2 (resultado incorrecto): con > 18, una persona de 18 años
quedaba como menor. "18 o más" se escribe >= 18.
"""

def verificar_edad(edad):
    if edad >= 18:  # CORRECCIÓN 2
        return "Mayor de edad"  # CORRECCIÓN 1
    else:
        return "Menor de edad"


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert verificar_edad(30) == "Mayor de edad"
    assert verificar_edad(18) == "Mayor de edad", "18 años ya es mayor de edad"
    assert verificar_edad(17) == "Menor de edad"

    print("Todas las pruebas pasaron")
