"""
Solución - Ejercicio propuesto 01 - Cuenta con saldo privado
"""

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo")
        self.titular = titular
        self.__saldo = saldo_inicial

    def consultar_saldo(self):
        return self.__saldo

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser positivo")
        self.__saldo += monto

    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser positivo")
        if monto > self.__saldo:
            raise ValueError("Saldo insuficiente")
        self.__saldo -= monto


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
    assert cuenta.consultar_saldo() == 1000

    try:
        cuenta.__saldo
        raise AssertionError("__saldo no debe ser accesible desde afuera")
    except AttributeError:
        pass

    cuenta.depositar(500)
    cuenta.retirar(200)
    assert cuenta.consultar_saldo() == 1300

    assert lanza_value_error(cuenta.retirar, 5000)
    assert lanza_value_error(cuenta.depositar, 0)
    assert lanza_value_error(CuentaBancaria, "Luis", -10)
    assert cuenta.consultar_saldo() == 1300

    print("Todas las pruebas pasaron")
