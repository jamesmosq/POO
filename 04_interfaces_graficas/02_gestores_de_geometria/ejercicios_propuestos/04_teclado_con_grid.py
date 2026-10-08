"""
Ejercicio propuesto 04 - Teclado con grid
Nivel: intermedio

Requisitos. Crea la clase Teclado(raiz) con un teclado de cajero:
1. self.pantalla: un Entry en la fila 0, ocupando las 3 columnas.
2. Botones del 1 al 9 en una cuadrícula de 3 x 3 (filas 1 a 3), creados
   con un ciclo. Calcula la fila y la columna con // y %.
3. Fila 4: botón "0" ocupando 2 columnas (columnspan=2) y botón "OK" en la
   columna 2.
4. Todos los botones con sticky="nsew", y todas las filas y columnas con
   weight=1, para que el teclado se estire al agrandar la ventana.
5. Guarda los botones en el diccionario self.botones (texto -> Button).
6. Cada número se agrega al final de self.pantalla al hacer clic.

Conceptos: grid con cálculo de posiciones, columnspan, weight, nsew.
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
    app = Teclado(raiz)

    assert app.pantalla.grid_info()["columnspan"] == 3
    for n in range(1, 10):
        info = app.botones[str(n)].grid_info()
        esperado = ((n - 1) // 3 + 1, (n - 1) % 3)
        assert (info["row"], info["column"]) == esperado, f"Botón {n}: {(info['row'], info['column'])}"
        assert info["sticky"] == "nesw"

    cero = app.botones["0"].grid_info()
    assert (cero["row"], cero["column"], cero["columnspan"]) == (4, 0, 2)
    assert app.botones["OK"].grid_info()["column"] == 2

    for i in range(5):
        assert raiz.rowconfigure(i)["weight"] == 1, f"Fila {i} sin weight"
    for i in range(3):
        assert raiz.columnconfigure(i)["weight"] == 1, f"Columna {i} sin weight"

    for tecla in "2026":
        app.botones[tecla].invoke()
    assert app.pantalla.get() == "2026"
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        Teclado(raiz)
        raiz.mainloop()
