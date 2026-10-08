"""
Solución - Ejercicio para corregir 01 - Frame sin iniciar

CORRECCIÓN 1 (AttributeError: 'Panel' object has no attribute 'tk'): una
clase que hereda de tk.Frame debe llamar a super().__init__(master) antes
de crear widgets dentro de ella. Ese __init__ es el que crea el Frame real
en la ventana.

CORRECCIÓN 2 (el panel no se veía): como cualquier widget, el Frame
necesita ubicarse con pack(), grid() o place().
"""

import tkinter as tk


class Panel(tk.Frame):
    def __init__(self, master):
        super().__init__(master)  # CORRECCIÓN 1
        self.pack(padx=10, pady=10)  # CORRECCIÓN 2
        self.titulo = tk.Label(self, text="Panel de control", font=("Arial", 14))
        self.titulo.pack(pady=5)
        self.boton = tk.Button(self, text="Actualizar")
        self.boton.pack(pady=5)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    panel = Panel(raiz)
    assert panel.titulo.master is panel
    assert panel.winfo_manager() == "pack", "El Panel no se ubicó en la ventana"
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        Panel(raiz)
        raiz.mainloop()
