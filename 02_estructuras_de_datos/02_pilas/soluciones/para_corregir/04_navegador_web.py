"""
Solución - Ejercicio para corregir 04 - Historial del navegador

CORRECCIÓN 1 (IndexError: pop from empty list): ir_atras no revisaba si
había historial. Además movía la página actual a adelante antes de saber
si se podía retroceder. Se valida primero, como en ir_adelante.

CORRECCIÓN 2: adelante también es una pila; la página a la que se vuelve
es la ÚLTIMA que entró, pop(), no la primera, pop(0).

CORRECCIÓN 3: al visitar una página nueva, el camino "hacia adelante" deja
de existir. Hay que vaciar la pila adelante.
"""

class Navegador:
    def __init__(self, inicio):
        self.actual = inicio
        self.atras = []
        self.adelante = []

    def visitar(self, url):
        self.atras.append(self.actual)
        self.actual = url
        self.adelante.clear()  # CORRECCIÓN 3

    def ir_atras(self):
        if self.atras:  # CORRECCIÓN 1
            self.adelante.append(self.actual)
            self.actual = self.atras.pop()

    def ir_adelante(self):
        if self.adelante:
            self.atras.append(self.actual)
            self.actual = self.adelante.pop()  # CORRECCIÓN 2


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    nav = Navegador("inicio")
    nav.ir_atras()
    assert nav.actual == "inicio", "Sin historial, Atrás no hace nada"
    assert nav.adelante == [], "Sin historial, Atrás no debe tocar adelante"

    for url in ("a.com", "b.com", "c.com"):
        nav.visitar(url)
    nav.ir_atras()
    nav.ir_atras()
    assert nav.actual == "a.com"

    nav.ir_adelante()
    assert nav.actual == "b.com", f"Adelante llevó a {nav.actual}"

    nav.visitar("d.com")
    nav.ir_adelante()
    assert nav.actual == "d.com", "Después de visitar una página nueva no hay Adelante"

    print("Todas las pruebas pasaron")
