"""
Solución - Ejercicio propuesto 01 - Saludo
"""

import tkinter as tk


class Aplicacion:
    def __init__(self, raiz):
        raiz.title("Saludo")
        self.entrada = tk.Entry(raiz, width=30)
        self.entrada.pack(padx=10, pady=5)
        # command recibe la función SIN paréntesis: Tkinter la llamará en cada clic.
        self.boton = tk.Button(raiz, text="Saludar", command=self.saludar)
        self.boton.pack(pady=5)
        self.mensaje = tk.Label(raiz, text="")
        self.mensaje.pack(pady=5)

    def saludar(self):
        nombre = self.entrada.get().strip()
        if nombre:
            self.mensaje.config(text=f"Hola, {nombre}!")
        else:
            self.mensaje.config(text="Escribe tu nombre")


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    app = Aplicacion(raiz)

    assert raiz.title() == "Saludo"
    assert app.boton.cget("text") == "Saludar"
    for widget in (app.entrada, app.boton, app.mensaje):
        assert widget.winfo_manager() == "pack", "Ubica todos los widgets con pack()"

    app.boton.invoke()
    assert app.mensaje.cget("text") == "Escribe tu nombre"

    app.entrada.insert(0, "  Ana ")
    app.boton.invoke()
    assert app.mensaje.cget("text") == "Hola, Ana!"
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        Aplicacion(raiz)
        raiz.mainloop()
