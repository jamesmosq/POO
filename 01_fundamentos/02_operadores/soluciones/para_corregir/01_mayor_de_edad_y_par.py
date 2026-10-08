"""
Solución - Ejercicio para corregir 01 - Mayor de edad y número par

CORRECCIÓN 1 (SyntaxError): el operador "mayor o igual" se escribe >=, no =>.

CORRECCIÓN 2 (resultado incorrecto): un número es par cuando el residuo de
dividirlo entre 2 es 0, no 1.
"""

edad = 18
numero = 10

# >>> tu código empieza aquí
es_mayor_de_edad = edad >= 18  # CORRECCIÓN 1
es_par = numero % 2 == 0  # CORRECCIÓN 2
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
    assert probar(edad=18, numero=10)["es_mayor_de_edad"] is True
    assert probar(edad=17, numero=10)["es_mayor_de_edad"] is False
    assert probar(edad=18, numero=10)["es_par"] is True
    assert probar(edad=18, numero=7)["es_par"] is False

    print("Todas las pruebas pasaron")
