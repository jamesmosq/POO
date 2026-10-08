"""
Ejercicio para corregir 02 - Empleados abstractos
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    - Empleado es abstracta: no se pueden crear objetos de ella.
    - Cada hija implementa rol(). El método concreto presentacion() usa rol().

        Desarrollador("Ana").presentacion() -> "Ana - Desarrollador"

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""
from abc import ABC, abstractmethod


class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def rol(self):
        pass

    def presentacion(self):
        return f"{self.nombre} - {self.rol()}"


class Desarrollador(Empleado):
    def rol(self):
        return super().rol() + "Desarrollador"


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    try:
        Empleado("X")
        raise AssertionError("Empleado debe ser abstracta: no se debe poder instanciar")
    except TypeError:
        pass

    assert Desarrollador("Ana").presentacion() == "Ana - Desarrollador"

    print("Todas las pruebas pasaron")
