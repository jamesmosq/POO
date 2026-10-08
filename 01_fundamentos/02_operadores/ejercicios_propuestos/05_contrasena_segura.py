"""
Ejercicio propuesto 05 - Contraseña segura
Nivel: avanzado

Una contraseña es segura si cumple TODAS estas condiciones:
    - Tiene 8 caracteres o más.
    - Tiene al menos una letra mayúscula.
    - Tiene al menos una letra minúscula.
    - No tiene espacios.

Requisitos. Crea estas variables booleanas a partir de clave:
    tiene_longitud
    tiene_mayuscula
    tiene_minuscula
    sin_espacios
    es_segura

Pistas (todavía no necesitas ciclos):
    - len(texto) da la cantidad de caracteres.
    - texto.lower() devuelve el texto en minúsculas. Si el texto original es
      distinto de su versión en minúsculas, es porque tenía mayúsculas.
    - El operador in dice si un texto aparece dentro de otro: "a" in "casa".

Conceptos: operadores lógicos con texto, len(), in, métodos de str.
"""

clave = "Python2026"

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
    claves = {
        "Python2026": True,
        "python2026": False,   # sin mayúscula
        "PYTHON2026": False,   # sin minúscula
        "Py2026": False,       # muy corta
        "Python 2026": False,  # tiene espacio
        "Abcdefgh": True,      # exactamente 8
    }
    for c, esperado in claves.items():
        r = probar(clave=c)
        assert r["es_segura"] is esperado, f"{c!r}: se esperaba {esperado}"

    r = probar(clave="Py 1")
    assert r["tiene_longitud"] is False
    assert r["tiene_mayuscula"] is True
    assert r["tiene_minuscula"] is True
    assert r["sin_espacios"] is False

    print("Todas las pruebas pasaron")
