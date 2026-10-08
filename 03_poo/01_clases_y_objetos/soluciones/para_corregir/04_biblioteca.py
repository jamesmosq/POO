"""
Solución - Ejercicio para corregir 04 - Biblioteca

CORRECCIÓN 1 (TypeError: isbn_valido() takes 1 positional argument but 2
were given): sin @staticmethod, al llamarlo desde un objeto
(libro.isbn_valido(...)) Python pasa el objeto como primer argumento. El
decorador indica que el método no recibe self.

CORRECCIÓN 2 (buscar retornaba None): se comparaba el objeto Libro con un
texto, y eso siempre es False. Hay que comparar su atributo titulo.

CORRECCIÓN 3 (prestar retornaba None): el método imprimía un mensaje, pero
no retornaba True. Si no hay return, la función devuelve None.
"""

class Libro:
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        self.prestado = False

    @staticmethod  # CORRECCIÓN 1
    def isbn_valido(isbn):
        return len(isbn) == 13 and isbn.isdigit()


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar(self, libro):
        if not Libro.isbn_valido(libro.isbn):
            raise ValueError("ISBN inválido")
        self.libros.append(libro)

    def buscar(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:  # CORRECCIÓN 2
                return libro
        return None

    def prestar(self, titulo):
        libro = self.buscar(titulo)
        if libro is None or libro.prestado:
            return False
        libro.prestado = True
        return True  # CORRECCIÓN 3


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert Libro.isbn_valido("9789584276971") is True
    assert Libro.isbn_valido("123") is False

    biblioteca = Biblioteca()
    biblioteca.agregar(Libro("Cien años de soledad", "9789584276971"))
    try:
        biblioteca.agregar(Libro("Sin ISBN", "123"))
        raise AssertionError("Debe lanzar ValueError")
    except ValueError:
        pass

    encontrado = biblioteca.buscar("Cien años de soledad")
    assert encontrado is not None and encontrado.isbn == "9789584276971"
    assert biblioteca.prestar("Cien años de soledad") is True
    assert biblioteca.prestar("Cien años de soledad") is False, "Ya estaba prestado"
    assert biblioteca.prestar("No existe") is False

    print("Todas las pruebas pasaron")
