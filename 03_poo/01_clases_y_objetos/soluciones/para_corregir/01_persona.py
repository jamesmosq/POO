"""
Solución - Ejercicio para corregir 01 - Persona

CORRECCIÓN 1 (TypeError: Persona() takes no arguments): el constructor se
llamaba __int__ (sin la i de init). Como Python no encontró __init__, usó
el constructor por defecto, que no recibe argumentos.

CORRECCIÓN 2 (TypeError: saludar() takes 0 positional arguments but 1 was
given): todos los métodos de instancia reciben self. Al llamar
ana.saludar(), Python pasa ana como primer argumento.
"""

class Persona:
    def __init__(self, nombre, edad):  # CORRECCIÓN 1
        self.nombre = nombre
        self.edad = edad

    def saludar(self):  # CORRECCIÓN 2
        return f"Hola, soy {self.nombre}"


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    ana = Persona("Ana", 20)
    assert ana.edad == 20
    assert ana.saludar() == "Hola, soy Ana"

    print("Todas las pruebas pasaron")
