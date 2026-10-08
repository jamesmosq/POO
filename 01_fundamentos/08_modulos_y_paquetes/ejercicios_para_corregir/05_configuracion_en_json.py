"""
Ejercicio para corregir 05 - Configuración en JSON
Nivel: avanzado
Errores a encontrar: 3

Qué debería hacer el programa:
    Una aplicación guarda sus preferencias en un archivo JSON.

    - cargar_config(ruta): retorna la configuración. Parte de los valores
      por defecto y los REEMPLAZA con lo que haya en el archivo. Si el
      archivo no existe, retorna una copia de los valores por defecto.
    - guardar_config(ruta, config): guarda la configuración completa,
      reemplazando el contenido anterior del archivo.

    Modificar la configuración que retorna cargar_config nunca debe cambiar
    CONFIG_POR_DEFECTO.

Ojo: dos de los errores no lanzan excepciones, solo producen datos
incorrectos. Las pruebas cargan y guardan varias veces para que salgan a la
luz.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""
import json
import os

CONFIG_POR_DEFECTO = {"tema": "claro", "idioma": "es", "tamano_letra": 12}


def cargar_config(ruta):
    if not os.path.exists(ruta):
        return CONFIG_POR_DEFECTO
    with open(ruta, encoding="utf-8") as archivo:
        guardada = json.load(archivo)
    return {**guardada, **CONFIG_POR_DEFECTO}


def guardar_config(ruta, config):
    with open(ruta, "a", encoding="utf-8") as archivo:
        json.dump(config, archivo)


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
