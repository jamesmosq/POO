"""
Ejercicio propuesto 02 - Formulario con grid
Nivel: básico

grid() ubica los widgets en una cuadrícula de filas y columnas:
    widget.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
    sticky: hacia qué lados se pega el widget dentro de su celda
            ("n", "s", "e", "w" y combinaciones como "ew").

Requisitos. Crea la clase Formulario(raiz) con un formulario de 3 campos:
1. Para cada campo de CAMPOS, un Label en la columna 0 (pegado a la
   derecha: sticky="e") y un Entry en la columna 1 (sticky="ew"), en la
   misma fila. Guarda los Entry en el diccionario self.entradas
   (clave = nombre del campo).
2. self.boton: Button "Guardar" en la fila 3, ocupando las dos columnas
   (columnspan=2).
3. La columna 1 debe crecer cuando la ventana se agranda:
       raiz.columnconfigure(1, weight=1)
4. Crea los Label y Entry con un ciclo sobre CAMPOS.

Conceptos: grid, row, column, sticky, columnspan, columnconfigure.
"""
import tkinter as tk

CAMPOS = ["Nombre", "Correo", "Teléfono"]

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    app = Formulario(raiz)

    assert list(app.entradas) == CAMPOS
    for fila, campo in enumerate(CAMPOS):
        info = app.entradas[campo].grid_info()
        assert (info["row"], info["column"]) == (fila, 1), f"{campo}: {info}"
        assert info["sticky"] == "ew"
        etiquetas = raiz.grid_slaves(row=fila, column=0)
        assert len(etiquetas) == 1 and etiquetas[0].cget("text") == campo
        assert etiquetas[0].grid_info()["sticky"] == "e"

    info = app.boton.grid_info()
    assert (info["row"], info["columnspan"]) == (3, 2), info
    assert raiz.columnconfigure(1)["weight"] == 1
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        Formulario(raiz)
        raiz.mainloop()
