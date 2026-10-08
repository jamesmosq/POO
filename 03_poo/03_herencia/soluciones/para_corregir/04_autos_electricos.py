"""
Solución - Ejercicio para corregir 04 - Autos eléctricos

CORRECCIÓN 1 (AttributeError: no existe 'puertas'): AutoElectrico llamaba a
Vehiculo.__init__ directamente y se saltaba a Auto, que es quien guarda las
puertas. Con super() se respeta la cadena completa: AutoElectrico -> Auto ->
Vehiculo.

CORRECCIÓN 2 (TypeError: __str__ returned non-string): faltaba 'return' en
__str__, entonces devolvía None. str() exige que __str__ retorne un texto.

CORRECCIÓN 3 (TypeError en isinstance): los argumentos estaban al revés. El
orden es isinstance(objeto, Clase).
"""


class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def __str__(self):
        return f"Vehículo {self.marca}"


class Auto(Vehiculo):
    def __init__(self, marca, puertas):
        super().__init__(marca)
        self.puertas = puertas

    def __str__(self):
        return super().__str__() + f" de {self.puertas} puertas"


class AutoElectrico(Auto):
    def __init__(self, marca, puertas, autonomia_km):
        super().__init__(marca, puertas)  # CORRECCIÓN 1
        self.autonomia_km = autonomia_km

    def __str__(self):
        return super().__str__() + f", autonomía {self.autonomia_km} km"  # CORRECCIÓN 2


def contar_electricos(vehiculos):
    return sum(1 for v in vehiculos if isinstance(v, AutoElectrico))  # CORRECCIÓN 3


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert str(Auto("Mazda", 4)) == "Vehículo Mazda de 4 puertas"

    byd = AutoElectrico("BYD", 4, 400)
    assert byd.puertas == 4
    assert str(byd) == "Vehículo BYD de 4 puertas, autonomía 400 km"

    flota = [Auto("Mazda", 4), byd, Vehiculo("Genérico"), AutoElectrico("Tesla", 2, 500)]
    assert contar_electricos(flota) == 2

    print("Todas las pruebas pasaron")
