"""
Solución - Ejercicio propuesto 03 - Conversor de unidades
"""

MILLAS_POR_KM = 0.621371
LIBRAS_POR_KG = 2.20462


def km_a_millas(km):
    return km * MILLAS_POR_KM


def millas_a_km(millas):
    return millas / MILLAS_POR_KM


def kg_a_libras(kg):
    return kg * LIBRAS_POR_KG


def libras_a_kg(libras):
    return libras / LIBRAS_POR_KG


def convertir(valor, desde, hacia):
    if desde == "km" and hacia == "millas":
        resultado = km_a_millas(valor)
    elif desde == "millas" and hacia == "km":
        resultado = millas_a_km(valor)
    elif desde == "kg" and hacia == "libras":
        resultado = kg_a_libras(valor)
    elif desde == "libras" and hacia == "kg":
        resultado = libras_a_kg(valor)
    else:
        raise ValueError(f"No se puede convertir de {desde} a {hacia}")
    return round(resultado, 2)


# ----------------------------------------------------------------------
# Pruebas
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
