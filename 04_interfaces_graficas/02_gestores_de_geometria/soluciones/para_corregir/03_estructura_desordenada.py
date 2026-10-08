"""
Solución - Ejercicio para corregir 03 - Estructura desordenada

CORRECCIÓN 1: el lateral estaba con side="right".

CORRECCIÓN 2: el contenido (expand=True) se empacaba antes que la barra de
estado y tomaba todo el espacio disponible; la barra quedaba aplastada o al
costado. Los widgets que van en los bordes se empacan primero y el que se
expande, al final.
"""

import tkinter as tk


class Estructura:
    def __init__(self, raiz):
        self.estado = tk.Label(raiz, text="Listo", anchor="w")
        self.estado.pack(side="bottom", fill="x")  # CORRECCIÓN 2
        self.lateral = tk.Frame(raiz, bg="#dddddd", width=150)
        self.lateral.pack(side="left", fill="y")  # CORRECCIÓN 1
        self.contenido = tk.Frame(raiz, bg="white")
        self.contenido.pack(side="left", fill="both", expand=True)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    app = Estructura(raiz)
    assert app.lateral.pack_info()["side"] == "left", "El menú lateral va a la izquierda"
    orden = raiz.pack_slaves()
    assert orden.index(app.estado) < orden.index(app.contenido), (
        "La barra de estado debe empacarse antes que el contenido"
    )
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        raiz.geometry("500x300")
        Estructura(raiz)
        raiz.mainloop()
