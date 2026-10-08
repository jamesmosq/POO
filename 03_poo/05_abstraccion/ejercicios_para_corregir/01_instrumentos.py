"""
Ejercicio para corregir 01 - Instrumentos
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    Instrumento es una clase abstracta con el método abstracto tocar().
    Guitarra y Piano la implementan.

        Guitarra().tocar() -> "Rasgueo de guitarra"
        Piano().tocar()    -> "Notas de piano"

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class Instrumento(ABC):
    @abstractmethod
    def tocar(self):
        pass


class Guitarra(Instrumento):
    def tocar(self):
        return "Rasgueo de guitarra"


class Piano(Instrumento):
    def toca(self):
        return "Notas de piano"


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert Guitarra().tocar() == "Rasgueo de guitarra"
    assert Piano().tocar() == "Notas de piano"

    print("Todas las pruebas pasaron")
