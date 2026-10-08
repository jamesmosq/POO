"""
Solución - Ejercicio propuesto 01 - Empleado y gerente
"""


class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def descripcion(self):
        return f"{self.nombre} gana {self.salario}"


class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        # El padre se encarga de nombre y salario; aquí solo se agrega lo nuevo.
        super().__init__(nombre, salario)
        self.departamento = departamento

    def descripcion(self):
        # Se reutiliza el texto del padre en lugar de volver a escribirlo.
        return f"{super().descripcion()} y dirige {self.departamento}"


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    ana = Empleado("Ana", 2500000)
    assert ana.nombre == "Ana"
    assert ana.salario == 2500000
    assert ana.descripcion() == "Ana gana 2500000"

    luis = Gerente("Luis", 5000000, "Ventas")
    assert luis.nombre == "Luis"
    assert luis.departamento == "Ventas"
    assert luis.descripcion() == "Luis gana 5000000 y dirige Ventas"
    assert isinstance(luis, Empleado), "Gerente debe heredar de Empleado"

    print("Todas las pruebas pasaron")
