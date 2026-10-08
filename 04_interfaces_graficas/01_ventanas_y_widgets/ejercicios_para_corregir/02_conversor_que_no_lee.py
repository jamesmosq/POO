"""
Ejercicio para corregir 02 - Conversor que no lee
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    El usuario escribe una cantidad de kilómetros, hace clic en
    "Convertir" y la etiqueta muestra el equivalente en millas con dos
    decimales: 10 -> "6.21 millas".

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""
import tkinter as tk


class Conversor:
    def __init__(self, raiz):
        self.entrada = tk.Entry(raiz)
        self.entrada.pack()
        self.texto = self.entrada.get()
        self.boton = tk.Button(raiz, text="Convertir", command=self.convertir)
        self.boton.pack()
        self.resultado = tk.Label(raiz, text="")
        self.resultado.pack()

    def convertir(self):
        try:
            km = float(self.texto)
        except ValueError:
            km = 0
        self.resultado.text = f"{km * 0.621371:.2f} millas"


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    app = Conversor(raiz)
    app.entrada.insert(0, "10")
    app.boton.invoke()
    assert app.resultado.cget("text") == "6.21 millas", f"La etiqueta muestra {app.resultado.cget('text')!r}"
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        Conversor(raiz)
        raiz.mainloop()
