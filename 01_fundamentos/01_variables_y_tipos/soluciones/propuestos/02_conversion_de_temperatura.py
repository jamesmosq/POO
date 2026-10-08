"""
Solución - Ejercicio propuesto 02 - Conversión de temperatura
"""

celsius = 25

# Multiplicación y división se evalúan antes que la suma, por eso no hacen
# falta paréntesis. Agregarlos tampoco está mal: (celsius * 9 / 5) + 32
fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15

print(f"{celsius} °C equivalen a {fahrenheit} °F y a {kelvin} K")


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert celsius == 25, "Las pruebas esperan celsius = 25"
    assert fahrenheit == 77.0, f"fahrenheit vale {fahrenheit}"
    assert round(kelvin, 2) == 298.15, f"kelvin vale {kelvin}"

    print("Todas las pruebas pasaron")
