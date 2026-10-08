"""
Ejercicio para corregir 03 - Lanzar y reportar errores
Nivel: intermedio
Errores a encontrar: 2

Qué debería hacer el programa:
    - validar_nota(nota) lanza ValueError("La nota debe estar entre 0 y 5")
      si la nota está fuera de rango; si no, la retorna.
    - reportar(nota) llama a validar_nota y retorna "Nota válida" o el
      TEXTO del mensaje de error.

        reportar(4.5) -> "Nota válida"
        reportar(7)   -> "La nota debe estar entre 0 y 5"

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


def validar_nota(nota):
    if nota < 0 or nota > 5:
        raise "La nota debe estar entre 0 y 5"
    return nota


def reportar(nota):
    try:
        validar_nota(nota)
        return "Nota válida"
    except ValueError as error:
        return error


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert validar_nota(3) == 3
    assert reportar(4.5) == "Nota válida"
    assert reportar(7) == "La nota debe estar entre 0 y 5", repr(reportar(7))
    assert reportar(-1) == "La nota debe estar entre 0 y 5"

    print("Todas las pruebas pasaron")
