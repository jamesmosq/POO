"""
Solución - Ejercicio propuesto 05 - Peajes
"""

import re


class Vehiculo:
    TARIFA_BASE = 10000

    def __init__(self, placa):
        placa = placa.upper()
        if not re.fullmatch(r"[A-Z]{3}[0-9]{3}", placa):
            raise ValueError(f"Placa inválida: {placa}")
        self.placa = placa

    def peaje(self):
        # self.TARIFA_BASE busca el atributo empezando por la clase del
        # objeto: si es un Carro, encuentra 12000.
        return self.TARIFA_BASE

    def __str__(self):
        return f"{self.placa} - {type(self).__name__} - ${self.peaje():,.0f}"


class Carro(Vehiculo):
    TARIFA_BASE = 12000


class Camion(Vehiculo):
    VALOR_EJE_ADICIONAL = 8000

    def __init__(self, placa, ejes):
        if ejes < 2:
            raise ValueError("Un camión tiene al menos 2 ejes")
        super().__init__(placa)
        self.ejes = ejes

    def peaje(self):
        return super().peaje() + (self.ejes - 2) * self.VALOR_EJE_ADICIONAL


class CamionRefrigerado(Camion):
    RECARGO = 20

    def peaje(self):
        return super().peaje() * (100 + self.RECARGO) / 100


def recaudo_total(vehiculos):
    return sum(v.peaje() for v in vehiculos)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    v = Vehiculo("abc123")
    assert v.placa == "ABC123"
    assert v.peaje() == 10000
    assert str(v) == "ABC123 - Vehiculo - $10,000"

    c = Carro("XYZ789")
    assert c.peaje() == 12000 and str(c) == "XYZ789 - Carro - $12,000"
    assert "peaje" not in Carro.__dict__, "Carro solo cambia TARIFA_BASE"

    assert Camion("TRK001", 2).peaje() == 10000
    assert Camion("TRK002", 4).peaje() == 26000
    frio = CamionRefrigerado("FRI001", 3)
    assert frio.peaje() == 21600, frio.peaje()
    assert str(frio) == "FRI001 - CamionRefrigerado - $21,600"
    assert isinstance(frio, Camion) and isinstance(frio, Vehiculo)

    for placa, args in (("AB123", ()), ("ABCD12", ()), ("123ABC", ())):
        try:
            Vehiculo(placa, *args)
            raise AssertionError(f"La placa {placa} debe lanzar ValueError")
        except ValueError:
            pass
    try:
        Camion("TRK003", 1)
        raise AssertionError("Un camión con 1 eje debe lanzar ValueError")
    except ValueError:
        pass

    assert recaudo_total([v, c, frio]) == 10000 + 12000 + 21600

    print("Todas las pruebas pasaron")
