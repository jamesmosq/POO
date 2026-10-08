"""
Solución - Ejercicio para corregir 02 - Login con grid

CORRECCIÓN 1 (la clave quedaba encima del usuario): la entrada de la clave
estaba en row=0, la misma celda que la del usuario. grid no avisa cuando
dos widgets comparten celda: simplemente los encima.

CORRECCIÓN 2 (el botón ocupaba una sola columna): para que un widget se
extienda por varias columnas se usa columnspan.
"""

import tkinter as tk


class Login:
    def __init__(self, raiz):
        tk.Label(raiz, text="Usuario").grid(row=0, column=0)
        self.usuario = tk.Entry(raiz)
        self.usuario.grid(row=0, column=1)
        tk.Label(raiz, text="Contraseña").grid(row=1, column=0)
        self.clave = tk.Entry(raiz, show="*")
        self.clave.grid(row=1, column=1)  # CORRECCIÓN 1
        self.boton = tk.Button(raiz, text="Ingresar")
        self.boton.grid(row=2, column=0, columnspan=2)  # CORRECCIÓN 2


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    app = Login(raiz)
    posicion = lambda w: (w.grid_info()["row"], w.grid_info()["column"])
    assert posicion(app.usuario) == (0, 1)
    assert posicion(app.clave) == (1, 1), f"La clave quedó en {posicion(app.clave)}"
    assert app.boton.grid_info()["columnspan"] == 2, "El botón debe ocupar las dos columnas"
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        Login(raiz)
        raiz.mainloop()
