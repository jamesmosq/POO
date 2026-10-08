"""
Solución - Ejercicio propuesto 02 - Estadísticas de notas
"""

def estadisticas(nota1, nota2, nota3):
    minimo = min(nota1, nota2, nota3)
    maximo = max(nota1, nota2, nota3)
    promedio = round((nota1 + nota2 + nota3) / 3, 2)
    return minimo, maximo, promedio


def aprobo(nota1, nota2, nota3):
    # Solo interesa el promedio; los otros dos valores se descartan con _.
    _, _, promedio = estadisticas(nota1, nota2, nota3)
    return promedio >= 3.0


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert estadisticas(3.0, 4.5, 4.0) == (3.0, 4.5, 3.83)
    minimo, maximo, promedio = estadisticas(5, 5, 5)
    assert (minimo, maximo, promedio) == (5, 5, 5)

    assert aprobo(3.0, 3.0, 3.0) is True
    assert aprobo(2.0, 3.5, 3.4) is False
    assert aprobo(4.0, 2.0, 3.5) is True

    print("Todas las pruebas pasaron")
