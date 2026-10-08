"""
Solución - Ejercicio propuesto 02 - Tarifa de parqueadero
"""

def tarifa(tipo_vehiculo, horas):
    tipo = tipo_vehiculo.strip().lower()
    if tipo == "carro":
        valor = horas * 3000
        if valor > 15000:
            valor = 15000
        return valor
    elif tipo == "moto":
        return horas * 1500
    elif tipo == "bicicleta":
        return 0
    else:
        return None


# ----------------------------------------------------------------------
# Pruebas
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
