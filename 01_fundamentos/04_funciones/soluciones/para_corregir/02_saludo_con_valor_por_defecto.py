"""
Solución - Ejercicio para corregir 02 - Saludo con valor por defecto

CORRECCIÓN 1 (SyntaxError: parameter without a default follows parameter
with a default): los parámetros con valor por defecto van siempre después
de los obligatorios. Además, el enunciado pide que nombre sea el primero.

CORRECCIÓN 2 (resultado literal "{saludo}, {nombre}"): faltaba la f antes
de las comillas. Sin la f, las llaves son texto normal.
"""

def saludar(nombre, saludo="Hola"):  # CORRECCIÓN 1
    return f"{saludo}, {nombre}"  # CORRECCIÓN 2


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert saludar("Ana") == "Hola, Ana", saludar("Ana")
    assert saludar("Ana", "Buenos días") == "Buenos días, Ana"
    assert saludar(nombre="Luis", saludo="Hey") == "Hey, Luis"

    print("Todas las pruebas pasaron")
