"""
Ejercicio para corregir 04 - Historial del navegador
Nivel: intermedio
Errores a encontrar: 3

Qué debería hacer el programa:
    Un navegador con botones Atrás y Adelante, implementado con dos pilas.

    - visitar(url): la página actual pasa a la pila atras y url pasa a ser
      la actual. Visitar una página nueva vacía la pila adelante.
    - ir_atras(): la actual pasa a adelante y se recupera la última de
      atras. Si atras está vacía, no hace nada.
    - ir_adelante(): lo contrario. Si adelante está vacía, no hace nada.

        visitar("a.com"), visitar("b.com"), visitar("c.com")
        ir_atras()     -> actual "b.com"
        ir_atras()     -> actual "a.com"
        ir_adelante()  -> actual "b.com"

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class Navegador:
    def __init__(self, inicio):
        self.actual = inicio
        self.atras = []
        self.adelante = []

    def visitar(self, url):
        self.atras.append(self.actual)
        self.actual = url

    def ir_atras(self):
        self.adelante.append(self.actual)
        self.actual = self.atras.pop()

    def ir_adelante(self):
        if self.adelante:
            self.atras.append(self.actual)
            self.actual = self.adelante.pop(0)


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
