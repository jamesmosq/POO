from abc import ABC, abstractmethod
class InstrumentoMusical(ABC):
    @abstractmethod
    def tocar(self):
        pass
class Guitarra(InstrumentoMusical):
    def tocar(self):
        return "Tocando la guitarra"
class Piano(InstrumentoMusical):
    def tocar(self):
        return "Tocando el piano"
class Bateria(InstrumentoMusical):
    def tocar(self):
        return "Tocando la bateria"
def tocar_instrumento(instrumento: InstrumentoMusical):
    print(instrumento.tocar())


tocar_instrumento(Guitarra())
tocar_instrumento(Piano())
tocar_instrumento(Bateria())