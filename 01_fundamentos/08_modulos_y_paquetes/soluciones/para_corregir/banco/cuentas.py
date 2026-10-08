"""Cuentas bancarias."""
from .utilidades import formatear_moneda  # CORRECCIÓN 1


class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto
        return self.saldo

    def resumen(self):
        return f"{self.titular}: {formatear_moneda(self.saldo)}"
