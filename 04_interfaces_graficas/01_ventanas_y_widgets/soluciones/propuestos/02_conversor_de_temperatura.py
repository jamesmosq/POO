"""
Solución - Ejercicio propuesto 02 - Conversor de temperatura
"""

import tkinter as tk


class Conversor:
    def __init__(self, raiz):
        raiz.title("Conversor")
        tk.Label(raiz, text="Grados Celsius:").pack(padx=10, pady=(10, 0))
        self.entrada = tk.Entry(raiz)
        self.entrada.pack(padx=10, pady=5)
        self.entrada.bind("<Return>", lambda evento: self.convertir())
        self.boton = tk.Button(raiz, text="Convertir", command=self.convertir)
        self.boton.pack(pady=5)
        self.resultado = tk.Label(raiz, text="")
        self.resultado.pack(pady=(0, 10))

    def convertir(self):
        texto = self.entrada.get().strip().replace(",", ".")
        try:
            celsius = float(texto)
        except ValueError:
            self.resultado.config(text="Valor inválido")
            return
        self.resultado.config(text=f"{celsius * 9 / 5 + 32:.1f} °F")


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    app = Conversor(raiz)
    assert raiz.title() == "Conversor"
    assert app.boton.cget("text") == "Convertir"

    app.entrada.insert(0, "25")
    app.boton.invoke()
    assert app.resultado.cget("text") == "77.0 °F", app.resultado.cget("text")

    app.entrada.delete(0, tk.END)
    app.entrada.insert(0, "36,5")
    app.boton.invoke()
    assert app.resultado.cget("text") == "97.7 °F", app.resultado.cget("text")

    app.entrada.delete(0, tk.END)
    app.entrada.insert(0, "abc")
    app.boton.invoke()
    assert app.resultado.cget("text") == "Valor inválido"

    assert app.entrada.bind("<Return>"), "Falta asociar la tecla Enter al Entry"
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        Conversor(raiz)
        raiz.mainloop()
