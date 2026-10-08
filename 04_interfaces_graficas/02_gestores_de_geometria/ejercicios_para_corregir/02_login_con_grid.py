"""
Ejercicio para corregir 02 - Login con grid
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    Un formulario de ingreso en cuadrícula:

        fila 0:  "Usuario"     [entrada usuario]
        fila 1:  "Contraseña"  [entrada clave]
        fila 2:  [   botón Ingresar, ocupa las 2 columnas   ]

Ojo: no hay excepciones. Los widgets "existen", pero quedan encimados o
mal distribuidos. Usa grid_info() para ver dónde quedó cada uno.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""
import tkinter as tk


class Login:
    def __init__(self, raiz):
        tk.Label(raiz, text="Usuario").grid(row=0, column=0)
        self.usuario = tk.Entry(raiz)
        self.usuario.grid(row=0, column=1)
        tk.Label(raiz, text="Contraseña").grid(row=1, column=0)
        self.clave = tk.Entry(raiz, show="*")
        self.clave.grid(row=0, column=1)
        self.boton = tk.Button(raiz, text="Ingresar")
        self.boton.grid(row=2, column=0)


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
