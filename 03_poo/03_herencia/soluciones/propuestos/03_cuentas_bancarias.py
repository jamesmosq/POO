"""
Solución - Ejercicio propuesto 03 - Cuentas bancarias
"""


class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def _validar_monto(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser mayor que cero")

    def depositar(self, monto):
        self._validar_monto(monto)
        self.saldo += monto
        return self.saldo

    def retirar(self, monto):
        self._validar_monto(monto)
        if monto > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= monto
        return self.saldo


class CuentaAhorros(CuentaBancaria):
    def __init__(self, titular, saldo=0, tasa=0.02):
        super().__init__(titular, saldo)
        self.tasa = tasa

    def aplicar_interes(self):
        self.saldo += self.saldo * self.tasa
        return self.saldo


class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo=0, sobregiro=100000):
        super().__init__(titular, saldo)
        self.sobregiro = sobregiro

    def retirar(self, monto):
        # No se puede usar super().retirar() porque el padre rechaza cualquier
        # retiro mayor al saldo. Sí se reutiliza la validación del monto.
        self._validar_monto(monto)
        if self.saldo - monto < -self.sobregiro:
            raise ValueError("Se supera el límite de sobregiro")
        self.saldo -= monto
        return self.saldo


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
def lanza_value_error(funcion, *argumentos):
    try:
        funcion(*argumentos)
    except ValueError:
        return True
    return False


if __name__ == "__main__":
    cuenta = CuentaBancaria("Ana", 1000)
    assert cuenta.depositar(500) == 1500
    assert cuenta.retirar(300) == 1200
    assert lanza_value_error(cuenta.retirar, 5000), "No se puede retirar más del saldo"
    assert lanza_value_error(cuenta.depositar, -10), "No se aceptan montos negativos"
    assert lanza_value_error(cuenta.retirar, 0), "No se aceptan montos en cero"

    ahorros = CuentaAhorros("Luis", 100000, tasa=0.05)
    assert ahorros.aplicar_interes() == 105000
    assert ahorros.depositar(5000) == 110000
    assert lanza_value_error(ahorros.retirar, 200000)

    corriente = CuentaCorriente("Eva", 50000)
    assert corriente.retirar(150000) == -100000
    assert lanza_value_error(corriente.retirar, 1), "Se superó el sobregiro"
    assert lanza_value_error(corriente.retirar, -5)

    assert isinstance(ahorros, CuentaBancaria)
    assert isinstance(corriente, CuentaBancaria)

    print("Todas las pruebas pasaron")
