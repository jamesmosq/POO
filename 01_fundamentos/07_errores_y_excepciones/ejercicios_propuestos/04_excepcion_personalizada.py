"""
Ejercicio propuesto 04 - Excepción personalizada
Nivel: intermedio

Puedes crear tus propios tipos de error para que quien use tu código los
pueda atrapar por separado. Basta con heredar de Exception:
    class MiError(Exception):
        pass

Requisitos:
1. Crea la excepción SaldoInsuficienteError, que herede de Exception.
2. Escribe retirar(saldo, monto), que retorne el saldo nuevo y:
   - Lance ValueError("El monto debe ser positivo") si monto <= 0.
   - Lance SaldoInsuficienteError(f"Faltan {faltante}") si el monto supera
     el saldo, donde faltante = monto - saldo.
3. Escribe intentar_retiro(saldo, monto), que llame a retirar y retorne un
   mensaje en lugar de lanzar el error:
       - éxito: "Retiro exitoso. Saldo: 700"
       - SaldoInsuficienteError: "Rechazado: Faltan 300"
       - ValueError: "Monto inválido"

Conceptos: clases de excepción, raise, varios except, str(error).
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
