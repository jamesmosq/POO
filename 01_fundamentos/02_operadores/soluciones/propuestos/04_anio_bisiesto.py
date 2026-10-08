"""
Solución - Ejercicio propuesto 04 - Año bisiesto
"""

anio = 2024

# >>> tu código empieza aquí
es_bisiesto = (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0
dias_del_anio = 365 + es_bisiesto  # True suma 1, False suma 0
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
    for a, esperado in [(2024, True), (2023, False), (1900, False), (2000, True), (2100, False), (1996, True)]:
        r = probar(anio=a)
        assert r["es_bisiesto"] is esperado, f"{a}: se esperaba {esperado}"
        assert r["dias_del_anio"] == (366 if esperado else 365), f"{a}: {r['dias_del_anio']} días"

    print("Todas las pruebas pasaron")
