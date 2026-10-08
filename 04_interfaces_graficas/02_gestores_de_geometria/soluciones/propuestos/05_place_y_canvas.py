"""
Solución - Ejercicio propuesto 05 - place y Canvas
"""

import tkinter as tk


class Tablero:
    ANCHO = 400
    ALTO = 300

    def __init__(self, raiz):
        raiz.title("Tablero")
        self.lienzo = tk.Canvas(raiz, width=self.ANCHO, height=self.ALTO, bg="white")
        self.lienzo.pack(fill="both", expand=True)
        self.dibujar_cuadricula(50)

        self.titulo = tk.Label(raiz, text="Tablero", bg="white")
        self.titulo.place(relx=1, rely=0, anchor="ne")
        self.boton_limpiar = tk.Button(raiz, text="Limpiar", command=self.limpiar)
        self.boton_limpiar.place(relx=0.5, rely=1, anchor="s")

    def dibujar_cuadricula(self, paso):
        self.lienzo.delete("cuadricula")
        for x in range(paso, self.ANCHO, paso):
            self.lienzo.create_line(x, 0, x, self.ALTO, fill="#dddddd", tags="cuadricula")
        for y in range(paso, self.ALTO, paso):
            self.lienzo.create_line(0, y, self.ANCHO, y, fill="#dddddd", tags="cuadricula")

    def agregar_circulo(self, x, y, radio):
        # create_oval recibe la caja que contiene al círculo: esquina superior
        # izquierda y esquina inferior derecha.
        return self.lienzo.create_oval(x - radio, y - radio, x + radio, y + radio,
                                       outline="#003893", width=2, tags="circulo")

    def limpiar(self):
        self.lienzo.delete("circulo")


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    app = Tablero(raiz)

    lineas = app.lienzo.find_withtag("cuadricula")
    assert len(lineas) == 400 // 50 - 1 + 300 // 50 - 1, f"Se dibujaron {len(lineas)} líneas"
    app.dibujar_cuadricula(100)
    assert len(app.lienzo.find_withtag("cuadricula")) == 3 + 2, "Al redibujar se debe borrar la cuadrícula anterior"

    app.agregar_circulo(100, 100, 20)
    app.agregar_circulo(200, 150, 30)
    assert len(app.lienzo.find_withtag("circulo")) == 2
    assert app.lienzo.coords(app.agregar_circulo(50, 60, 10)) == [40.0, 50.0, 60.0, 70.0]

    info = app.titulo.place_info()
    assert (info["relx"], info["rely"], info["anchor"]) == ("1", "0", "ne"), info
    info = app.boton_limpiar.place_info()
    assert (info["relx"], info["rely"], info["anchor"]) == ("0.5", "1", "s"), info

    app.boton_limpiar.invoke()
    assert app.lienzo.find_withtag("circulo") == ()
    assert len(app.lienzo.find_withtag("cuadricula")) == 5, "Limpiar no debe borrar la cuadrícula"
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        Tablero(raiz)
        raiz.mainloop()
