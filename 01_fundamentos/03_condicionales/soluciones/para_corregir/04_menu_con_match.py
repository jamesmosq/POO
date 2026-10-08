"""
Solución - Ejercicio para corregir 04 - Menú con match-case

CORRECCIÓN 1 (SyntaxError: wildcard makes remaining patterns unreachable):
case _ atrapa cualquier valor, así que todo lo que esté debajo nunca se
ejecutaría. Python lo detecta y no deja correr el programa. case _ va
siempre al final.

CORRECCIÓN 2 (resultado incorrecto): case "2" compara con el texto "2",
pero la opción llega como el número 2. 2 y "2" son valores distintos.

CORRECCIÓN 3 (SyntaxError: name capture 'SALIR' makes remaining patterns
unreachable): en un case, un nombre suelto como SALIR no se compara con la
constante: crea una variable nueva que atrapa cualquier valor, igual que _.
Para comparar con una constante se usa el valor literal o un nombre con
punto, como Opciones.SALIR.
"""

SALIR = 9


def ejecutar(opcion):
    match opcion:
        case 1:
            return "Crear"
        case 2:  # CORRECCIÓN 2
            return "Listar"
        case _ if opcion == SALIR:  # CORRECCIÓN 3 (o simplemente: case 9)
            return "Salir"
        case _:  # CORRECCIÓN 1
            return "Opción no válida"


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert ejecutar(1) == "Crear"
    assert ejecutar(2) == "Listar"
    assert ejecutar(9) == "Salir"
    assert ejecutar(5) == "Opción no válida"
    assert ejecutar(0) == "Opción no válida"

    print("Todas las pruebas pasaron")
