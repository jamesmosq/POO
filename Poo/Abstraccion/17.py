from abc import ABC, abstractmethod

class contenidoStreaming(ABC):

    def __init__(self, titulo, duracion, clasificacion, fecha_lanzamiento, views):
        self.titulo = titulo
        self.duracion = duracion
        self.clasificacion = clasificacion
        self.fecha_lanzamiento = fecha_lanzamiento
        self.views = views


    @abstractmethod
    def reproducir(self):
        pass
    @abstractmethod
    def pausar(self):
        pass
    @abstractmethod
    def calcular_popularidad(self):
        pass

    @abstractmethod
    def mostrar_info(self):
        pass

class Pelicula(contenidoStreaming):

    def __init__(self, titulo, duracion, clasificacion, fecha_lanzamiento, views):
        super().__init__(titulo, duracion, clasificacion, fecha_lanzamiento, views)

    def reproducir(self):
        print(f"Reproduciendo película: {self.titulo}")

    def pausar(self):
        print(f"Pausando película: {self.titulo}")

    def calcular_popularidad(self):
        return self.views / 1000

    def mostrar_info(self):
        return f"{self.titulo} - {self.duracion} min - {self.clasificacion} - {self.fecha_lanzamiento}"

p1 = Pelicula("Inception", 148, "PG-13", "2010-07-16", 5000000)
print(p1.mostrar_info())