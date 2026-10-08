"""
Ejercicio para corregir 01 - Libro con __str__
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    libro = Libro("Cien años de soledad", "García Márquez")
    str(libro)   -> "Cien años de soledad, de García Márquez"
    repr(libro)  -> "Libro('Cien años de soledad', 'García Márquez')"

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return self.titulo, self.autor

    def __rpr__(self):
        return f"Libro({self.titulo!r}, {self.autor!r})"


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    libro = Libro("Cien años de soledad", "García Márquez")
    assert str(libro) == "Cien años de soledad, de García Márquez"
    assert repr(libro) == "Libro('Cien años de soledad', 'García Márquez')", repr(libro)

    print("Todas las pruebas pasaron")
