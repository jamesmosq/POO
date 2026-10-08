"""
Ejercicio propuesto 04 - Deshacer y rehacer
Nivel: intermedio

Los editores de texto implementan Ctrl+Z y Ctrl+Y con DOS pilas:
    - historial: guarda los estados anteriores para poder deshacer.
    - rehechos:  guarda lo que se deshizo para poder rehacer.

Completa la clase Editor:
    escribir(texto)  agrega texto al contenido. Antes, guarda el contenido
                     actual en historial. Escribir algo nuevo VACÍA la pila
                     de rehechos (ya no se puede rehacer).
    deshacer()       vuelve al estado anterior. El estado actual pasa a
                     rehechos. Si no hay historial, no hace nada.
    rehacer()        recupera lo último que se deshizo. El estado actual
                     vuelve al historial. Si no hay nada, no hace nada.

El contenido actual está en self.contenido.

Conceptos: dos pilas cooperando, estados.
"""


class Editor:
    def __init__(self):
        self.contenido = ""
        self.historial = []
        self.rehechos = []

    def escribir(self, texto):
        pass

    def deshacer(self):
        pass

    def rehacer(self):
        pass


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
