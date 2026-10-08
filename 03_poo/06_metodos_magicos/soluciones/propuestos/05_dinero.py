"""
Solución - Ejercicio propuesto 05 - Dinero
"""

from decimal import Decimal


class Dinero:
    def __init__(self, cantidad, moneda="COP"):
        # Decimal(str(0.1)) es exactamente 0.1; Decimal(0.1) no lo es.
        self.cantidad = Decimal(str(cantidad))
        self.moneda = moneda

    def _validar_moneda(self, otro):
        if self.moneda != otro.moneda:
            raise ValueError(f"No se puede operar {self.moneda} con {otro.moneda}")

    def __add__(self, otro):
        self._validar_moneda(otro)
        return Dinero(self.cantidad + otro.cantidad, self.moneda)

    def __radd__(self, otro):
        # sum() empieza con 0 + primer_elemento.
        if otro == 0:
            return self
        return self + otro

    def __sub__(self, otro):
        self._validar_moneda(otro)
        return Dinero(self.cantidad - otro.cantidad, self.moneda)

    def __mul__(self, factor):
        return Dinero(self.cantidad * Decimal(str(factor)), self.moneda)

    def __eq__(self, otro):
        if not isinstance(otro, Dinero):
            return NotImplemented
        return (self.cantidad, self.moneda) == (otro.cantidad, otro.moneda)

    def __lt__(self, otro):
        self._validar_moneda(otro)
        return self.cantidad < otro.cantidad

    def __hash__(self):
        return hash((self.cantidad, self.moneda))

    def __str__(self):
        return f"${self.cantidad:,.2f} {self.moneda}"

    def __bool__(self):
        return self.cantidad != 0


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    from decimal import Decimal

    assert Dinero(0.1) + Dinero(0.2) == Dinero(0.3), "Con Decimal la suma debe ser exacta"
    assert str(Dinero(1500.5)) == "$1,500.50 COP"
    assert str(Dinero(10, "USD") * 3) == "$30.00 USD"
    assert Dinero(100) - Dinero(30) == Dinero(70)

    precios = [Dinero(1000), Dinero(2500), Dinero(500)]
    assert sum(precios) == Dinero(4000)
    assert max(precios) == Dinero(2500)

    assert not Dinero(0)
    assert Dinero(1)
    assert len({Dinero(5), Dinero(5.0), Dinero(6)}) == 2
    assert Dinero(5).cantidad == Decimal("5")

    try:
        Dinero(1, "COP") + Dinero(1, "USD")
        raise AssertionError("No se pueden sumar monedas distintas")
    except ValueError:
        pass

    print("Todas las pruebas pasaron")
