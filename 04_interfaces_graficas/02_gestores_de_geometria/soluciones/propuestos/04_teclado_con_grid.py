"""
Solución - Ejercicio propuesto 04 - Teclado con grid
"""

import tkinter as tk


class Teclado:
    def __init__(self, raiz):
        raiz.title("Cajero")
        self.pantalla = tk.Entry(raiz, justify="right", font=("Arial", 16))
        self.pantalla.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=5, pady=5)
        self.botones = {}
        for n in range(1, 10):
            fila = (n - 1) // 3 + 1
            columna = (n - 1) % 3
            self._crear_boton(raiz, str(n), fila, columna)
        self._crear_boton(raiz, "0", 4, 0, columnspan=2)
        self._crear_boton(raiz, "OK", 4, 2)
        for i in range(5):
            raiz.rowconfigure(i, weight=1)
        for i in range(3):
            raiz.columnconfigure(i, weight=1)

    def _crear_boton(self, raiz, texto, fila, columna, columnspan=1):
        boton = tk.Button(raiz, text=texto, command=lambda t=texto: self.presionar(t))
        boton.grid(row=fila, column=columna, columnspan=columnspan, sticky="nsew", padx=2, pady=2)
        self.botones[texto] = boton

    def presionar(self, tecla):
        if tecla.isdigit():
            self.pantalla.insert(tk.END, tecla)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    app = Teclado(raiz)

    assert app.pantalla.grid_info()["columnspan"] == 3
    for n in range(1, 10):
        info = app.botones[str(n)].grid_info()
        esperado = ((n - 1) // 3 + 1, (n - 1) % 3)
        assert (info["row"], info["column"]) == esperado, f"Botón {n}: {(info['row'], info['column'])}"
        assert info["sticky"] == "nesw"

    cero = app.botones["0"].grid_info()
    assert (cero["row"], cero["column"], cero["columnspan"]) == (4, 0, 2)
    assert app.botones["OK"].grid_info()["column"] == 2

    for i in range(5):
        assert raiz.rowconfigure(i)["weight"] == 1, f"Fila {i} sin weight"
    for i in range(3):
        assert raiz.columnconfigure(i)["weight"] == 1, f"Columna {i} sin weight"

    for tecla in "2026":
        app.botones[tecla].invoke()
    assert app.pantalla.get() == "2026"
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        Teclado(raiz)
        raiz.mainloop()
