"""
Solución - Ejercicio propuesto 02 - Formulario con grid
"""

import tkinter as tk

CAMPOS = ["Nombre", "Correo", "Teléfono"]


class Formulario:
    def __init__(self, raiz):
        raiz.title("Formulario")
        self.entradas = {}
        for fila, campo in enumerate(CAMPOS):
            tk.Label(raiz, text=campo).grid(row=fila, column=0, sticky="e", padx=5, pady=5)
            entrada = tk.Entry(raiz)
            entrada.grid(row=fila, column=1, sticky="ew", padx=5, pady=5)
            self.entradas[campo] = entrada
        self.boton = tk.Button(raiz, text="Guardar")
        self.boton.grid(row=len(CAMPOS), column=0, columnspan=2, pady=10)
        raiz.columnconfigure(1, weight=1)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    app = Formulario(raiz)

    assert list(app.entradas) == CAMPOS
    for fila, campo in enumerate(CAMPOS):
        info = app.entradas[campo].grid_info()
        assert (info["row"], info["column"]) == (fila, 1), f"{campo}: {info}"
        assert info["sticky"] == "ew"
        etiquetas = raiz.grid_slaves(row=fila, column=0)
        assert len(etiquetas) == 1 and etiquetas[0].cget("text") == campo
        assert etiquetas[0].grid_info()["sticky"] == "e"

    info = app.boton.grid_info()
    assert (info["row"], info["columnspan"]) == (3, 2), info
    assert raiz.columnconfigure(1)["weight"] == 1
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        Formulario(raiz)
        raiz.mainloop()
