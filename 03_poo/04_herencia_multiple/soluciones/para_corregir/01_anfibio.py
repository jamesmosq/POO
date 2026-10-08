"""
Solución - Ejercicio para corregir 01 - Anfibio

CORRECCIÓN 1 (SyntaxError): los padres se separan con coma:
class Anfibio(Terrestre, Acuatico).

CORRECCIÓN 2 (TypeError: Acuatico.navegar() missing 1 required positional
argument: 'self'): al llamar un método por el nombre de la clase, Python no
pasa el objeto automáticamente. Como navegar() se hereda, lo más simple es
self.navegar(). (Acuatico.navegar(self) también funciona.)
"""

class Terrestre:
    def andar(self):
        return "Avanzando por tierra"


class Acuatico:
    def navegar(self):
        return "Navegando en el agua"


class Anfibio(Terrestre, Acuatico):  # CORRECCIÓN 1
    def describir(self):
        return f"{self.andar()} y {self.navegar()}"  # CORRECCIÓN 2


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert Anfibio().describir() == "Avanzando por tierra y Navegando en el agua"
    assert isinstance(Anfibio(), Acuatico)

    print("Todas las pruebas pasaron")
