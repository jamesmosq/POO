"""
Solución - Ejercicio para corregir 04 - Año bisiesto

CORRECCIÓN 1 (TypeError: not all arguments converted during string
formatting): con texto, % no es el residuo sino un operador de formato. Hay
que convertir el año a int.

CORRECCIÓN 2 (resultado incorrecto): los operadores estaban cruzados. La
regla es (divisible entre 4 Y no entre 100) O divisible entre 400.

CORRECCIÓN 3 (TypeError: can only concatenate str (not "bool") to str): no
se puede unir texto con un bool usando +. Se convierte con str() o se usa un
f-string.
"""

texto_anio = "2024"

# >>> tu código empieza aquí
anio = int(texto_anio)  # CORRECCIÓN 1
es_bisiesto = (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0  # CORRECCIÓN 2
mensaje = f"¿{texto_anio} es bisiesto? {es_bisiesto}"  # CORRECCIÓN 3
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
    for texto, esperado in [("2024", True), ("2023", False), ("1900", False), ("2000", True)]:
        r = probar(texto_anio=texto)
        assert r["es_bisiesto"] is esperado, f"{texto}: se esperaba {esperado}"
        assert r["mensaje"] == f"¿{texto} es bisiesto? {esperado}", r["mensaje"]

    print("Todas las pruebas pasaron")
