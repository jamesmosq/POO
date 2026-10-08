"""
Ejercicio para corregir 02 - Saludo con valor por defecto
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    saludar(nombre, saludo="Hola") retorna el saludo armado:
        saludar("Ana")               -> "Hola, Ana"
        saludar("Ana", "Buenos días") -> "Buenos días, Ana"

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


def saludar(saludo="Hola", nombre):
    return "{saludo}, {nombre}"


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert saludar("Ana") == "Hola, Ana", saludar("Ana")
    assert saludar("Ana", "Buenos días") == "Buenos días, Ana"
    assert saludar(nombre="Luis", saludo="Hey") == "Hey, Luis"

    print("Todas las pruebas pasaron")
