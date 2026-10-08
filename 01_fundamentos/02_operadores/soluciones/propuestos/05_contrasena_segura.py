"""
Solución - Ejercicio propuesto 05 - Contraseña segura
"""

clave = "Python2026"

# >>> tu código empieza aquí
tiene_longitud = len(clave) >= 8
tiene_mayuscula = clave != clave.lower()
tiene_minuscula = clave != clave.upper()
sin_espacios = " " not in clave
es_segura = tiene_longitud and tiene_mayuscula and tiene_minuscula and sin_espacios
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
