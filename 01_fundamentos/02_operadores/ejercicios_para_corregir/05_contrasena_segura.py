"""
Ejercicio para corregir 05 - Contraseña segura
Nivel: avanzado
Errores a encontrar: 3

Qué debería hacer el programa:
    Una contraseña es segura si cumple TODAS estas condiciones:
        - Tiene 8 caracteres o más.
        - Tiene al menos una mayúscula.
        - No tiene espacios.

        "Python2026" -> True
        "Abcdefgh"   -> True   (exactamente 8 caracteres)
        "python2026" -> False  (sin mayúscula)

Ojo: el programa no lanza errores; todos los fallos son de lógica. Prueba
con varias contraseñas e imprime cada variable para encontrarlos.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""

clave = "Python2026"

# >>> tu código empieza aquí
tiene_longitud = len(clave) > 8
tiene_mayuscula = clave.lower() == clave
sin_espacios = " " not in clave
es_segura = tiene_longitud or tiene_mayuscula and sin_espacios
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
    claves = {
        "Python2026": True,
        "Abcdefgh": True,
        "python2026": False,
        "Py2026": False,
        "Python 2026": False,
        "MUY LARGA PERO CON ESPACIOS": False,
    }
    for c, esperado in claves.items():
        r = probar(clave=c)
        assert r["es_segura"] is esperado, f"{c!r}: se esperaba {esperado}"

    print("Todas las pruebas pasaron")
