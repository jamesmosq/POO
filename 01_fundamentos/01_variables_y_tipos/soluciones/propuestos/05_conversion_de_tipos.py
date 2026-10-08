"""
Solución - Ejercicio propuesto 05 - Conversión de tipos
"""

texto_edad = "17"
texto_precio = "2500.50"
texto_cantidad = "3"

edad = int(texto_edad)
precio = float(texto_precio)
cantidad = int(texto_cantidad)

total = precio * cantidad
es_mayor_de_edad = edad >= 18
mensaje = f"Total: {total}"
print(mensaje)

# Respuesta a la pregunta:
# texto_precio * 3 no da error: repite el texto tres veces
# ("2500.502500.502500.50"). texto_precio + 3 sí da error (TypeError),
# porque Python no suma un texto con un número.


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert edad == 17 and type(edad) is int
    assert precio == 2500.5 and type(precio) is float
    assert cantidad == 3 and type(cantidad) is int
    assert total == 7501.5, f"total vale {total!r}"
    assert es_mayor_de_edad is False
    assert mensaje == "Total: 7501.5", mensaje

    print("Todas las pruebas pasaron")
