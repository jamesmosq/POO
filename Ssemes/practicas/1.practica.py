# Ejemplo 1: Empleado con múltiples roles
class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def trabajar(self):
        return f"{self.nombre} está trabajando."

class Ingeniero:
    def programar(self):
        return "Escribiendo código."

class Gerente:
    def gestionar(self):
        return "Gestionando el equipo."

class IngenieroPrincipal(Empleado, Ingeniero, Gerente):
    def __init__(self, nombre):
        super().__init__(nombre)

# Uso del Ejemplo 1
jefe_ingenieros = IngenieroPrincipal("Ana")
print(jefe_ingenieros.trabajar())
print(jefe_ingenieros.programar())
print(jefe_ingenieros.gestionar())

