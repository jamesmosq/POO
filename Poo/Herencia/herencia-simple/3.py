from abc import ABC, abstractmethod


# ABSTRACCIÓN
class ProductoBancario(ABC):
    def __init__(self, numero, titular):
        # ENCAPSULAMIENTO
        self._numero = numero  # Protegido (un guion bajo)
        self._titular = titular
        self._activo = True

    @abstractmethod
    def calcular_balance(self):
        pass

    @abstractmethod
    def puede_realizar_operacion(self, monto):
        pass

    def get_info(self):
        return f"Producto #{self._numero} - Titular: {self._titular}"

    def desactivar(self):
        self._activo = False
        return f"Producto {self._numero} desactivado"


# HERENCIA
class CuentaAhorro(ProductoBancario):
    def __init__(self, numero, titular, saldo_inicial=0, tasa_interes=0.01):
        super().__init__(numero, titular)
        self.__saldo = saldo_inicial  # Privado (doble guion bajo)
        self.__tasa_interes = tasa_interes

    def calcular_balance(self):
        return self.__saldo

    def puede_realizar_operacion(self, monto):
        return monto <= self.__saldo and self._activo

    def depositar(self, monto):
        if monto > 0 and self._activo:
            self.__saldo += monto
            return f"Depósito de ${monto} realizado. Nuevo saldo: ${self.__saldo}"
        return "Operación no válida"

    def retirar(self, monto):
        if self.puede_realizar_operacion(monto):
            self.__saldo -= monto
            return f"Retiro de ${monto} realizado. Nuevo saldo: ${self.__saldo}"
        return "Fondos insuficientes o cuenta inactiva"

    def aplicar_interes(self):
        interes = self.__saldo * self.__tasa_interes
        self.__saldo += interes
        return f"Interés de ${interes:.2f} aplicado. Nuevo saldo: ${self.__saldo}"


class TarjetaCredito(ProductoBancario):
    def __init__(self, numero, titular, limite_credito, tasa_interes=0.025):
        super().__init__(numero, titular)
        self.__limite = limite_credito  # Privado
        self.__saldo_utilizado = 0  # Privado
        self.__tasa_interes = tasa_interes

    def calcular_balance(self):
        return self.__limite - self.__saldo_utilizado

    def puede_realizar_operacion(self, monto):
        return monto <= self.calcular_balance() and self._activo

    def realizar_compra(self, monto):
        if self.puede_realizar_operacion(monto):
            self.__saldo_utilizado += monto
            return f"Compra de ${monto} realizada. Crédito disponible: ${self.calcular_balance()}"
        return "Límite excedido o tarjeta inactiva"

    def realizar_pago(self, monto):
        if monto > 0 and self._activo:
            self.__saldo_utilizado = max(0, self.__saldo_utilizado - monto)
            return f"Pago de ${monto} realizado. Crédito disponible: ${self.calcular_balance()}"
        return "Operación no válida"


# POLIMORFISMO
class SistemaNotificaciones:
    @staticmethod
    def notificar_operacion(producto, mensaje, canal):
        info = producto.get_info()
        balance = producto.calcular_balance()

        if canal == "email":
            return f"EMAIL: {info} - {mensaje} - Balance actual: ${balance}"
        elif canal == "sms":
            return f"SMS: Producto #{producto._numero} - {mensaje}"
        elif canal == "app":
            return f"APP NOTIFICATION: {mensaje} - Balance: ${balance}"
        else:
            return "Canal no soportado"


# Demostración
cuenta = CuentaAhorro("AH-1001", "Carlos Pérez", 1000)
tarjeta = TarjetaCredito("TC-5001", "Carlos Pérez", 5000)

print(cuenta.get_info())
print(cuenta.depositar(500))
print(SistemaNotificaciones.notificar_operacion(cuenta, "Depósito exitoso", "email"))

print("\n" + tarjeta.get_info())
print(tarjeta.realizar_compra(2000))
print(SistemaNotificaciones.notificar_operacion(tarjeta, "Compra aprobada", "sms"))

# Lista de productos bancarios (polimorfismo)
productos = [cuenta, tarjeta]
print("\nResumen de productos:")
for producto in productos:
    print(f"{producto.get_info()} - Balance: ${producto.calcular_balance()}")