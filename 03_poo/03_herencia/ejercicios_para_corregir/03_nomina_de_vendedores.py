"""
Ejercicio para corregir 03 - Nómina de vendedores
Nivel: intermedio
Errores a encontrar: 3

Qué debería hacer el programa:
    Un Vendedor es un Empleado que gana su salario base más una comisión del
    10% sobre el total de sus ventas. Cada vendedor lleva su propia lista de
    ventas.

        ana = Vendedor("Ana", 1000000)
        ana.registrar_venta(2000000)
        ana.calcular_salario()   ->  1200000

        beto = Vendedor("Beto", 1000000)
        beto.calcular_salario()  ->  1000000   (no ha vendido nada)

Ojo: no todos los errores lanzan una excepción. Algunos solo producen un
resultado incorrecto. Uno de ellos es un error clásico de Python que aparece
incluso en código profesional.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base


class Vendedor(Empleado):
    PORCENTAJE_COMISION = 10

    def __init__(self, nombre, salario_base, ventas=[]):
        super().__init__(nombre, salario_base)
        self.ventas = ventas

    def registrar_venta(self, valor):
        self.ventas.append(valor)

    def calcular_salario(self):
        comision = sum(self.ventas) * self.PORCENTAJE_COMISION
        super().calcular_salario() + comision


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert Empleado("Carlos", 900000).calcular_salario() == 900000

    ana = Vendedor("Ana", 1000000)
    ana.registrar_venta(2000000)
    assert ana.calcular_salario() == 1200000, f"Ana: {ana.calcular_salario()}"

    beto = Vendedor("Beto", 1000000)
    assert beto.ventas == [], f"Beto no ha vendido, pero tiene ventas: {beto.ventas}"
    assert beto.calcular_salario() == 1000000

    print("Todas las pruebas pasaron")
