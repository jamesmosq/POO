"""
Solución - Ejercicio para corregir 04 - Teclado que no crece

CORRECCIÓN 1 (TclError: bad option "-columspan"): la opción se escribe
columnspan.

CORRECCIÓN 2 (los botones 1, 2 y 3 quedaban en la fila de la pantalla): la
fila 0 es de la pantalla, así que los botones empiezan en la fila 1: se
suma 1 a la fila calculada.

CORRECCIÓN 3 (la tercera columna no crecía): range(2) solo configura las
columnas 0 y 1. Hay tres columnas: range(3).
"""

import tkinter as tk


class Teclado:
    def __init__(self, raiz):
        self.pantalla = tk.Entry(raiz)
        self.pantalla.grid(row=0, column=0, columnspan=3, sticky="ew")  # CORRECCIÓN 1
        self.botones = {}
        for n in range(1, 10):
            boton = tk.Button(raiz, text=str(n))
            boton.grid(row=(n - 1) // 3 + 1, column=(n - 1) % 3, sticky="nsew")  # CORRECCIÓN 2
            self.botones[n] = boton
        for columna in range(3):  # CORRECCIÓN 3
            raiz.columnconfigure(columna, weight=1)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    app = Teclado(raiz)
    assert app.pantalla.grid_info()["columnspan"] == 3
    assert app.botones[1].grid_info()["row"] == 1, "La fila 0 es de la pantalla"
    assert app.botones[9].grid_info()["row"] == 3
    for columna in range(3):
        assert raiz.columnconfigure(columna)["weight"] == 1, f"La columna {columna} no crece"
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        Teclado(raiz)
        raiz.mainloop()
