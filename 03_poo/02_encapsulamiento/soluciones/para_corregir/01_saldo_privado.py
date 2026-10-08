"""
Solución - Ejercicio para corregir 01 - Saldo privado

CORRECCIÓN 1 (AttributeError: 'CuentaBancaria' object has no attribute
'saldo'): el atributo se llama __saldo. Dentro de la clase se usa
self.__saldo.

CORRECCIÓN 2 (el depósito no se reflejaba): self.__Saldo (con S
mayúscula) es OTRO atributo. Python no avisa: simplemente lo crea. El
saldo real nunca cambiaba.
"""

class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

    def consultar_saldo(self):
        return self.__saldo  # CORRECCIÓN 1

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser positivo")
        self.__saldo = self.__saldo + monto  # CORRECCIÓN 2


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    cuenta = CuentaBancaria(1000)
    assert cuenta.consultar_saldo() == 1000
    cuenta.depositar(500)
    assert cuenta.consultar_saldo() == 1500, f"Saldo: {cuenta.consultar_saldo()}"

    print("Todas las pruebas pasaron")
