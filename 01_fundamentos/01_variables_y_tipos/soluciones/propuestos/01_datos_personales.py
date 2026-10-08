"""
Solución - Ejercicio propuesto 01 - Datos personales
"""

nombre = "Ana"
edad = 20
estatura = 1.65
es_estudiante = True

presentacion = f"Me llamo {nombre}, tengo {edad} años y mido {estatura} m"
print(presentacion)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert type(nombre) is str, "nombre debe ser texto (str)"
    assert type(edad) is int, "edad debe ser un entero (int)"
    assert type(estatura) is float, "estatura debe ser decimal (float)"
    assert type(es_estudiante) is bool, "es_estudiante debe ser True o False (bool)"
    assert presentacion == "Me llamo Ana, tengo 20 años y mido 1.65 m", presentacion

    print("Todas las pruebas pasaron")
