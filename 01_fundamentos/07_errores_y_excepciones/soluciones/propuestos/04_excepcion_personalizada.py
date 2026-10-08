"""
Solución - Ejercicio propuesto 04 - Excepción personalizada
"""

class SaldoInsuficienteError(Exception):
    pass


def retirar(saldo, monto):
    if monto <= 0:
        raise ValueError("El monto debe ser positivo")
    if monto > saldo:
        faltante = monto - saldo
        raise SaldoInsuficienteError(f"Faltan {faltante}")
    return saldo - monto


def intentar_retiro(saldo, monto):
    try:
        nuevo_saldo = retirar(saldo, monto)
    except SaldoInsuficienteError as error:
        return f"Rechazado: {error}"
    except ValueError:
        return "Monto inválido"
    return f"Retiro exitoso. Saldo: {nuevo_saldo}"


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert issubclass(SaldoInsuficienteError, Exception)
    assert retirar(1000, 300) == 700

    try:
        retirar(1000, 1300)
        raise AssertionError("Debe lanzar SaldoInsuficienteError")
    except SaldoInsuficienteError as error:
        assert str(error) == "Faltan 300"

    assert intentar_retiro(1000, 300) == "Retiro exitoso. Saldo: 700"
    assert intentar_retiro(1000, 1300) == "Rechazado: Faltan 300"
    assert intentar_retiro(1000, -5) == "Monto inválido"

    print("Todas las pruebas pasaron")
