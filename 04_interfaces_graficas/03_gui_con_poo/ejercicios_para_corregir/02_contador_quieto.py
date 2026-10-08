"""
Ejercicio para corregir 02 - Contador quieto
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    Un contador con un IntVar y una etiqueta conectada con textvariable.
    Cada clic en "+1" suma uno y la etiqueta se actualiza sola.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""
import tkinter as tk


class Contador(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.valor = tk.IntVar(value=0)
        self.etiqueta = tk.Label(self, textvariable=self.valor)
        self.etiqueta.pack()
        self.boton = tk.Button(self, text="+1", command=sumar)
        self.boton.pack()

    def sumar(self):
        self.valor.get() + 1


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    app = Contador(raiz)
    app.boton.invoke()
    app.boton.invoke()
    assert str(app.etiqueta.cget("text")) == "2", f"La etiqueta muestra {str(app.etiqueta.cget('text'))!r}"
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        Contador(raiz)
        raiz.mainloop()
