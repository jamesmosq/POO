"""
Solución - Ejercicio para corregir 03 - Procesar pagos

CORRECCIÓN 1 (TypeError: Tarjeta.cobrar() takes 1 positional argument but
2 were given): Tarjeta definía cobrar sin el parámetro monto. Para usar
los objetos de forma intercambiable, todos deben tener el método con los
mismos parámetros.

CORRECCIÓN 2 (TypeError al sumar): Nequi retornaba un texto ("$1000") en
lugar de un número. Todos deben retornar el mismo tipo de dato; el
formato para mostrar se aplica después, no dentro del cálculo.
"""

class Efectivo:
    def cobrar(self, monto):
        return monto


class Tarjeta:
    def cobrar(self, monto):  # CORRECCIÓN 1
        return monto * 1.03


class Nequi:
    def cobrar(self, monto):
        return monto  # CORRECCIÓN 2


def total_cobrado(pagos):
    return sum(medio.cobrar(monto) for medio, monto in pagos)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    pagos = [(Efectivo(), 1000), (Tarjeta(), 1000), (Nequi(), 1000)]
    assert round(total_cobrado(pagos), 2) == 3030

    print("Todas las pruebas pasaron")
