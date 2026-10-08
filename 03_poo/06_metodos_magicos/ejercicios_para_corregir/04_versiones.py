"""
Ejercicio para corregir 04 - Versiones
Nivel: intermedio
Errores a encontrar: 3

Qué debería hacer el programa:
    - Version("1.10.0") > Version("1.9.0")  -> True
    - sorted() ordena versiones de la más antigua a la más nueva.
    - Las versiones se pueden guardar en un set (dos iguales cuentan una vez).

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""
from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, texto):
        self.texto = texto

    def __eq__(self, otra):
        return self.texto == otra.texto

    def __lt__(self, otra):
        return self.texto < otra.texto

    def __str__(self):
        return self.texto


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    unicas = {Version("1.0.0"), Version("1.0.0"), Version("2.0.0")}
    assert len(unicas) == 2

    assert Version("1.10.0") > Version("1.9.0"), "1.10 es más nueva que 1.9"
    ordenadas = sorted([Version("1.10.0"), Version("1.2.0"), Version("1.9.3")])
    assert [str(v) for v in ordenadas] == ["1.2.0", "1.9.3", "1.10.0"]

    assert (Version("1.0.0") == "1.0.0") is False, "Una Version no es igual a un texto"

    print("Todas las pruebas pasaron")
