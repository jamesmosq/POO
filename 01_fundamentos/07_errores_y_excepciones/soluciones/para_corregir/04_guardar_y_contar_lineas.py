"""
Solución - Ejercicio para corregir 04 - Guardar y contar líneas

CORRECCIÓN 1 (FileNotFoundError o io.UnsupportedOperation: not writable):
open() sin modo abre el archivo para LEER. Para escribir (y reemplazar el
contenido) se usa el modo "w".

CORRECCIÓN 2 (contaba 1 línea en lugar de 3): write() no agrega el salto
de línea. Sin "\n" todo queda en una sola línea: "abc".

CORRECCIÓN 3 (NameError: name 'FileNotFound' is not defined): el nombre
correcto es FileNotFoundError. El error solo aparece cuando el archivo no
existe, porque Python evalúa el except únicamente cuando ocurre una
excepción. Por eso hay que probar también el camino del error.
"""

def guardar_lineas(ruta, lineas):
    with open(ruta, "w", encoding="utf-8") as archivo:  # CORRECCIÓN 1
        for linea in lineas:
            archivo.write(linea + "\n")  # CORRECCIÓN 2


def contar_lineas(ruta):
    try:
        with open(ruta, encoding="utf-8") as archivo:
            return len(archivo.readlines())
    except FileNotFoundError:  # CORRECCIÓN 3
        return 0


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os
    import tempfile

    carpeta = tempfile.mkdtemp()
    ruta = os.path.join(carpeta, "datos.txt")

    guardar_lineas(ruta, ["a", "b", "c"])
    assert contar_lineas(ruta) == 3, f"contar_lineas retornó {contar_lineas(ruta)}"
    guardar_lineas(ruta, ["solo una"])
    assert contar_lineas(ruta) == 1, "guardar_lineas debe reemplazar el contenido"
    assert contar_lineas(os.path.join(carpeta, "no_existe.txt")) == 0

    print("Todas las pruebas pasaron")
