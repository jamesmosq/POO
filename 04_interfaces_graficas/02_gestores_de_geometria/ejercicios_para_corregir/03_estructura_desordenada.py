"""
Ejercicio para corregir 03 - Estructura desordenada
Nivel: intermedio
Errores a encontrar: 2

Qué debería hacer el programa:
    Barra de estado abajo (todo el ancho), menú lateral a la IZQUIERDA y el
    contenido ocupando el resto del espacio.

Pista: con pack, el orden en que se empacan los widgets importa. Un widget
con expand=True toma todo el espacio sobrante que quede en ese momento.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""
import tkinter as tk


class Estructura:
    def __init__(self, raiz):
        self.lateral = tk.Frame(raiz, bg="#dddddd", width=150)
        self.lateral.pack(side="right", fill="y")
        self.contenido = tk.Frame(raiz, bg="white")
        self.contenido.pack(side="left", fill="both", expand=True)
        self.estado = tk.Label(raiz, text="Listo", anchor="w")
        self.estado.pack(side="bottom", fill="x")


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    app = Estructura(raiz)
    assert app.lateral.pack_info()["side"] == "left", "El menú lateral va a la izquierda"
    orden = raiz.pack_slaves()
    assert orden.index(app.estado) < orden.index(app.contenido), (
        "La barra de estado debe empacarse antes que el contenido"
    )
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        raiz.geometry("500x300")
        Estructura(raiz)
        raiz.mainloop()
