"""
Solución - Ejercicio para corregir 02 - Contador quieto

CORRECCIÓN 1 (NameError: name 'sumar' is not defined): dentro de la clase,
los métodos se referencian a través del objeto: self.sumar.

CORRECCIÓN 2 (la etiqueta no cambiaba): self.valor.get() + 1 calcula el
número pero no lo guarda. Para cambiar una variable de Tkinter se usa
set(), y así la etiqueta conectada se actualiza sola.
"""

import tkinter as tk


class Contador(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.valor = tk.IntVar(value=0)
        self.etiqueta = tk.Label(self, textvariable=self.valor)
        self.etiqueta.pack()
        self.boton = tk.Button(self, text="+1", command=self.sumar)  # CORRECCIÓN 1
        self.boton.pack()

    def sumar(self):
        self.valor.set(self.valor.get() + 1)  # CORRECCIÓN 2


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    app = Contador(raiz)
    app.boton.invoke()
    app.boton.invoke()
    assert str(app.etiqueta.cget("text")) == "2", f"La etiqueta muestra {str(app.etiqueta.cget('text'))!r}"
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        Contador(raiz)
        raiz.mainloop()
