"""
Solución - Ejercicio propuesto 02 - Guardar y cargar JSON
"""

import json
import os


def guardar_json(ruta, datos):
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=2)


def cargar_json(ruta):
    if not os.path.exists(ruta):
        return {}
    with open(ruta, encoding="utf-8") as archivo:
        return json.load(archivo)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os
    import tempfile

    carpeta = tempfile.mkdtemp()
    ruta = os.path.join(carpeta, "estudiantes.json")

    assert cargar_json(ruta) == {}

    datos = {"curso": "POO", "estudiantes": [{"nombre": "Ana", "nota": 4.5}, {"nombre": "Íñigo", "nota": 3.8}]}
    guardar_json(ruta, datos)
    assert cargar_json(ruta) == datos

    contenido = open(ruta, encoding="utf-8").read()
    assert "Íñigo" in contenido, "Usa ensure_ascii=False para guardar las tildes tal cual"
    assert "\n" in contenido, "Usa indent=2 para que el archivo sea legible"

    print("Todas las pruebas pasaron")
