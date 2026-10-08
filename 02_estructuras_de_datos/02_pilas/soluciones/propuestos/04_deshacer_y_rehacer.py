"""
Solución - Ejercicio propuesto 04 - Deshacer y rehacer
"""

class Editor:
    def __init__(self):
        self.contenido = ""
        self.historial = []
        self.rehechos = []

    def escribir(self, texto):
        self.historial.append(self.contenido)
        self.contenido += texto
        self.rehechos.clear()  # una acción nueva invalida lo que se podía rehacer

    def deshacer(self):
        if self.historial:
            self.rehechos.append(self.contenido)
            self.contenido = self.historial.pop()

    def rehacer(self):
        if self.rehechos:
            self.historial.append(self.contenido)
            self.contenido = self.rehechos.pop()


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    editor = Editor()
    editor.escribir("Hola")
    editor.escribir(" mundo")
    editor.escribir("!")
    assert editor.contenido == "Hola mundo!"

    editor.deshacer()
    assert editor.contenido == "Hola mundo"
    editor.deshacer()
    assert editor.contenido == "Hola"

    editor.rehacer()
    assert editor.contenido == "Hola mundo"

    editor.escribir(" cruel")
    assert editor.contenido == "Hola mundo cruel"
    editor.rehacer()
    assert editor.contenido == "Hola mundo cruel", "Después de escribir, no se puede rehacer"

    for _ in range(10):
        editor.deshacer()
    assert editor.contenido == "", "Deshacer de más no debe fallar"

    print("Todas las pruebas pasaron")
