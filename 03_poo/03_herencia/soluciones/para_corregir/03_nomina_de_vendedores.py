"""
Solución - Ejercicio para corregir 03 - Nómina de vendedores

CORRECCIÓN 1 (el método retorna None): faltaba 'return'. Una función sin
return devuelve None aunque calcule el valor correcto.

CORRECCIÓN 2 (resultado incorrecto): PORCENTAJE_COMISION vale 10, pero se
multiplicaba directamente; eso es el 1000%, no el 10%. Hay que dividir entre
100.

CORRECCIÓN 3 (argumento por defecto mutable): 'ventas=[]' crea UNA sola
lista cuando Python lee la definición de la función, y todos los vendedores
creados sin ventas comparten esa misma lista. Por eso Beto "tenía" las
ventas de Ana. La forma correcta es usar None y crear la lista adentro.
"""


class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base


class Vendedor(Empleado):
    PORCENTAJE_COMISION = 10

    def __init__(self, nombre, salario_base, ventas=None):  # CORRECCIÓN 3
        super().__init__(nombre, salario_base)
        self.ventas = [] if ventas is None else list(ventas)

    def registrar_venta(self, valor):
        self.ventas.append(valor)

    def calcular_salario(self):
        comision = sum(self.ventas) * self.PORCENTAJE_COMISION / 100  # CORRECCIÓN 2
        return super().calcular_salario() + comision  # CORRECCIÓN 1


# ----------------------------------------------------------------------
# Pruebas
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
