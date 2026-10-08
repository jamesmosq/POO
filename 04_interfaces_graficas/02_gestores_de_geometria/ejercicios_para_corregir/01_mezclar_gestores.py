"""
Ejercicio para corregir 01 - Mezclar gestores
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    Una ventana con un encabezado arriba, que ocupe todo el ancho, y un
    texto de contenido debajo, que ocupe el resto del espacio.

Pista: lee con atención el mensaje del primer error. Tkinter explica
exactamente qué está mal.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""
import tkinter as tk


class Pagina:
    def __init__(self, raiz):
        self.encabezado = tk.Label(raiz, text="Mi aplicación", bg="#003893", fg="white")
        self.encabezado.pack(side="top")
        self.contenido = tk.Label(raiz, text="Bienvenido")
        self.contenido.grid(row=1, column=0)


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
