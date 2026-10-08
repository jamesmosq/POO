# Ejercicio 2: Gestor de empleados
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def aumentar_salario(self, porcentaje=None, cantidad=None):
        if porcentaje is not None:
            self.salario *= (1 + porcentaje/100)
        elif cantidad is not None:
            self.salario += cantidad
        return self.salario

# Uso:
emp = Empleado("Juan", 1000)
print(emp.aumentar_salario(porcentaje=10))  # 1100.0
print(emp.aumentar_salario(cantidad=500))   # 1600.0

