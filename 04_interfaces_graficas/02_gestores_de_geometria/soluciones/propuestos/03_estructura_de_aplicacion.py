"""
Solución - Ejercicio propuesto 03 - Estructura de una aplicación
"""

import tkinter as tk


class Estructura:
    def __init__(self, raiz):
        raiz.title("Aplicación")
        self.barra = tk.Frame(raiz, bg="#003893", height=40)
        self.barra.pack(side="top", fill="x")

        # La barra de estado se empaca ANTES que lateral y contenido; si no,
        # el contenido (expand=True) tomaría todo el espacio y la aplastaría.
        self.estado = tk.Frame(raiz, bg="#dddddd", height=25)
        self.estado.pack(side="bottom", fill="x")

        self.lateral = tk.Frame(raiz, bg="#eeeeee", width=150)
        self.lateral.pack(side="left", fill="y")
        self.contenido = tk.Frame(raiz, bg="white")
        self.contenido.pack(side="left", fill="both", expand=True)

        self.botones = []
        for texto in ("Inicio", "Clientes", "Salir"):
            boton = tk.Button(self.lateral, text=texto)
            boton.pack(fill="x", padx=5, pady=2)
            self.botones.append(boton)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    app = Estructura(raiz)

    esperado = {
        "barra": ("top", "x", 0),
        "estado": ("bottom", "x", 0),
        "lateral": ("left", "y", 0),
        "contenido": ("left", "both", 1),
    }
    for nombre, (side, fill, expand) in esperado.items():
        info = getattr(app, nombre).pack_info()
        assert (info["side"], info["fill"], info["expand"]) == (side, fill, expand), f"{nombre}: {info}"

    orden = raiz.pack_slaves()
    assert orden.index(app.estado) < orden.index(app.lateral), "Empaca la barra de estado antes que el lateral"
    assert int(app.lateral.cget("width")) == 150

    assert [b.cget("text") for b in app.botones] == ["Inicio", "Clientes", "Salir"]
    assert all(b.master is app.lateral for b in app.botones), "Los botones van dentro del lateral"
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        raiz.geometry("600x400")
        Estructura(raiz)
        raiz.mainloop()
