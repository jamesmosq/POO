"""
Solución - Ejercicio para corregir 05 - Tablero con place

CORRECCIÓN 1 (TclError: bad anchor "centre"): el valor válido es
"center" (en inglés estadounidense). Los demás valores de anchor son
puntos cardinales: "n", "ne", "e", "se", "s", "sw", "w", "nw".

CORRECCIÓN 2 (el círculo no quedaba centrado): create_oval recibe la caja
que contiene al óvalo. Para centrarlo en (x, y) la caja va de
(x - radio, y - radio) a (x + radio, y + radio).

CORRECCIÓN 3 (Limpiar borraba la cuadrícula): delete("all") borra todo el
lienzo. Para borrar solo los círculos se usa su tag.
"""

import tkinter as tk


class Tablero:
    def __init__(self, raiz):
        self.lienzo = tk.Canvas(raiz, width=300, height=200, bg="white")
        self.lienzo.pack(fill="both", expand=True)
        for x in range(50, 300, 50):
            self.lienzo.create_line(x, 0, x, 200, fill="#cccccc", tags="cuadricula")
        self.boton = tk.Button(raiz, text="Limpiar", command=self.limpiar)
        self.boton.place(relx=0.5, rely=0.5, anchor="center")  # CORRECCIÓN 1

    def agregar_circulo(self, x, y, radio):
        return self.lienzo.create_oval(x - radio, y - radio, x + radio, y + radio, tags="circulo")  # CORRECCIÓN 2

    def limpiar(self):
        self.lienzo.delete("circulo")  # CORRECCIÓN 3


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    app = Tablero(raiz)
    assert app.boton.place_info()["anchor"] == "center"

    circulo = app.agregar_circulo(100, 100, 10)
    assert app.lienzo.coords(circulo) == [90.0, 90.0, 110.0, 110.0], app.lienzo.coords(circulo)

    app.boton.invoke()
    assert app.lienzo.find_withtag("circulo") == ()
    assert len(app.lienzo.find_withtag("cuadricula")) == 5, "Limpiar borró también la cuadrícula"
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        Tablero(raiz)
        raiz.mainloop()
