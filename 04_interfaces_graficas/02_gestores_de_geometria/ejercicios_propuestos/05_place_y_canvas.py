"""
Ejercicio propuesto 05 - place y Canvas
Nivel: avanzado

place() ubica un widget por coordenadas. Con coordenadas RELATIVAS
(relx, rely entre 0 y 1) la posición se adapta al tamaño de la ventana:
    widget.place(relx=0.5, rely=0.5, anchor="center")   # centrado

Canvas es un widget para dibujar: líneas, rectángulos, óvalos y texto.

Requisitos. Crea la clase Tablero(raiz):
1. self.lienzo: un Canvas de 400x300 con fondo blanco, que llene la
   ventana (pack fill="both", expand=True).
2. dibujar_cuadricula(paso): dibuja líneas verticales y horizontales cada
   "paso" píxeles. Cada línea con la etiqueta (tag) "cuadricula". Antes de
   dibujar, borra la cuadrícula anterior: self.lienzo.delete("cuadricula").
   Llámalo en __init__ con paso 50.
3. agregar_circulo(x, y, radio): dibuja un óvalo con tag "circulo" y
   retorna su id.
4. self.titulo: un Label "Tablero" ubicado con place en la esquina
   superior derecha: relx=1, rely=0, anchor="ne".
5. self.boton_limpiar: Button "Limpiar" centrado abajo: relx=0.5,
   rely=1, anchor="s". Al hacer clic borra todos los círculos.

Conceptos: place con coordenadas relativas, anchor, Canvas, tags.
"""
import tkinter as tk

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
