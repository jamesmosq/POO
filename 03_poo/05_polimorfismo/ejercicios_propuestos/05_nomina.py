"""
Ejercicio propuesto 05 - Nómina
Nivel: avanzado

Una empresa tiene empleados con formas de pago distintas, y la nómina debe
calcularlos todos sin preguntar de qué tipo es cada uno.

Requisitos:
1. Clase base Empleado(nombre):
   - calcular_pago(): NotImplementedError en la base.
   - __str__(): "Ana: $2,500,000" (usa calcular_pago y el formato :,.0f).
2. Hijas:
   - EmpleadoFijo(nombre, salario): cobra el salario.
   - EmpleadoPorHoras(nombre, tarifa, horas): las primeras 40 horas se
     pagan a la tarifa normal; cada hora adicional se paga a 1.5 veces la
     tarifa.
   - Vendedor(nombre, salario, ventas): cobra el salario (reutiliza
     EmpleadoFijo con herencia) más 5 % de las ventas.
3. Clase Nomina:
   - agregar(empleado)
   - total(): suma de los pagos.
   - reporte(): lista de str(empleado), de mayor a menor pago.

Conceptos: polimorfismo, herencia de varios niveles, super(), __str__.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
