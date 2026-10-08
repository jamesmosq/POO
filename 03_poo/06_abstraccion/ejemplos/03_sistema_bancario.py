class SistemaBancario:
    """
    Abstracción de un sistema bancario que oculta la complejidad
    de las operaciones internas
    """

    def __init__(self):
        self._cuentas = {}  # Diccionario privado
        self._contador_transacciones = 0

    def crear_cuenta(self, numero_cuenta, titular, saldo_inicial=0):
        """Interfaz simple para crear cuentas"""
        if numero_cuenta in self._cuentas:
            raise ValueError("La cuenta ya existe")

        self._cuentas[numero_cuenta] = {
            'titular': titular,
            'saldo': saldo_inicial,
            'historial': []
        }
        self._registrar_transaccion(numero_cuenta, f"Cuenta creada con saldo inicial: ${saldo_inicial}")

    def depositar(self, numero_cuenta, cantidad):
        """Interfaz simple para depósitos"""
        if numero_cuenta not in self._cuentas:
            raise ValueError("Cuenta no encontrada")

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")

        self._cuentas[numero_cuenta]['saldo'] += cantidad
        self._registrar_transaccion(numero_cuenta, f"Depósito: +${cantidad}")

    def retirar(self, numero_cuenta, cantidad):
        """Interfaz simple para retiros"""
        if numero_cuenta not in self._cuentas:
            raise ValueError("Cuenta no encontrada")

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")

        if self._cuentas[numero_cuenta]['saldo'] < cantidad:
            raise ValueError("Saldo insuficiente")

        self._cuentas[numero_cuenta]['saldo'] -= cantidad
        self._registrar_transaccion(numero_cuenta, f"Retiro: -${cantidad}")

    def consultar_saldo(self, numero_cuenta):
        """Interfaz simple para consultar saldo"""
        if numero_cuenta not in self._cuentas:
            raise ValueError("Cuenta no encontrada")

        return self._cuentas[numero_cuenta]['saldo']

    def _registrar_transaccion(self, numero_cuenta, descripcion):
        """Método privado para registrar transacciones"""
        from datetime import datetime
        self._contador_transacciones += 1
        transaccion = {
            'id': self._contador_transacciones,
            'fecha': datetime.now(),
            'descripcion': descripcion
        }
        self._cuentas[numero_cuenta]['historial'].append(transaccion)


# Uso del sistema bancario (abstracción en acción)
banco = SistemaBancario()
banco.crear_cuenta("12345", "Juan Pérez", 1000)
banco.depositar("12345", 500)
banco.retirar("12345", 200)
print(f"Saldo actual: ${banco.consultar_saldo('12345')}")