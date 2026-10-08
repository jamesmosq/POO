"""
Solución - Ejercicio propuesto 02 - Validar edad
"""

def validar_edad(texto):
    try:
        edad = int(texto)  # int() ignora los espacios al inicio y al final
    except ValueError:
        raise ValueError("La edad debe ser un número entero")
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    if edad > 120:
        raise ValueError("La edad no es realista")
    return edad


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
def mensaje_de_error(funcion, *argumentos):
    try:
        funcion(*argumentos)
    except ValueError as error:
        return str(error)
    return None


if __name__ == "__main__":
    assert validar_edad("25") == 25
    assert validar_edad(" 0 ") == 0
    assert validar_edad("120") == 120

    assert mensaje_de_error(validar_edad, "veinte") == "La edad debe ser un número entero"
    assert mensaje_de_error(validar_edad, "-3") == "La edad no puede ser negativa"
    assert mensaje_de_error(validar_edad, "121") == "La edad no es realista"

    print("Todas las pruebas pasaron")
