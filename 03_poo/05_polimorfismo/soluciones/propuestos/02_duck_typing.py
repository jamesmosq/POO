"""
Solución - Ejercicio propuesto 02 - Duck typing
"""

class Pato:
    def hablar(self):
        return "Cuac"


class Robot:
    def __init__(self, modelo):
        self.modelo = modelo

    def hablar(self):
        return f"Soy el robot {self.modelo}"


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        return f"Hola, me llamo {self.nombre}"


class Piedra:
    pass


def coro(objetos):
    return [objeto.hablar() for objeto in objetos if hasattr(objeto, "hablar")]


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    objetos = [Pato(), Piedra(), Robot("T-800"), Persona("Ana")]
    assert coro(objetos) == ["Cuac", "Soy el robot T-800", "Hola, me llamo Ana"]
    assert coro([]) == []

    for clase in (Pato, Robot, Persona):
        assert clase.__bases__ == (object,), f"{clase.__name__} no debe heredar de otra clase"

    print("Todas las pruebas pasaron")
