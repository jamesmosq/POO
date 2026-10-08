"""
Ejercicio para corregir 04 - Año bisiesto
Nivel: intermedio
Errores a encontrar: 3

Qué debería hacer el programa:
    Un año es bisiesto si es divisible entre 4 y no entre 100, o si es
    divisible entre 400. El año llega como texto, como lo entregaría input().

        "2024" -> es_bisiesto True,  mensaje "¿2024 es bisiesto? True"
        "1900" -> es_bisiesto False, mensaje "¿1900 es bisiesto? False"

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""

texto_anio = "2024"

# >>> tu código empieza aquí
anio = texto_anio
es_bisiesto = anio % 4 == 0 or anio % 100 != 0 and anio % 400 == 0
mensaje = "¿" + texto_anio + " es bisiesto? " + es_bisiesto
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
    for texto, esperado in [("2024", True), ("2023", False), ("1900", False), ("2000", True)]:
        r = probar(texto_anio=texto)
        assert r["es_bisiesto"] is esperado, f"{texto}: se esperaba {esperado}"
        assert r["mensaje"] == f"¿{texto} es bisiesto? {esperado}", r["mensaje"]

    print("Todas las pruebas pasaron")
