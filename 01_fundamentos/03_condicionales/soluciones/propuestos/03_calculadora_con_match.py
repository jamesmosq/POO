"""
Solución - Ejercicio propuesto 03 - Calculadora con match-case
"""

def calcular(a, operador, b):
    match operador:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/" if b == 0:
            # La guarda se revisa antes del case "/" normal.
            return "Error: división por cero"
        case "/":
            return a / b
        case _:
            return "Operador no válido"


# ----------------------------------------------------------------------
# Pruebas
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
