"""
Ejercicio propuesto 03 - Conversor de unidades
Nivel: intermedio

Vas a dividir un problema en funciones pequeñas y luego combinarlas.

Requisitos:
1. Escribe cuatro funciones de una sola línea cada una:
       km_a_millas(km)        -> km * 0.621371
       millas_a_km(millas)    -> millas / 0.621371
       kg_a_libras(kg)        -> kg * 2.20462
       libras_a_kg(libras)    -> libras / 2.20462
2. Escribe convertir(valor, desde, hacia), que llame a la función que
   corresponda y retorne el resultado redondeado a 2 decimales:
       convertir(10, "km", "millas")  -> 6.21
       convertir(5, "kg", "libras")   -> 11.02
   Si la conversión no existe, lanza:
       raise ValueError(f"No se puede convertir de {desde} a {hacia}")
3. Usa una constante para cada factor (por ejemplo MILLAS_POR_KM) en lugar
   de escribir el número varias veces.

Conceptos: descomposición en funciones, constantes, raise.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert round(km_a_millas(1), 6) == 0.621371
    assert round(millas_a_km(0.621371), 6) == 1
    assert round(kg_a_libras(1), 5) == 2.20462
    assert round(libras_a_kg(2.20462), 5) == 1

    assert convertir(10, "km", "millas") == 6.21
    assert convertir(6.21, "millas", "km") == 9.99
    assert convertir(5, "kg", "libras") == 11.02
    assert convertir(11.02, "libras", "kg") == 5.0

    try:
        convertir(1, "km", "kg")
        raise AssertionError("Debe lanzar ValueError")
    except ValueError as error:
        assert str(error) == "No se puede convertir de km a kg"

    print("Todas las pruebas pasaron")
