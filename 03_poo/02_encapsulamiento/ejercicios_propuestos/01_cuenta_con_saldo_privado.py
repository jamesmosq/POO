"""
Ejercicio propuesto 01 - Cuenta con saldo privado
Nivel: básico

Encapsular es proteger los datos internos de un objeto para que solo se
modifiquen a través de sus métodos, que validan cada cambio.

En Python:
    self.nombre    público
    self._nombre   "protegido": convención que dice "no lo toques desde afuera"
    self.__nombre  "privado": Python le cambia el nombre (name mangling) para
                   que no se pueda acceder como objeto.__nombre

Requisitos. Crea la clase CuentaBancaria(titular, saldo_inicial=0):
1. Guarda el saldo en un atributo privado __saldo.
2. consultar_saldo(): retorna el saldo.
3. depositar(monto) y retirar(monto): validan que el monto sea positivo y,
   al retirar, que haya saldo suficiente (si no, ValueError).
4. Un saldo inicial negativo lanza ValueError.

Conceptos: atributos privados, métodos de acceso, validación.
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
