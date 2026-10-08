"""
Solución - Ejercicio propuesto 03 - Medios de pago
"""

class MedioDePago:
    nombre = "Genérico"

    def comision(self, monto):
        return 0

    def cobrar(self, monto):
        # Igual para todos; self.comision() llama a la versión de cada hija.
        return monto + self.comision(monto)


class Efectivo(MedioDePago):
    nombre = "Efectivo"


class TarjetaCredito(MedioDePago):
    nombre = "Tarjeta"

    def comision(self, monto):
        return monto * 3 / 100


class PSE(MedioDePago):
    nombre = "PSE"

    def comision(self, monto):
        return 2500


def procesar_pagos(pagos):
    totales = {}
    for medio, monto in pagos:
        totales[medio.nombre] = totales.get(medio.nombre, 0) + medio.cobrar(monto)
    return totales


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert Efectivo().cobrar(10000) == 10000
    assert TarjetaCredito().cobrar(10000) == 10300
    assert PSE().cobrar(10000) == 12500

    pagos = [(Efectivo(), 5000), (TarjetaCredito(), 20000), (PSE(), 1000), (Efectivo(), 3000)]
    assert procesar_pagos(pagos) == {"Efectivo": 8000, "Tarjeta": 20600, "PSE": 3500}

    for clase in (Efectivo, TarjetaCredito, PSE):
        assert "cobrar" not in clase.__dict__, f"{clase.__name__} no debe sobrescribir cobrar()"

    print("Todas las pruebas pasaron")
