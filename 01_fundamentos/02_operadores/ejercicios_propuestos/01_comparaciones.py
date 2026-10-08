"""
Ejercicio propuesto 01 - Comparaciones
Nivel: básico

Requisitos. Usando las variables a y b, crea estas variables booleanas
(cada una debe valer True o False):
    a_es_mayor        -> a es mayor que b
    son_iguales       -> a y b son iguales
    son_diferentes    -> a y b son diferentes
    a_es_par          -> a es par (pista: residuo de dividir entre 2)
    b_es_multiplo_de_7 -> b es múltiplo de 7

Escribe tu código entre las dos marcas. Las pruebas lo ejecutan varias
veces con otros valores de a y b, así que no escribas True o False a mano:
usa operadores.

Conceptos: operadores relacionales (> < >= <= == !=), operador %.
"""

a = 15
b = 7

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
