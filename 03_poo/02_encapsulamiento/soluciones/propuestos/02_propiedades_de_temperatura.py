"""
Solución - Ejercicio propuesto 02 - Propiedades de temperatura
"""

CERO_ABSOLUTO = -273.15


class Temperatura:
    def __init__(self, celsius=0):
        self.celsius = celsius  # pasa por el setter, así también se valida

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        if valor < CERO_ABSOLUTO:
            raise ValueError("No puede haber una temperatura menor al cero absoluto")
        self._celsius = valor

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, valor):
        self.celsius = (valor - 32) * 5 / 9


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    t = Temperatura(25)
    assert t.celsius == 25
    assert t.fahrenheit == 77

    t.fahrenheit = 212
    assert t.celsius == 100

    t.celsius = -273.15
    try:
        t.celsius = -300
        raise AssertionError("Debe lanzar ValueError")
    except ValueError:
        pass
    assert t.celsius == -273.15

    try:
        Temperatura(-500)
        raise AssertionError("El constructor también debe validar")
    except ValueError:
        pass

    assert isinstance(Temperatura.celsius, property), "celsius debe ser una propiedad"

    print("Todas las pruebas pasaron")
