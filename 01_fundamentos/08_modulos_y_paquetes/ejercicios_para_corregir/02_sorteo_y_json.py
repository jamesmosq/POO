"""
Ejercicio para corregir 02 - Sorteo y JSON
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    - sortear(participantes, semilla) elige un ganador al azar de la lista,
      usando un generador random.Random(semilla) para que sea reproducible.
    - guardar_resultado(ruta, ganador) guarda {"ganador": ganador} en un
      archivo JSON.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""
import json
from random import Random


def sortear(participantes, semilla):
    generador = random.Random(semilla)
    return generador.choice(participantes)


def guardar_resultado(ruta, ganador):
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dumps({"ganador": ganador}, archivo)


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
