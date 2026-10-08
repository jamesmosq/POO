"""
Solución - Ejercicio para corregir 03 - Formulario con opciones

CORRECCIÓN 1 (la talla XL no sumaba): self.talla.get sin paréntesis es el
método, no el valor elegido; compararlo con "XL" siempre da False.

CORRECCIÓN 2 (el envío express no sumaba): el Checkbutton no estaba
conectado a la variable self.express, así que marcarlo no la cambiaba. Se
conecta con variable=self.express.
"""

import tkinter as tk
from tkinter import ttk


class Pedido:
    def __init__(self, raiz):
        self.talla = ttk.Combobox(raiz, values=["S", "M", "L", "XL"], state="readonly")
        self.talla.pack()
        self.express = tk.BooleanVar(value=False)
        self.check = tk.Checkbutton(raiz, text="Envío express", variable=self.express)  # CORRECCIÓN 2
        self.check.pack()
        self.boton = tk.Button(raiz, text="Calcular", command=self.calcular)
        self.boton.pack()
        self.total = tk.Label(raiz, text="")
        self.total.pack()

    def calcular(self):
        precio = 50000
        if self.talla.get() == "XL":  # CORRECCIÓN 1
            precio += 5000
        if self.express.get():
            precio += 12000
        self.total.config(text=f"Total: {precio}")


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    app = Pedido(raiz)

    app.talla.set("M")
    app.boton.invoke()
    assert app.total.cget("text") == "Total: 50000"

    app.talla.set("XL")
    app.boton.invoke()
    assert app.total.cget("text") == "Total: 55000", app.total.cget("text")

    app.check.invoke()
    app.boton.invoke()
    assert app.total.cget("text") == "Total: 67000", app.total.cget("text")
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        Pedido(raiz)
        raiz.mainloop()
