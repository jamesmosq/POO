"""
Solución - Ejercicio propuesto 01 - Vehículo anfibio
"""

class Terrestre:
    def andar(self):
        return "Avanzando por tierra"

    def velocidad(self):
        return 80


class Acuatico:
    def navegar(self):
        return "Navegando en el agua"

    def velocidad(self):
        return 30


class Anfibio(Terrestre, Acuatico):
    # velocidad() no se escribe: por el MRO (Anfibio, Terrestre, Acuatico)
    # se toma la de Terrestre.

    def velocidad_en_agua(self):
        # Para usar la versión de un padre concreto se le llama por su nombre
        # y se le pasa el objeto.
        return Acuatico.velocidad(self)

    def describir(self):
        return f"Anfibio: {self.velocidad()} km/h en tierra, {self.velocidad_en_agua()} km/h en agua"


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    a = Anfibio()
    assert a.andar() == "Avanzando por tierra"
    assert a.navegar() == "Navegando en el agua"
    assert a.velocidad() == 80, "Por el MRO se usa la velocidad de Terrestre"
    assert a.velocidad_en_agua() == 30
    assert a.describir() == "Anfibio: 80 km/h en tierra, 30 km/h en agua"

    assert Anfibio.__bases__ == (Terrestre, Acuatico), "Hereda de Terrestre y de Acuatico, en ese orden"
    assert "velocidad" not in Anfibio.__dict__, "No redefinas velocidad() en Anfibio"
    assert isinstance(a, Terrestre) and isinstance(a, Acuatico)

    print("Todas las pruebas pasaron")
