"""
Ejercicio propuesto 01 - Saludo por idioma
Nivel: básico

Requisitos:
1. Escribe la función saludar(nombre, idioma="es") que RETORNE (no que
   imprima) el saludo según el idioma:
       "es" -> "Hola, Ana"
       "en" -> "Hello, Ana"
       "fr" -> "Bonjour, Ana"
   Si el idioma no se conoce, usa el saludo en español.
2. Si se llama sin idioma, debe saludar en español: saludar("Ana").

Diferencia clave: print() muestra un texto en pantalla; return entrega un
valor a quien llamó la función para que lo pueda usar.

Conceptos: def, parámetros, valores por defecto, return.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert saludar("Ana") == "Hola, Ana"
    assert saludar("Ana", "es") == "Hola, Ana"
    assert saludar("John", "en") == "Hello, John"
    assert saludar("Marie", idioma="fr") == "Bonjour, Marie"
    assert saludar("Luis", "de") == "Hola, Luis"

    print("Todas las pruebas pasaron")
