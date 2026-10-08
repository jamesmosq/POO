"""
Solución - Ejercicio propuesto 01 - Clasificar una nota
"""

def clasificar_nota(nota):
    # Primero se descartan los valores inválidos; así las demás condiciones
    # pueden suponer que la nota está entre 0 y 5.
    if nota < 0 or nota > 5:
        return "Nota inválida"
    elif nota < 3.0:
        return "Reprobado"
    elif nota < 4.0:
        return "Aceptable"
    elif nota < 4.5:
        return "Bueno"
    else:
        return "Excelente"


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    casos = {
        -1: "Nota inválida", 5.1: "Nota inválida",
        0: "Reprobado", 2.9: "Reprobado",
        3.0: "Aceptable", 3.9: "Aceptable",
        4.0: "Bueno", 4.4: "Bueno",
        4.5: "Excelente", 5.0: "Excelente",
    }
    for nota, esperado in casos.items():
        obtenido = clasificar_nota(nota)
        assert obtenido == esperado, f"clasificar_nota({nota}) retornó {obtenido!r}, se esperaba {esperado!r}"

    print("Todas las pruebas pasaron")
