"""
Ejercicio para corregir 03 - Formulario con opciones
Nivel: intermedio
Errores a encontrar: 2

Qué debería hacer el programa:
    Un Combobox para elegir la talla y un Checkbutton "Envío express".
    Al hacer clic en "Calcular" se muestra el precio:
        precio base 50000; talla "XL" suma 5000; envío express suma 12000.

        Talla "XL" con express -> "Total: 67000"

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""
import tkinter as tk
from tkinter import ttk


class Pedido:
    def __init__(self, raiz):
        self.talla = ttk.Combobox(raiz, values=["S", "M", "L", "XL"], state="readonly")
        self.talla.pack()
        self.express = tk.BooleanVar(value=False)
        self.check = tk.Checkbutton(raiz, text="Envío express")
        self.check.pack()
        self.boton = tk.Button(raiz, text="Calcular", command=self.calcular)
        self.boton.pack()
        self.total = tk.Label(raiz, text="")
        self.total.pack()

    def calcular(self):
        precio = 50000
        if self.talla.get == "XL":
            precio += 5000
        if self.express.get():
            precio += 12000
        self.total.config(text=f"Total: {precio}")


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
