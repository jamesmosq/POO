"""
Ejercicio propuesto 01 - Conversiones seguras
Nivel: básico

Requisitos:
1. a_entero(texto): convierte el texto a int. Si no se puede (por ejemplo
   "abc" o "3.5"), retorna None en lugar de dejar que el programa falle.
2. dividir(a, b): retorna a / b. Si b es 0, retorna None.

Usa try / except con el tipo de error EXACTO que quieres atrapar
(ValueError, ZeroDivisionError). No uses un except sin tipo: esconde
errores que sí deberías ver.

Conceptos: try, except, tipos de excepción.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert a_entero("42") == 42
    assert a_entero("-7") == -7
    assert a_entero("abc") is None
    assert a_entero("3.5") is None
    assert a_entero("") is None

    assert dividir(10, 4) == 2.5
    assert dividir(10, 0) is None

    fuente = open(__file__, encoding="utf-8").read().split("# Pruebas")[0]
    assert "except:" not in fuente, "No uses except sin tipo de error"

    print("Todas las pruebas pasaron")
