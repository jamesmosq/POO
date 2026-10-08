"""
Ejercicio propuesto 01 - Datos personales
Nivel: básico

Requisitos:
1. Crea estas variables con exactamente estos valores:
       nombre         -> "Ana"
       edad           -> 20
       estatura       -> 1.65
       es_estudiante  -> True
2. Crea la variable presentacion usando un f-string, para que quede así:
       "Me llamo Ana, tengo 20 años y mido 1.65 m"
3. Imprime presentacion.

Conceptos: variables, tipos de datos (str, int, float, bool), f-strings.

Cuando termines, ejecuta el archivo. Si todo está bien verás el mensaje
"Todas las pruebas pasaron".
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert type(nombre) is str, "nombre debe ser texto (str)"
    assert type(edad) is int, "edad debe ser un entero (int)"
    assert type(estatura) is float, "estatura debe ser decimal (float)"
    assert type(es_estudiante) is bool, "es_estudiante debe ser True o False (bool)"
    assert presentacion == "Me llamo Ana, tengo 20 años y mido 1.65 m", presentacion

    print("Todas las pruebas pasaron")
