"""
Ejercicio para corregir 04 - Biblioteca
Nivel: intermedio
Errores a encontrar: 3

Qué debería hacer el programa:
    - Libro(titulo, isbn). Libro.isbn_valido(isbn) es un método estático:
      un ISBN es válido si tiene 13 dígitos.
    - Biblioteca.agregar(libro) solo acepta libros con ISBN válido (si no,
      ValueError).
    - Biblioteca.buscar(titulo) retorna el LIBRO con ese título, o None.
    - Biblioteca.prestar(titulo) marca el libro como prestado y retorna
      True; si no existe o ya estaba prestado, retorna False.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class Libro:
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        self.prestado = False

    def isbn_valido(isbn):
        return len(isbn) == 13 and isbn.isdigit()


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar(self, libro):
        if not libro.isbn_valido(libro.isbn):
            raise ValueError("ISBN inválido")
        self.libros.append(libro)

    def buscar(self, titulo):
        for libro in self.libros:
            if libro == titulo:
                return libro
        return None

    def prestar(self, titulo):
        libro = self.buscar(titulo)
        if libro is None or libro.prestado:
            return False
        libro.prestado = True
        print(f"Préstamo de {titulo} registrado")


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
