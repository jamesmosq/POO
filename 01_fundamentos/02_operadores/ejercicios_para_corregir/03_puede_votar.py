"""
Ejercicio para corregir 03 - ¿Puede votar?
Nivel: intermedio
Errores a encontrar: 2

Qué debería hacer el programa:
    Una persona puede votar si tiene 18 años o más Y tiene cédula.
    La respuesta sobre la cédula llega como texto: "si" o "no".

        edad 20, respuesta "si" -> True
        edad 20, respuesta "no" -> False
        edad 16, respuesta "si" -> False

Ojo: ninguno de los dos errores lanza una excepción.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""

edad = 20
respuesta_cedula = "no"

# >>> tu código empieza aquí
tiene_cedula = bool(respuesta_cedula)
puede_votar = edad >= 18 or tiene_cedula
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
    casos = [((20, "si"), True), ((20, "no"), False), ((16, "si"), False), ((16, "no"), False)]
    for (e, resp), esperado in casos:
        r = probar(edad=e, respuesta_cedula=resp)
        assert r["puede_votar"] is esperado, f"edad={e}, cédula={resp!r}: se esperaba {esperado}"

    print("Todas las pruebas pasaron")
