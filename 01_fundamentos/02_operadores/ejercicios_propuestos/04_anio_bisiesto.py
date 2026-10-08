"""
Ejercicio propuesto 04 - Año bisiesto
Nivel: intermedio

Un año es bisiesto si:
    - es divisible entre 4 y NO es divisible entre 100,
    - o es divisible entre 400.

Ejemplos: 2024 sí, 2023 no, 1900 no (divisible entre 100 pero no entre 400),
2000 sí (divisible entre 400).

Requisitos:
1. Crea es_bisiesto (bool) con una sola expresión.
2. Crea dias_del_anio (int): 366 si es bisiesto, 365 si no.
   Pista sin usar if: True vale 1 y False vale 0 en una suma.

Conceptos: operador %, and, or, not, bool como número.
"""

anio = 2024

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
    for a, esperado in [(2024, True), (2023, False), (1900, False), (2000, True), (2100, False), (1996, True)]:
        r = probar(anio=a)
        assert r["es_bisiesto"] is esperado, f"{a}: se esperaba {esperado}"
        assert r["dias_del_anio"] == (366 if esperado else 365), f"{a}: {r['dias_del_anio']} días"

    print("Todas las pruebas pasaron")
