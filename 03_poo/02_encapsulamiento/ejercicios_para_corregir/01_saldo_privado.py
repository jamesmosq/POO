"""
Ejercicio para corregir 01 - Saldo privado
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    CuentaBancaria guarda el saldo en el atributo privado __saldo.
        cuenta = CuentaBancaria(1000)
        cuenta.depositar(500)
        cuenta.consultar_saldo() -> 1500

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

    def consultar_saldo(self):
        return self.saldo

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser positivo")
        self.__Saldo = self.__saldo + monto


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    cuenta = CuentaBancaria(1000)
    assert cuenta.consultar_saldo() == 1000
    cuenta.depositar(500)
    assert cuenta.consultar_saldo() == 1500, f"Saldo: {cuenta.consultar_saldo()}"

    print("Todas las pruebas pasaron")
