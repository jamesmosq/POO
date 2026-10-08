"""
Solución - Ejercicio propuesto 01 - Franjas con pack
"""

import tkinter as tk


class Bandera:
    def __init__(self, raiz):
        raiz.title("Colombia")
        raiz.geometry("300x200")
        self.amarillo = tk.Label(raiz, bg="#FCD116", height=4)
        self.azul = tk.Label(raiz, bg="#003893", height=2)
        self.rojo = tk.Label(raiz, bg="#CE1126", height=2)
        for franja in (self.amarillo, self.azul, self.rojo):
            franja.pack(side="top", fill="both", expand=True)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    app = Bandera(raiz)
    franjas = [app.amarillo, app.azul, app.rojo]
    colores = [f.cget("bg").upper() for f in franjas]
    assert colores == ["#FCD116", "#003893", "#CE1126"], colores

    assert raiz.pack_slaves() == franjas, "Las franjas deben estar en orden de arriba hacia abajo"
    for franja in franjas:
        info = franja.pack_info()
        assert info["fill"] == "both" and info["expand"] == 1, info
        assert info["side"] == "top"
    assert app.amarillo.cget("height") == 2 * app.azul.cget("height")
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        Bandera(raiz)
        raiz.mainloop()
