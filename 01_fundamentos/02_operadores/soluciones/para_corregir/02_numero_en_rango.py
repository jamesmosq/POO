"""
Solución - Ejercicio para corregir 02 - Número en rango

CORRECCIÓN 1: 'es_cero = numero = 0' no compara, es una asignación
encadenada: guarda 0 en numero y en es_cero. Por eso numero cambiaba y todo
lo que venía después usaba el valor equivocado. Para comparar se usa ==.

CORRECCIÓN 2: '1 <= numero >= 100' significa "1 <= numero y numero >= 100",
es decir, solo números de 100 en adelante. El rango correcto es
1 <= numero <= 100.
"""

numero = 50

# >>> tu código empieza aquí
es_cero = numero == 0  # CORRECCIÓN 1
esta_en_rango = 1 <= numero <= 100  # CORRECCIÓN 2
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
    for n, cero, rango in [(50, False, True), (0, True, False), (1, False, True),
                           (100, False, True), (101, False, False), (-5, False, False)]:
        r = probar(numero=n)
        assert r["numero"] == n, f"El código cambió numero de {n} a {r['numero']}"
        assert r["es_cero"] is cero, f"numero={n}: es_cero vale {r['es_cero']!r}"
        assert r["esta_en_rango"] is rango, f"numero={n}: esta_en_rango vale {r['esta_en_rango']!r}"

    print("Todas las pruebas pasaron")
