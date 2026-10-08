"""
Solución - Ejercicio para corregir 03 - Lanzar y reportar errores

CORRECCIÓN 1 (TypeError: exceptions must derive from BaseException): no
se puede lanzar un texto. Se lanza un objeto de excepción con el texto como
mensaje: raise ValueError("...").

CORRECCIÓN 2 (retornaba el objeto de error): error es un objeto
ValueError, no un texto. Al compararlo con un str da False. Para obtener
el mensaje se usa str(error).
"""

def validar_nota(nota):
    if nota < 0 or nota > 5:
        raise ValueError("La nota debe estar entre 0 y 5")  # CORRECCIÓN 1
    return nota


def reportar(nota):
    try:
        validar_nota(nota)
        return "Nota válida"
    except ValueError as error:
        return str(error)  # CORRECCIÓN 2


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert validar_nota(3) == 3
    assert reportar(4.5) == "Nota válida"
    assert reportar(7) == "La nota debe estar entre 0 y 5", repr(reportar(7))
    assert reportar(-1) == "La nota debe estar entre 0 y 5"

    print("Todas las pruebas pasaron")
