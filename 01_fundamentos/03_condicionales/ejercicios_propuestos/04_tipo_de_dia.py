"""
Ejercicio propuesto 04 - Tipo de día
Nivel: intermedio

Completa la función tipo_de_dia(dia) usando match-case:

    "lunes" a "viernes"   -> "Hábil"
    "sábado" o "domingo"  -> "Fin de semana"
    Cualquier otro texto  -> "Día no válido"

El día puede llegar con mayúsculas o espacios ("  LUNES "). Además, acepta
"sabado" sin tilde.

Pista: un case puede tener varias opciones separadas con |
    case "a" | "b" | "c":

Conceptos: match-case, patrones con |, normalizar texto.
"""


def tipo_de_dia(dia):
    # Escribe tu solución aquí
    pass


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    for d in ["lunes", "martes", "miércoles", "jueves", "viernes"]:
        assert tipo_de_dia(d) == "Hábil", d
    assert tipo_de_dia("sábado") == "Fin de semana"
    assert tipo_de_dia("sabado") == "Fin de semana"
    assert tipo_de_dia("Domingo") == "Fin de semana"
    assert tipo_de_dia("  LUNES ") == "Hábil"
    assert tipo_de_dia("feriado") == "Día no válido"

    print("Todas las pruebas pasaron")
