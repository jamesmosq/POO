"""
Ejercicio propuesto 02 - Rango de edad
Nivel: básico

Requisitos. Usando la variable edad, crea tres variables booleanas:
    es_menor        -> menos de 18 años
    es_adulto       -> de 18 a 59 años (incluidos los dos extremos)
    es_adulto_mayor -> 60 años o más

Para es_adulto usa una comparación encadenada, por ejemplo:
    10 <= x <= 20
Python la lee como "x está entre 10 y 20".

Para cualquier edad, exactamente una de las tres variables debe ser True.

Conceptos: comparaciones encadenadas, límites de un rango.
"""

edad = 25

# >>> tu código empieza aquí

# <<< tu código termina aquí


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
