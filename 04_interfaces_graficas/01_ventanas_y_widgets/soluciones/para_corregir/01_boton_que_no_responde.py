"""
Solución - Ejercicio para corregir 01 - Botón que no responde

CORRECCIÓN 1 (la etiqueta no aparecía): crear un widget no lo muestra;
hay que ubicarlo con pack(), grid() o place().

CORRECCIÓN 2 (contaba antes del clic y después no hacía nada):
command=self.contar() EJECUTA la función al crear el botón y le pasa a
command su resultado (None). Se debe pasar la función sin paréntesis:
command=self.contar. Tkinter la llamará en cada clic.
"""

import tkinter as tk


class Aplicacion:
    def __init__(self, raiz):
        self.clics = 0
        self.etiqueta = tk.Label(raiz, text="Clics: 0")
        self.etiqueta.pack()  # CORRECCIÓN 1
        self.boton = tk.Button(raiz, text="Contar", command=self.contar)  # CORRECCIÓN 2
        self.boton.pack()

    def contar(self):
        self.clics += 1
        self.etiqueta.config(text=f"Clics: {self.clics}")


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    app = Aplicacion(raiz)
    assert app.etiqueta.winfo_manager() == "pack", "La etiqueta no se ubicó en la ventana"
    assert app.etiqueta.cget("text") == "Clics: 0", "La etiqueta cambió antes de hacer clic"
    app.boton.invoke()
    app.boton.invoke()
    assert app.etiqueta.cget("text") == "Clics: 2", app.etiqueta.cget("text")
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        Aplicacion(raiz)
        raiz.mainloop()
