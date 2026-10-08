"""
Ejercicio propuesto 02 - Conversión de temperatura
Nivel: básico

Requisitos:
1. Usa la variable celsius que ya está creada.
2. Calcula fahrenheit con la fórmula:  F = C * 9 / 5 + 32
3. Calcula kelvin con la fórmula:      K = C + 273.15
4. Imprime los tres valores con un mensaje claro.

Prueba después con otros valores de celsius (0, 100, -40) y revisa que los
resultados tengan sentido. Las pruebas usan el valor 25.

Conceptos: operadores aritméticos, precedencia, variables numéricas.
"""

celsius = 25

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert celsius == 25, "Las pruebas esperan celsius = 25"
    assert fahrenheit == 77.0, f"fahrenheit vale {fahrenheit}"
    assert round(kelvin, 2) == 298.15, f"kelvin vale {kelvin}"

    print("Todas las pruebas pasaron")
