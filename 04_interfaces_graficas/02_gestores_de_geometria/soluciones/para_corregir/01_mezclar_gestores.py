"""
Solución - Ejercicio para corregir 01 - Mezclar gestores

CORRECCIÓN 1 (TclError: cannot use geometry manager grid inside . which
already has slaves managed by pack): dentro de un mismo contenedor no se
pueden mezclar pack y grid. Se usa uno solo; aquí, pack. (Sí se pueden
usar distintos gestores en contenedores DISTINTOS, por ejemplo grid dentro
de un Frame que está ubicado con pack.)

CORRECCIÓN 2 (el encabezado no ocupaba todo el ancho): sin fill="x", un
widget ocupa solo lo que necesita su texto.
"""

import tkinter as tk


class Pagina:
    def __init__(self, raiz):
        self.encabezado = tk.Label(raiz, text="Mi aplicación", bg="#003893", fg="white")
        self.encabezado.pack(side="top", fill="x")  # CORRECCIÓN 2
        self.contenido = tk.Label(raiz, text="Bienvenido")
        self.contenido.pack(fill="both", expand=True)  # CORRECCIÓN 1


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    app = Pagina(raiz)
    assert app.encabezado.pack_info()["fill"] == "x", "El encabezado debe ocupar todo el ancho"
    info = app.contenido.pack_info()
    assert info["fill"] == "both" and info["expand"] == 1
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        Pagina(raiz)
        raiz.mainloop()
