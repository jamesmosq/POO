"""
Solución - Ejercicio propuesto 05 - collections.Counter y pathlib
"""

from collections import Counter
from pathlib import Path


def palabras_mas_comunes(texto, n):
    return Counter(texto.lower().split()).most_common(n)


def archivos_python(carpeta):
    return sorted(archivo.name for archivo in Path(carpeta).glob("*.py"))


def contar_lineas_de_codigo(carpeta):
    resultado = {}
    for archivo in Path(carpeta).glob("*.py"):
        resultado[archivo.name] = len(archivo.read_text(encoding="utf-8").splitlines())
    return resultado


# ----------------------------------------------------------------------
# Pruebas
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
