"""
Solución - Ejercicio para corregir 05 - Contraseña segura

CORRECCIÓN 1: "8 caracteres o más" es >= 8. Con > 8 una clave de
exactamente 8 caracteres se rechazaba. Los errores en los límites de un
rango son de los más comunes: siempre hay que probar el valor exacto del
límite.

CORRECCIÓN 2: clave.lower() == clave es True cuando NO hay mayúsculas. La
condición estaba invertida; debe ser !=.

CORRECCIÓN 3: la regla exige que se cumplan TODAS las condiciones, así que
se unen con and. Con or bastaba una clave larga para ser "segura".
"""

clave = "Python2026"

# >>> tu código empieza aquí
tiene_longitud = len(clave) >= 8  # CORRECCIÓN 1
tiene_mayuscula = clave.lower() != clave  # CORRECCIÓN 2
sin_espacios = " " not in clave
es_segura = tiene_longitud and tiene_mayuscula and sin_espacios  # CORRECCIÓN 3
# <<< tu código termina aquí


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
def probar(**datos):
    """Ejecuta el código con otros datos y retorna las variables que creó."""
    fuente = open(__file__, encoding="utf-8").read()
    codigo = fuente.split("# >>> tu código empieza aquí")[1].split("# <<< tu código termina aquí")[0]
    variables = dict(datos)
    exec(codigo, variables)
    return variables


if __name__ == "__main__":
    claves = {
        "Python2026": True,
        "Abcdefgh": True,
        "python2026": False,
        "Py2026": False,
        "Python 2026": False,
        "MUY LARGA PERO CON ESPACIOS": False,
    }
    for c, esperado in claves.items():
        r = probar(clave=c)
        assert r["es_segura"] is esperado, f"{c!r}: se esperaba {esperado}"

    print("Todas las pruebas pasaron")
