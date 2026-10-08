"""
Ejercicio para corregir 01 - Frame sin iniciar
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    Panel es un Frame con un título y un botón. Debe verse en la ventana.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""
import tkinter as tk


class Panel(tk.Frame):
    def __init__(self, master):
        self.titulo = tk.Label(self, text="Panel de control", font=("Arial", 14))
        self.titulo.pack(pady=5)
        self.boton = tk.Button(self, text="Actualizar")
        self.boton.pack(pady=5)


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    panel = Panel(raiz)
    assert panel.titulo.master is panel
    assert panel.winfo_manager() == "pack", "El Panel no se ubicó en la ventana"
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        Panel(raiz)
        raiz.mainloop()
