"""
Solución - Ejercicio propuesto 05 - Nómina
"""

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def calcular_pago(self):
        raise NotImplementedError("Cada tipo de empleado calcula su pago")

    def __str__(self):
        return f"{self.nombre}: ${self.calcular_pago():,.0f}"


class EmpleadoFijo(Empleado):
    def __init__(self, nombre, salario):
        super().__init__(nombre)
        self.salario = salario

    def calcular_pago(self):
        return self.salario


class EmpleadoPorHoras(Empleado):
    HORAS_NORMALES = 40
    FACTOR_EXTRA = 1.5

    def __init__(self, nombre, tarifa, horas):
        super().__init__(nombre)
        self.tarifa = tarifa
        self.horas = horas

    def calcular_pago(self):
        normales = min(self.horas, self.HORAS_NORMALES)
        extra = max(self.horas - self.HORAS_NORMALES, 0)
        return normales * self.tarifa + extra * self.tarifa * self.FACTOR_EXTRA


class Vendedor(EmpleadoFijo):
    def __init__(self, nombre, salario, ventas):
        super().__init__(nombre, salario)
        self.ventas = ventas

    def calcular_pago(self):
        return super().calcular_pago() + self.ventas * 5 / 100


class Nomina:
    def __init__(self):
        self.empleados = []

    def agregar(self, empleado):
        self.empleados.append(empleado)

    def total(self):
        return sum(e.calcular_pago() for e in self.empleados)

    def reporte(self):
        ordenados = sorted(self.empleados, key=lambda e: e.calcular_pago(), reverse=True)
        return [str(e) for e in ordenados]


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    ana = EmpleadoFijo("Ana", 2_500_000)
    luis = EmpleadoPorHoras("Luis", 20_000, 45)
    eva = Vendedor("Eva", 1_500_000, 20_000_000)

    assert ana.calcular_pago() == 2_500_000
    assert luis.calcular_pago() == 950_000, "40 h * 20.000 + 5 h * 30.000"
    assert EmpleadoPorHoras("Beto", 20_000, 30).calcular_pago() == 600_000
    assert eva.calcular_pago() == 2_500_000
    assert isinstance(eva, EmpleadoFijo), "Vendedor debe heredar de EmpleadoFijo"
    assert str(ana) == "Ana: $2,500,000"

    nomina = Nomina()
    for empleado in (luis, ana, eva):
        nomina.agregar(empleado)
    assert nomina.total() == 5_950_000
    assert nomina.reporte() == ["Ana: $2,500,000", "Eva: $2,500,000", "Luis: $950,000"]

    print("Todas las pruebas pasaron")
