"""
Solución - Ejercicio propuesto 05 - Promedio desde un archivo
"""

def promedio_de_archivo(ruta):
    try:
        with open(ruta, encoding="utf-8") as archivo:
            lineas = archivo.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"No existe el archivo {ruta}")

    notas = []
    invalidas = 0
    for linea in lineas:
        try:
            notas.append(float(linea))  # float() ignora el salto de línea final
        except ValueError:
            invalidas += 1

    promedio = sum(notas) / len(notas) if notas else 0
    return promedio, invalidas


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os
    import tempfile

    carpeta = tempfile.mkdtemp()
    ruta = os.path.join(carpeta, "notas.txt")
    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write("4.5\nabc\n3.5\n\n")
    assert promedio_de_archivo(ruta) == (4.0, 2)

    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write("nada\n")
    assert promedio_de_archivo(ruta) == (0, 1)

    try:
        promedio_de_archivo(os.path.join(carpeta, "no_existe.txt"))
        raise AssertionError("Debe lanzar FileNotFoundError")
    except FileNotFoundError as error:
        assert str(error).startswith("No existe el archivo"), str(error)

    print("Todas las pruebas pasaron")
