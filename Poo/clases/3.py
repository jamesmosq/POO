class Libro:
    def __init__(self,titulo,autor,anioPublicacion,genero):
        self.titulo = titulo
        self.autor = autor
        self.anioPublicacion = anioPublicacion
        self.genero = genero

    def descripcion(self):
        return f"'{self.titulo}' por {self.autor}, publicado en {self.anioPublicacion} en el género {self.genero}"

libro1= Libro("cien años","pepito perez",1920,"comedia")
print(libro1.descripcion())