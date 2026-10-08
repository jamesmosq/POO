"""
Solución - Ejercicio propuesto 01 - Saludo por idioma
"""

def saludar(nombre, idioma="es"):
    if idioma == "en":
        saludo = "Hello"
    elif idioma == "fr":
        saludo = "Bonjour"
    else:
        saludo = "Hola"
    return f"{saludo}, {nombre}"


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert saludar("Ana") == "Hola, Ana"
    assert saludar("Ana", "es") == "Hola, Ana"
    assert saludar("John", "en") == "Hello, John"
    assert saludar("Marie", idioma="fr") == "Bonjour, Marie"
    assert saludar("Luis", "de") == "Hola, Luis"

    print("Todas las pruebas pasaron")
