from abc import ABC , abstractmethod
class InstrumentoMusical(ABC):
    @abstractmethod
    def tocar(self):
        pass

    @abstractmethod
    def afinar(self):
        pass

    @abstractmethod
    def limpiar(self):
        pass
class Guitarra(InstrumentoMusical):
    def tocar(self):
        return "Tocando la guitarra"

    def afinar(self):
        return "Afinando la guitarra"

    def limpiar(self):
        return "Limpiando la guitarra"

G1= Guitarra()
print(G1.tocar())

print(G1.afinar())