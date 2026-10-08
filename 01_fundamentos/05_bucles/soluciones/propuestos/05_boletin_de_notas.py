"""
Solución - Ejercicio propuesto 05 - Boletín de notas
"""

def validar(nombres, notas):
    if len(nombres) != len(notas):
        raise ValueError("Las listas deben tener el mismo largo")


def boletin(nombres, notas):
    validar(nombres, notas)
    lineas = []
    for posicion, (nombre, nota) in enumerate(zip(nombres, notas), start=1):
        estado = "Aprobado" if nota >= 3.0 else "Reprobado"
        lineas.append(f"{posicion}. {nombre}: {nota} ({estado})")
    return lineas


def mejor_estudiante(nombres, notas):
    validar(nombres, notas)
    mejor_nombre = None
    mejor_nota = None
    for nombre, nota in zip(nombres, notas):
        # Con > estricto, en un empate se queda el primero.
        if mejor_nota is None or nota > mejor_nota:
            mejor_nombre, mejor_nota = nombre, nota
    return mejor_nombre


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    nombres = ["Ana", "Luis", "Eva"]
    notas = [4.5, 2.8, 4.5]

    assert boletin(nombres, notas) == [
        "1. Ana: 4.5 (Aprobado)",
        "2. Luis: 2.8 (Reprobado)",
        "3. Eva: 4.5 (Aprobado)",
    ]
    assert boletin([], []) == []
    assert mejor_estudiante(nombres, notas) == "Ana"
    assert mejor_estudiante(["Luis", "Eva"], [3.0, 3.1]) == "Eva"

    for funcion in (boletin, mejor_estudiante):
        try:
            funcion(["Ana", "Luis"], [4.0])
            raise AssertionError(f"{funcion.__name__} debe lanzar ValueError")
        except ValueError:
            pass

    print("Todas las pruebas pasaron")
