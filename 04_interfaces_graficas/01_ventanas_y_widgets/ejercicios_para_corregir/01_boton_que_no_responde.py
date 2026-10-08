"""
Ejercicio para corregir 01 - Botón que no responde
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    Una ventana con una etiqueta y un botón "Contar". Al abrir, la etiqueta
    muestra "Clics: 0" y cada clic suma uno. Los dos widgets deben verse en
    la ventana.

Ojo: ninguno de los dos errores lanza una excepción. Uno hace que algo no
se vea y el otro hace que el botón actúe en el momento equivocado.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""
import tkinter as tk


class Aplicacion:
    def __init__(self, raiz):
        self.clics = 0
        self.etiqueta = tk.Label(raiz, text="Clics: 0")
        self.boton = tk.Button(raiz, text="Contar", command=self.contar())
        self.boton.pack()

    def contar(self):
        self.clics += 1
        self.etiqueta.config(text=f"Clics: {self.clics}")


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    app = Aplicacion(raiz)
    assert app.etiqueta.winfo_manager() == "pack", "La etiqueta no se ubicó en la ventana"
    assert app.etiqueta.cget("text") == "Clics: 0", "La etiqueta cambió antes de hacer clic"
    app.boton.invoke()
    app.boton.invoke()
    assert app.etiqueta.cget("text") == "Clics: 2", app.etiqueta.cget("text")
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        Aplicacion(raiz)
        raiz.mainloop()
