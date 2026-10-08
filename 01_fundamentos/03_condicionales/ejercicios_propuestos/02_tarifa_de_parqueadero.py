"""
Ejercicio propuesto 02 - Tarifa de parqueadero
Nivel: básico

Completa la función tarifa(tipo_vehiculo, horas) para que retorne cuánto
debe pagar un vehículo:

    "carro"      -> 3000 por hora, pero nunca más de 15000 (tarifa plena)
    "moto"       -> 1500 por hora
    "bicicleta"  -> gratis (0)
    Cualquier otro tipo -> None

El tipo puede llegar con mayúsculas o espacios ("  Carro "). Límpialo antes
de comparar con .strip().lower().

Conceptos: if, elif, else, condiciones anidadas, métodos de texto.
"""


def tarifa(tipo_vehiculo, horas):
    # Escribe tu solución aquí
    pass


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert tarifa("carro", 2) == 6000
    assert tarifa("carro", 5) == 15000
    assert tarifa("carro", 8) == 15000, "El carro no paga más de 15000"
    assert tarifa("moto", 4) == 6000
    assert tarifa("bicicleta", 10) == 0
    assert tarifa("  Carro ", 1) == 3000, "Debe aceptar mayúsculas y espacios"
    assert tarifa("MOTO", 2) == 3000
    assert tarifa("bus", 3) is None

    print("Todas las pruebas pasaron")
