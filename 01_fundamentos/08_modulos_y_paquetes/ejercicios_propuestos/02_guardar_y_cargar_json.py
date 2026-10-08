"""
Ejercicio propuesto 02 - Guardar y cargar JSON
Nivel: básico

JSON es un formato de texto para guardar datos (listas, diccionarios,
números, textos). El módulo json convierte entre JSON y objetos de Python.

Requisitos:
1. guardar_json(ruta, datos): guarda los datos en el archivo.
   - Usa with open(ruta, "w", encoding="utf-8").
   - Usa json.dump(datos, archivo, ensure_ascii=False, indent=2) para que
     las tildes se vean bien y el archivo sea legible.
2. cargar_json(ruta): retorna los datos del archivo. Si el archivo no
   existe, retorna un diccionario vacío.
   Pista: os.path.exists(ruta) o atrapar FileNotFoundError.

Diferencia importante:
    json.dump / json.load    -> trabajan con ARCHIVOS
    json.dumps / json.loads  -> trabajan con TEXTOS (la s es de string)

Conceptos: json, os.path, archivos.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
