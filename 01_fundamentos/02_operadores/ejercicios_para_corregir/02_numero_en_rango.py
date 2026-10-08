"""
Ejercicio para corregir 02 - Número en rango
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    es_cero        -> True si numero es 0.
    esta_en_rango  -> True si numero está entre 1 y 100 (incluidos).

Ojo: este programa no lanza ningún error. Los dos errores producen
resultados incorrectos, y uno de ellos cambia el valor de numero sin que
te des cuenta. Usa print() para ver qué valor tiene cada variable.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""

numero = 50

# >>> tu código empieza aquí
es_cero = numero = 0
esta_en_rango = 1 <= numero >= 100
# <<< tu código termina aquí


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
