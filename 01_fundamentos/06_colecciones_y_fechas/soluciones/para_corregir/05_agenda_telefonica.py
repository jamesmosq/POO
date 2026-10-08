"""
Solución - Ejercicio para corregir 05 - Agenda telefónica

CORRECCIÓN 1 (KeyError: 'Eva'): si el contacto no existe, agenda[nombre]
falla. setdefault(nombre, []) retorna la lista existente o crea una vacía
si no está.

CORRECCIÓN 2 (orden incorrecto): sorted(agenda) ordena las claves
alfabéticamente. Para ordenar por cantidad de teléfonos de mayor a menor,
y desempatar por nombre, se usa una clave de ordenamiento.

CORRECCIÓN 3 (RuntimeError: dictionary changed size during iteration): no
se puede borrar de un diccionario mientras se recorre. Se recorre una copia
de las claves con list(agenda).
"""

def agregar_telefono(agenda, nombre, telefono):
    agenda.setdefault(nombre, []).append(telefono)  # CORRECCIÓN 1


def ranking(agenda):
    # El signo menos invierte el orden de la cantidad sin invertir el del nombre.
    return sorted(agenda, key=lambda nombre: (-len(agenda[nombre]), nombre))  # CORRECCIÓN 2


def limpiar_vacios(agenda):
    for nombre in list(agenda):  # CORRECCIÓN 3
        if not agenda[nombre]:
            del agenda[nombre]


# ----------------------------------------------------------------------
# Pruebas
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
