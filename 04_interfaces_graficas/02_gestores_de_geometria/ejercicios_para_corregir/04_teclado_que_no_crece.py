"""
Ejercicio para corregir 04 - Teclado que no crece
Nivel: intermedio
Errores a encontrar: 3

Qué debería hacer el programa:
    Pantalla en la fila 0 (ocupa 3 columnas) y los botones del 1 al 9 en
    las filas 1 a 3. Todas las columnas deben crecer al agrandar la
    ventana (weight=1).

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""
import tkinter as tk


class Teclado:
    def __init__(self, raiz):
        self.pantalla = tk.Entry(raiz)
        self.pantalla.grid(row=0, column=0, columspan=3, sticky="ew")
        self.botones = {}
        for n in range(1, 10):
            boton = tk.Button(raiz, text=str(n))
            boton.grid(row=(n - 1) // 3, column=(n - 1) % 3, sticky="nsew")
            self.botones[n] = boton
        for columna in range(2):
            raiz.columnconfigure(columna, weight=1)


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    app = Teclado(raiz)
    assert app.pantalla.grid_info()["columnspan"] == 3
    assert app.botones[1].grid_info()["row"] == 1, "La fila 0 es de la pantalla"
    assert app.botones[9].grid_info()["row"] == 3
    for columna in range(3):
        assert raiz.columnconfigure(columna)["weight"] == 1, f"La columna {columna} no crece"
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        Teclado(raiz)
        raiz.mainloop()
