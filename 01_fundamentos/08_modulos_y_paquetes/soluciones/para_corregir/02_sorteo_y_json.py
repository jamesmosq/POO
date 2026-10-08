"""
Solución - Ejercicio para corregir 02 - Sorteo y JSON

CORRECCIÓN 1 (NameError: name 'random' is not defined): con
"from random import Random" solo se trae la clase Random; el nombre random
no existe en el archivo. Se usa Random(semilla) directamente (o se cambia
la importación por "import random").

CORRECCIÓN 2 (TypeError: dumps() takes 1 positional argument but 2 were
given): json.dumps convierte a TEXTO y no recibe un archivo. Para escribir
en un archivo se usa json.dump (sin s).
"""

import json
from random import Random


def sortear(participantes, semilla):
    generador = Random(semilla)  # CORRECCIÓN 1
    return generador.choice(participantes)


def guardar_resultado(ruta, ganador):
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump({"ganador": ganador}, archivo)  # CORRECCIÓN 2


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os
    import tempfile

    personas = ["Ana", "Luis", "Eva", "Pedro"]
    ganador = sortear(personas, semilla=3)
    assert ganador in personas
    assert sortear(personas, semilla=3) == ganador, "La misma semilla da el mismo ganador"

    ruta = os.path.join(tempfile.mkdtemp(), "sorteo.json")
    guardar_resultado(ruta, ganador)
    with open(ruta, encoding="utf-8") as archivo:
        assert json.load(archivo) == {"ganador": ganador}

    print("Todas las pruebas pasaron")
