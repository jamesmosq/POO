"""
Ejercicio para corregir 05 - Tablero con place
Nivel: avanzado
Errores a encontrar: 3

Qué debería hacer el programa:
    - Un Canvas con una cuadrícula (tag "cuadricula").
    - agregar_circulo(x, y, radio): dibuja un círculo CENTRADO en (x, y),
      con tag "circulo".
    - Un botón "Limpiar" centrado en la ventana con place
      (relx=0.5, rely=0.5). Al hacer clic borra solo los círculos.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""
import tkinter as tk


class Tablero:
    def __init__(self, raiz):
        self.lienzo = tk.Canvas(raiz, width=300, height=200, bg="white")
        self.lienzo.pack(fill="both", expand=True)
        for x in range(50, 300, 50):
            self.lienzo.create_line(x, 0, x, 200, fill="#cccccc", tags="cuadricula")
        self.boton = tk.Button(raiz, text="Limpiar", command=self.limpiar)
        self.boton.place(relx=0.5, rely=0.5, anchor="centre")

    def agregar_circulo(self, x, y, radio):
        return self.lienzo.create_oval(x, y, x + radio, y + radio, tags="circulo")

    def limpiar(self):
        self.lienzo.delete("all")


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    app = Tablero(raiz)
    assert app.boton.place_info()["anchor"] == "center"

    circulo = app.agregar_circulo(100, 100, 10)
    assert app.lienzo.coords(circulo) == [90.0, 90.0, 110.0, 110.0], app.lienzo.coords(circulo)

    app.boton.invoke()
    assert app.lienzo.find_withtag("circulo") == ()
    assert len(app.lienzo.find_withtag("cuadricula")) == 5, "Limpiar borró también la cuadrícula"
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        Tablero(raiz)
        raiz.mainloop()
