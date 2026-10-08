"""
Solución - Ejercicio para corregir 02 - Conversor que no lee

CORRECCIÓN 1 (la etiqueta no cambiaba): self.resultado.text = ... crea un
atributo de Python que Tkinter ignora. Para cambiar lo que muestra un
widget se usa config(text=...).

CORRECCIÓN 2 (siempre convertía 0): el texto del Entry se leía en
__init__, cuando el campo estaba vacío, y ese valor no cambia después. Hay
que leer self.entrada.get() dentro de convertir(), en el momento del clic.
"""

import tkinter as tk


class Conversor:
    def __init__(self, raiz):
        self.entrada = tk.Entry(raiz)
        self.entrada.pack()
        self.boton = tk.Button(raiz, text="Convertir", command=self.convertir)
        self.boton.pack()
        self.resultado = tk.Label(raiz, text="")
        self.resultado.pack()

    def convertir(self):
        try:
            km = float(self.entrada.get())  # CORRECCIÓN 2
        except ValueError:
            km = 0
        self.resultado.config(text=f"{km * 0.621371:.2f} millas")  # CORRECCIÓN 1


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    app = Conversor(raiz)
    app.entrada.insert(0, "10")
    app.boton.invoke()
    assert app.resultado.cget("text") == "6.21 millas", f"La etiqueta muestra {app.resultado.cget('text')!r}"
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        Conversor(raiz)
        raiz.mainloop()
