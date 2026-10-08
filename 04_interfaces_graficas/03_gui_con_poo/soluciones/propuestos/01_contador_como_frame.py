"""
Solución - Ejercicio propuesto 01 - Contador como Frame
"""

import tkinter as tk


class Contador(tk.Frame):
    def __init__(self, master):
        super().__init__(master, padx=10, pady=10)
        self.pack()
        self.valor = tk.IntVar(value=0)
        self.etiqueta = tk.Label(self, textvariable=self.valor, font=("Arial", 24))
        self.etiqueta.pack()
        self.boton_sumar = tk.Button(self, text="+1", command=self.sumar)
        self.boton_sumar.pack(side="left", padx=5)
        self.boton_reiniciar = tk.Button(self, text="Reiniciar", command=self.reiniciar)
        self.boton_reiniciar.pack(side="left", padx=5)

    def sumar(self):
        self.valor.set(self.valor.get() + 1)

    def reiniciar(self):
        self.valor.set(0)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    app = Contador(raiz)

    assert isinstance(app, tk.Frame), "Contador debe heredar de tk.Frame"
    assert app.winfo_manager() == "pack", "El Frame debe ubicarse con self.pack()"
    assert app.etiqueta.master is app, "Los widgets van dentro del Frame"
    assert str(app.etiqueta.cget("text")) == "0"

    for _ in range(3):
        app.boton_sumar.invoke()
    assert app.valor.get() == 3
    assert str(app.etiqueta.cget("text")) == "3", "Usa textvariable para que la etiqueta se actualice sola"

    app.boton_reiniciar.invoke()
    assert str(app.etiqueta.cget("text")) == "0"

    otro = Contador(raiz)
    otro.boton_sumar.invoke()
    assert app.valor.get() == 0 and otro.valor.get() == 1, "Cada contador es independiente"
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        raiz.title("Dos contadores")
        Contador(raiz)
        Contador(raiz)
        raiz.mainloop()
