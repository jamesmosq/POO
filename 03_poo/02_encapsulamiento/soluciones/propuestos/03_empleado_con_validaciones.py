"""
Solución - Ejercicio propuesto 03 - Empleado con validaciones
"""

class Empleado:
    SALARIO_MINIMO = 1_423_500

    def __init__(self, nombre, salario, email):
        self.nombre = nombre
        self.salario = salario
        self.email = email

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        limpio = " ".join(valor.split()).title()
        if not limpio:
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = limpio

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        if valor < self.SALARIO_MINIMO:
            raise ValueError(f"El salario no puede ser menor que {self.SALARIO_MINIMO}")
        self._salario = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if valor.count("@") != 1 or "." not in valor.split("@")[1]:
            raise ValueError(f"Email inválido: {valor}")
        self._email = valor.lower()

    def aumentar_salario(self, porcentaje):
        self.salario = self.salario * (100 + porcentaje) / 100


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
def lanza_value_error(funcion):
    try:
        funcion()
    except ValueError:
        return True
    return False


if __name__ == "__main__":
    e = Empleado("  ana  pérez ", 2_000_000, "Ana.Perez@Empresa.com")
    assert e.nombre == "Ana Pérez"
    assert e.email == "ana.perez@empresa.com"

    e.aumentar_salario(10)
    assert e.salario == 2_200_000

    assert lanza_value_error(lambda: Empleado("", 2_000_000, "a@b.co"))
    assert lanza_value_error(lambda: Empleado("Luis", 1_000_000, "a@b.co"))
    assert lanza_value_error(lambda: Empleado("Luis", 2_000_000, "sin-arroba.com"))
    assert lanza_value_error(lambda: Empleado("Luis", 2_000_000, "a@@b.com"))
    assert lanza_value_error(lambda: Empleado("Luis", 2_000_000, "a@sinpunto"))

    def asignar_salario_bajo():
        e.salario = 100
    assert lanza_value_error(asignar_salario_bajo)
    assert e.salario == 2_200_000

    print("Todas las pruebas pasaron")
