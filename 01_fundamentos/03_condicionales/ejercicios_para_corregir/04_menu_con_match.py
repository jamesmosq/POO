"""
Ejercicio para corregir 04 - Menú con match-case
Nivel: intermedio
Errores a encontrar: 3

Qué debería hacer el programa:
    Recibir el número de opción de un menú (un int) y retornar la acción:
        1 -> "Crear"
        2 -> "Listar"
        9 -> "Salir"     (el 9 está guardado en la constante SALIR)
        cualquier otro número -> "Opción no válida"

Pista: si el error dice que un patrón "makes remaining patterns
unreachable", lee con calma qué patrones atrapan cualquier valor.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""

SALIR = 9


def ejecutar(opcion):
    match opcion:
        case 1:
            return "Crear"
        case _:
            return "Opción no válida"
        case "2":
            return "Listar"
        case SALIR:
            return "Salir"


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert ejecutar(1) == "Crear"
    assert ejecutar(2) == "Listar"
    assert ejecutar(9) == "Salir"
    assert ejecutar(5) == "Opción no válida"
    assert ejecutar(0) == "Opción no válida"

    print("Todas las pruebas pasaron")
