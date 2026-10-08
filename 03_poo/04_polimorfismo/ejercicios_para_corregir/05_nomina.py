"""
Ejercicio para corregir 05 - Nómina
Nivel: avanzado
Errores a encontrar: 3

Qué debería hacer el programa:
    - EmpleadoFijo cobra su salario.
    - EmpleadoPorHoras: 40 horas a tarifa normal y cada hora EXTRA a 1.5
      veces la tarifa.
    - Vendedor (hijo de EmpleadoFijo): salario + 5 % de las ventas.
    - reporte(empleados): nombres ordenados de MAYOR a menor pago.

        EmpleadoPorHoras("Luis", 20000, 45).calcular_pago() -> 950000
        Vendedor("Eva", 1500000, 20000000).calcular_pago()  -> 2500000

Ojo: el programa no lanza errores. Calcula a mano el pago de cada
empleado y compáralo con lo que retorna el programa.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
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
        return self.horas * self.tarifa * 1.5


class Vendedor(EmpleadoFijo):
    def __init__(self, nombre, salario, ventas):
        super().__init__(nombre, salario)
        self.ventas = ventas

    def calcular_pago(self):
        return self.ventas * 5 / 100


def reporte(empleados):
    ordenados = sorted(empleados, key=lambda e: e.calcular_pago())
    return [e.nombre for e in ordenados]


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
