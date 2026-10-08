"""
Ejercicio para corregir 01 - Anfibio
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    Anfibio hereda de Terrestre y de Acuatico. describir() usa los métodos
    de los dos padres:

        Anfibio().describir() -> "Avanzando por tierra y Navegando en el agua"

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class Terrestre:
    def andar(self):
        return "Avanzando por tierra"


class Acuatico:
    def navegar(self):
        return "Navegando en el agua"


class Anfibio(Terrestre Acuatico):
    def describir(self):
        return f"{self.andar()} y {Acuatico.navegar()}"


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert Anfibio().describir() == "Avanzando por tierra y Navegando en el agua"
    assert isinstance(Anfibio(), Acuatico)

    print("Todas las pruebas pasaron")
