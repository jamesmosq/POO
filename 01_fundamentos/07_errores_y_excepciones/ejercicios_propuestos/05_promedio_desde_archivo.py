"""
Ejercicio propuesto 05 - Promedio desde un archivo
Nivel: avanzado

Un archivo de texto tiene una nota por línea, pero algunas líneas vienen
mal (vacías o con texto). El programa no debe fallar por eso.

Requisitos. Escribe promedio_de_archivo(ruta), que retorne una tupla
(promedio, lineas_invalidas):
    - Abre el archivo con with open(ruta, encoding="utf-8").
    - Cada línea válida se convierte a float y cuenta para el promedio.
    - Las líneas que no se pueden convertir se cuentan como inválidas y se
      ignoran. Las líneas vacías también son inválidas.
    - Si no hay ninguna nota válida, el promedio es 0.
    - Si el archivo no existe, lanza FileNotFoundError con el mensaje
      f"No existe el archivo {ruta}".

    Archivo:            Resultado:
        4.5                 (4.0, 2)
        abc
        3.5
        (vacía)

Conceptos: archivos, with, excepciones dentro de un ciclo, re-lanzar.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
