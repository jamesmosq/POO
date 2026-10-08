"""
Ejercicio para corregir 01 - Mayor de edad y número par
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    es_mayor_de_edad -> True si edad es 18 o más.
    es_par           -> True si numero es par.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""

edad = 18
numero = 10

# >>> tu código empieza aquí
es_mayor_de_edad = edad => 18
es_par = numero % 2 == 1
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
    assert probar(edad=18, numero=10)["es_mayor_de_edad"] is True
    assert probar(edad=17, numero=10)["es_mayor_de_edad"] is False
    assert probar(edad=18, numero=10)["es_par"] is True
    assert probar(edad=18, numero=7)["es_par"] is False

    print("Todas las pruebas pasaron")
