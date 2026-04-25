"""

1.	__init__: En el ejemplo del Libro, usamos __init__ para inicializar un libro con su título,
autor y número de páginas.
Este método se llama automáticamente cuando creamos una nueva instancia de Libro.
"""
# 1. __init__
class Libro:
    def __init__(self, titulo, autor, paginas,pasta):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.pasta = pasta

libro = Libro("El Quijote", "Miguel de Cervantes", 863,'azucar')
print(f"Libro creado: {libro.titulo} por {libro.autor} pasta de {libro.pasta}" )

libro = Libro("ERERWETETWTW", "TREETWTEEEE", 863,'plastico y arena')
print(f"Libro creado: {libro.titulo} por {libro.autor} pasta de {libro.pasta}" )