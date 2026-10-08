"""
Solución - Ejercicio propuesto 04 - Tipo de día
"""

def tipo_de_dia(dia):
    match dia.strip().lower():
        case "lunes" | "martes" | "miércoles" | "miercoles" | "jueves" | "viernes":
            return "Hábil"
        case "sábado" | "sabado" | "domingo":
            return "Fin de semana"
        case _:
            return "Día no válido"


# ----------------------------------------------------------------------
# Pruebas
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
