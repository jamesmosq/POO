"""
Ejercicio para corregir 04 - Guardar y contar líneas
Nivel: intermedio
Errores a encontrar: 3

Qué debería hacer el programa:
    - guardar_lineas(ruta, lineas) escribe cada elemento de la lista en una
      línea distinta del archivo (lo crea o lo reemplaza).
    - contar_lineas(ruta) retorna cuántas líneas tiene el archivo, o 0 si el
      archivo no existe.

        guardar_lineas("datos.txt", ["a", "b", "c"])
        contar_lineas("datos.txt")      -> 3
        contar_lineas("no_existe.txt")  -> 0

Pista: uno de los errores solo aparece cuando ocurre una excepción. Python
no revisa los nombres de los except hasta que los necesita.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


def guardar_lineas(ruta, lineas):
    with open(ruta, encoding="utf-8") as archivo:
        for linea in lineas:
            archivo.write(linea)


def contar_lineas(ruta):
    try:
        with open(ruta, encoding="utf-8") as archivo:
            return len(archivo.readlines())
    except FileNotFound:
        return 0


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
