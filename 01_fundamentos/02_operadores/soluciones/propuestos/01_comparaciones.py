"""
Solución - Ejercicio propuesto 01 - Comparaciones
"""

a = 15
b = 7

# >>> tu código empieza aquí
a_es_mayor = a > b
son_iguales = a == b
son_diferentes = a != b
a_es_par = a % 2 == 0
b_es_multiplo_de_7 = b % 7 == 0
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
    r = probar(a=15, b=7)
    assert r["a_es_mayor"] is True
    assert r["son_iguales"] is False
    assert r["son_diferentes"] is True
    assert r["a_es_par"] is False
    assert r["b_es_multiplo_de_7"] is True

    r = probar(a=4, b=4)
    assert r["a_es_mayor"] is False
    assert r["son_iguales"] is True
    assert r["son_diferentes"] is False
    assert r["a_es_par"] is True
    assert r["b_es_multiplo_de_7"] is False

    r = probar(a=-2, b=21)
    assert r["a_es_mayor"] is False and r["a_es_par"] is True and r["b_es_multiplo_de_7"] is True

    print("Todas las pruebas pasaron")
