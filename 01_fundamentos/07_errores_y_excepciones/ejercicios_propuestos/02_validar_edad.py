"""
Ejercicio propuesto 02 - Validar edad
Nivel: básico

Además de atrapar errores, una función puede LANZARLOS cuando recibe datos
inválidos. Así quien la llama se entera del problema.

Requisitos. Escribe validar_edad(texto), que retorne la edad como int o
lance ValueError con estos mensajes exactos:
    - Si el texto no es un número entero:  "La edad debe ser un número entero"
    - Si es negativa:                      "La edad no puede ser negativa"
    - Si es mayor que 120:                 "La edad no es realista"

Pista: atrapa el ValueError de int() y lanza uno nuevo con tu mensaje:
    try:
        edad = int(texto)
    except ValueError:
        raise ValueError("...")

Conceptos: raise, mensajes de error claros, validación de entradas.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
