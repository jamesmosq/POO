"""
Solución - Ejercicio para corregir 01 - Libro con __str__

CORRECCIÓN 1 (TypeError: __str__ returned non-string (type tuple)):
"return a, b" retorna una tupla. __str__ siempre debe retornar un texto.

CORRECCIÓN 2 (repr mostraba "<__main__.Libro object at ...>"): el método se
llamaba __rpr__. Python no avisa de un método mágico mal escrito: solo lo
ignora y usa el comportamiento por defecto.
"""

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo}, de {self.autor}"  # CORRECCIÓN 1

    def __repr__(self):  # CORRECCIÓN 2
        return f"Libro({self.titulo!r}, {self.autor!r})"


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    libro = Libro("Cien años de soledad", "García Márquez")
    assert str(libro) == "Cien años de soledad, de García Márquez"
    assert repr(libro) == "Libro('Cien años de soledad', 'García Márquez')", repr(libro)

    print("Todas las pruebas pasaron")
