"""
Solución - Ejercicio para corregir 05 - Configuración en JSON

CORRECCIÓN 1 (se modificaban los valores por defecto): retornar
CONFIG_POR_DEFECTO entrega el MISMO diccionario, no una copia. Quien lo
modificaba cambiaba los valores por defecto de todo el programa. Se retorna
una copia con dict(...) o .copy().

CORRECCIÓN 2 (los valores guardados se perdían): al combinar diccionarios
con **, si una clave se repite gana el ÚLTIMO. Los valores por defecto
deben ir primero y los guardados después, para que estos los reemplacen.

CORRECCIÓN 3 (json.decoder.JSONDecodeError: Extra data): el modo "a"
agrega al final del archivo, así que el segundo guardado dejaba dos objetos
JSON seguidos, y eso ya no es un JSON válido. Para reemplazar el contenido
se usa el modo "w".
"""

import json
import os

CONFIG_POR_DEFECTO = {"tema": "claro", "idioma": "es", "tamano_letra": 12}


def cargar_config(ruta):
    if not os.path.exists(ruta):
        return dict(CONFIG_POR_DEFECTO)  # CORRECCIÓN 1
    with open(ruta, encoding="utf-8") as archivo:
        guardada = json.load(archivo)
    return {**CONFIG_POR_DEFECTO, **guardada}  # CORRECCIÓN 2


def guardar_config(ruta, config):
    with open(ruta, "w", encoding="utf-8") as archivo:  # CORRECCIÓN 3
        json.dump(config, archivo)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import tempfile

    ruta = os.path.join(tempfile.mkdtemp(), "config.json")

    config = cargar_config(ruta)
    config["tema"] = "oscuro"
    assert CONFIG_POR_DEFECTO["tema"] == "claro", "Se modificaron los valores por defecto"

    guardar_config(ruta, config)
    assert cargar_config(ruta)["tema"] == "oscuro", "El valor guardado debe reemplazar al de por defecto"

    config["tamano_letra"] = 16
    guardar_config(ruta, config)
    assert cargar_config(ruta) == {"tema": "oscuro", "idioma": "es", "tamano_letra": 16}

    print("Todas las pruebas pasaron")
