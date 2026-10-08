"""
Ejercicio propuesto 03 - Cuentas bancarias
Nivel: intermedio

Un banco maneja dos tipos de cuenta que comparten las operaciones básicas,
pero cada una tiene una regla propia.

Requisitos:
1. Clase CuentaBancaria(titular, saldo=0):
   - depositar(monto): suma al saldo y retorna el saldo nuevo.
   - retirar(monto): resta del saldo y retorna el saldo nuevo.
   - Ambos métodos lanzan ValueError si el monto es menor o igual a 0.
   - retirar() lanza ValueError si el monto supera el saldo.
2. Clase CuentaAhorros(titular, saldo=0, tasa=0.02), hija de CuentaBancaria:
   - aplicar_interes(): suma saldo * tasa al saldo y retorna el saldo nuevo.
3. Clase CuentaCorriente(titular, saldo=0, sobregiro=100000), hija de
   CuentaBancaria:
   - Sobrescribe retirar() para permitir que el saldo quede negativo hasta
     el límite del sobregiro. Por ejemplo, con saldo 50000 y sobregiro 100000
     se pueden retirar hasta 150000.
   - Sigue lanzando ValueError si el monto es menor o igual a 0.

Pista: piensa qué parte de la validación puedes reutilizar del padre y cuál
debes cambiar.

Conceptos: herencia, sobrescritura, excepciones, validación.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
