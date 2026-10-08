"""
Ejercicio propuesto 03 - Calculadora con match-case
Nivel: intermedio

Completa la función calcular(a, operador, b) usando match-case (no if):

    "+"  -> a + b
    "-"  -> a - b
    "*"  -> a * b
    "/"  -> a / b, pero si b es 0 retorna "Error: división por cero"
    Cualquier otro operador -> "Operador no válido"

Pista: dentro de un case puedes poner un if, o usar una guarda:
    case "/" if b == 0:

Conceptos: match-case, case _, guardas (if dentro del case).
"""


def calcular(a, operador, b):
    # Escribe tu solución aquí
    pass


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert calcular(6, "+", 3) == 9
    assert calcular(6, "-", 3) == 3
    assert calcular(6, "*", 3) == 18
    assert calcular(6, "/", 3) == 2
    assert calcular(6, "/", 0) == "Error: división por cero"
    assert calcular(6, "%", 3) == "Operador no válido"

    fuente = open(__file__, encoding="utf-8").read().split("# Pruebas")[0]
    assert "match" in fuente, "Debes usar match-case"

    print("Todas las pruebas pasaron")
