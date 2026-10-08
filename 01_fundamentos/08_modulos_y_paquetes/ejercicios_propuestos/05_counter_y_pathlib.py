"""
Ejercicio propuesto 05 - collections.Counter y pathlib
Nivel: avanzado

Dos módulos muy útiles de la biblioteca estándar:
    collections.Counter  cuenta elementos de una colección.
    pathlib.Path         maneja rutas y archivos como objetos.

Requisitos:
1. palabras_mas_comunes(texto, n): retorna una lista de tuplas
   (palabra, cantidad) con las n palabras más frecuentes, en minúscula.
   Usa Counter y su método most_common(n).
2. archivos_python(carpeta): retorna una lista ORDENADA con los nombres
   (solo el nombre, sin la ruta) de los archivos .py que hay en la
   carpeta. Usa Path(carpeta).glob("*.py") y el atributo .name.
3. contar_lineas_de_codigo(carpeta): retorna un diccionario
   {nombre_archivo: cantidad_de_líneas} para cada .py de la carpeta.
   Usa Path.read_text(encoding="utf-8").

Conceptos: collections, pathlib, explorar la documentación oficial.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import tempfile
    from pathlib import Path

    texto = "el perro y el gato y el loro"
    assert palabras_mas_comunes(texto, 2) == [("el", 3), ("y", 2)]
    assert palabras_mas_comunes("Hola hola HOLA", 1) == [("hola", 3)]

    carpeta = Path(tempfile.mkdtemp())
    (carpeta / "b.py").write_text("x = 1\ny = 2\n", encoding="utf-8")
    (carpeta / "a.py").write_text("print('hola')\n", encoding="utf-8")
    (carpeta / "notas.txt").write_text("no es python", encoding="utf-8")

    assert archivos_python(carpeta) == ["a.py", "b.py"]
    assert contar_lineas_de_codigo(carpeta) == {"a.py": 1, "b.py": 2}

    print("Todas las pruebas pasaron")
