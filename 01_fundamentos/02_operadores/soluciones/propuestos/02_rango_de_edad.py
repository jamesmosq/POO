"""
Solución - Ejercicio propuesto 02 - Rango de edad
"""

edad = 25

# >>> tu código empieza aquí
es_menor = edad < 18
es_adulto = 18 <= edad <= 59
es_adulto_mayor = edad >= 60
# <<< tu código termina aquí


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
def probar(**datos):
    """Ejecuta tu código con otros datos y retorna las variables que creó."""
    fuente = open(__file__, encoding="utf-8").read()
    codigo = fuente.split("# >>> tu código empieza aquí")[1].split("# <<< tu código termina aquí")[0]
    variables = dict(datos)
    exec(codigo, variables)
    return variables


if __name__ == "__main__":
    esperado = {
        5: (True, False, False),
        17: (True, False, False),
        18: (False, True, False),
        59: (False, True, False),
        60: (False, False, True),
        90: (False, False, True),
    }
    for e, (menor, adulto, mayor) in esperado.items():
        r = probar(edad=e)
        obtenido = (r["es_menor"], r["es_adulto"], r["es_adulto_mayor"])
        assert obtenido == (menor, adulto, mayor), f"edad {e}: {obtenido}"

    print("Todas las pruebas pasaron")
