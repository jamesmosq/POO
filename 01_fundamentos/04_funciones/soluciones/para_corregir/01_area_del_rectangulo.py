"""
Solución - Ejercicio para corregir 01 - Área del rectángulo

CORRECCIÓN 1 (NameError: name 'area_rectangulo' is not defined): Python
ejecuta el archivo de arriba hacia abajo. La función se usaba antes de
haberla definido. Las definiciones van primero.

CORRECCIÓN 2 (resultado None): la función imprimía el área pero no la
retornaba. Una función sin return devuelve None, así que resultado quedaba
en None aunque en pantalla se viera 12.
"""

def area_rectangulo(base, altura):
    return base * altura  # CORRECCIÓN 2


resultado = area_rectangulo(3, 4)  # CORRECCIÓN 1


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert area_rectangulo(2, 5) == 10, "La función debe RETORNAR el área"
    assert resultado == 12, f"resultado vale {resultado!r}"

    print("Todas las pruebas pasaron")
