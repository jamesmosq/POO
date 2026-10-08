"""
Ejercicio para corregir 05 - Agenda telefónica
Nivel: avanzado
Errores a encontrar: 3

Qué debería hacer el programa:
    La agenda es un diccionario: nombre -> lista de teléfonos.
        {"Ana": ["3001234567"], "Luis": []}

    - agregar_telefono(agenda, nombre, telefono): agrega el teléfono; si el
      contacto no existe, lo crea.
    - ranking(agenda): nombres ordenados de MÁS a MENOS teléfonos (si hay
      empate, por orden alfabético).
    - limpiar_vacios(agenda): elimina de la agenda los contactos sin
      teléfonos.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


def agregar_telefono(agenda, nombre, telefono):
    agenda[nombre].append(telefono)


def ranking(agenda):
    return sorted(agenda)


def limpiar_vacios(agenda):
    for nombre in agenda:
        if not agenda[nombre]:
            del agenda[nombre]


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    agenda = {"Ana": ["300"], "Luis": []}
    agregar_telefono(agenda, "Ana", "301")
    agregar_telefono(agenda, "Eva", "310")
    assert agenda == {"Ana": ["300", "301"], "Luis": [], "Eva": ["310"]}

    agregar_telefono(agenda, "Beto", "320")
    assert ranking(agenda) == ["Ana", "Beto", "Eva", "Luis"], ranking(agenda)

    limpiar_vacios(agenda)
    assert agenda == {"Ana": ["300", "301"], "Eva": ["310"], "Beto": ["320"]}

    print("Todas las pruebas pasaron")
