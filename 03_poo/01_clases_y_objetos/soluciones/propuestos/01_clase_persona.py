"""
Solución - Ejercicio propuesto 01 - Clase Persona
"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"

    def cumplir_anios(self):
        self.edad += 1
        return self.edad

    def es_mayor_de_edad(self):
        return self.edad >= 18


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    ana = Persona("Ana", 17)
    luis = Persona("Luis", 30)

    assert ana.nombre == "Ana" and ana.edad == 17
    assert ana.presentarse() == "Hola, soy Ana y tengo 17 años"
    assert ana.es_mayor_de_edad() is False

    assert ana.cumplir_anios() == 18
    assert ana.es_mayor_de_edad() is True
    assert ana.presentarse() == "Hola, soy Ana y tengo 18 años"

    assert luis.edad == 30, "Cada objeto tiene sus propios atributos"

    print("Todas las pruebas pasaron")
