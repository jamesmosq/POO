"""
Solución - Ejercicio para corregir 05 - Nómina

CORRECCIÓN 1 (Luis cobraba 1.350.000): se multiplicaban TODAS las horas
por 1.5. Solo las horas que pasan de 40 llevan recargo.

CORRECCIÓN 2 (Eva cobraba solo la comisión): Vendedor sobrescribía
calcular_pago y se perdía el salario. Con super().calcular_pago() se
reutiliza el cálculo del padre y se le suma la comisión.

CORRECCIÓN 3 (el reporte salía de menor a mayor): sorted ordena de forma
ascendente; para ordenar de mayor a menor se usa reverse=True.
"""

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def calcular_pago(self):
        raise NotImplementedError


class EmpleadoFijo(Empleado):
    def __init__(self, nombre, salario):
        super().__init__(nombre)
        self.salario = salario

    def calcular_pago(self):
        return self.salario


class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, tarifa, horas):
        super().__init__(nombre)
        self.tarifa = tarifa
        self.horas = horas

    def calcular_pago(self):
        if self.horas <= 40:
            return self.horas * self.tarifa
        extra = self.horas - 40
        return 40 * self.tarifa + extra * self.tarifa * 1.5  # CORRECCIÓN 1


class Vendedor(EmpleadoFijo):
    def __init__(self, nombre, salario, ventas):
        super().__init__(nombre, salario)
        self.ventas = ventas

    def calcular_pago(self):
        return super().calcular_pago() + self.ventas * 5 / 100  # CORRECCIÓN 2


def reporte(empleados):
    ordenados = sorted(empleados, key=lambda e: e.calcular_pago(), reverse=True)  # CORRECCIÓN 3
    return [e.nombre for e in ordenados]


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    ana = EmpleadoFijo("Ana", 2_000_000)
    luis = EmpleadoPorHoras("Luis", 20_000, 45)
    eva = Vendedor("Eva", 1_500_000, 20_000_000)

    assert EmpleadoPorHoras("Beto", 20_000, 30).calcular_pago() == 600_000
    assert luis.calcular_pago() == 950_000, f"Luis cobra {luis.calcular_pago()}"
    assert eva.calcular_pago() == 2_500_000, f"Eva cobra {eva.calcular_pago()}"
    assert reporte([ana, luis, eva]) == ["Eva", "Ana", "Luis"], reporte([ana, luis, eva])

    print("Todas las pruebas pasaron")
