"""
Solución - Ejercicio para corregir 03 - ¿Puede votar?

CORRECCIÓN 1: bool("no") es True. Cualquier texto que no esté vacío se
considera verdadero, aunque diga "no". Hay que comparar el texto:
respuesta_cedula == "si".

CORRECCIÓN 2: la regla pide edad Y cédula, así que el operador es and, no or.
"""

edad = 20
respuesta_cedula = "no"

# >>> tu código empieza aquí
tiene_cedula = respuesta_cedula == "si"  # CORRECCIÓN 1
puede_votar = edad >= 18 and tiene_cedula  # CORRECCIÓN 2
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
    casos = [((20, "si"), True), ((20, "no"), False), ((16, "si"), False), ((16, "no"), False)]
    for (e, resp), esperado in casos:
        r = probar(edad=e, respuesta_cedula=resp)
        assert r["puede_votar"] is esperado, f"edad={e}, cédula={resp!r}: se esperaba {esperado}"

    print("Todas las pruebas pasaron")
