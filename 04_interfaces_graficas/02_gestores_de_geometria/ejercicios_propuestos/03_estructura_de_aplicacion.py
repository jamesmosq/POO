"""
Ejercicio propuesto 03 - Estructura de una aplicación
Nivel: intermedio

La mayoría de las aplicaciones tienen la misma estructura: una barra
arriba, un menú lateral y un área de contenido que ocupa el resto. Se
construye con Frames y pack().

    +--------------------------------+
    |  barra (arriba, todo el ancho) |
    +--------+-----------------------+
    | lateral|  contenido            |
    | (izq.) |  (crece en ambas      |
    |        |   direcciones)        |
    +--------+-----------------------+
    |  estado (abajo, todo el ancho) |
    +--------------------------------+

Requisitos. Crea la clase Estructura(raiz) con cuatro Frames:
1. self.barra: side="top", fill="x".
2. self.estado: side="bottom", fill="x".
3. self.lateral: side="left", fill="y", width=150.
4. self.contenido: side="left", fill="both", expand=True.
5. Dentro de self.lateral, tres botones apilados ("Inicio", "Clientes",
   "Salir") con fill="x". Guárdalos en la lista self.botones.

IMPORTANTE: con pack el ORDEN importa. La barra de estado debe empacarse
ANTES que el lateral y el contenido, o quedará aplastada.

Conceptos: Frames como contenedores, pack con side, orden de empaquetado.
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
    app = Estructura(raiz)

    esperado = {
        "barra": ("top", "x", 0),
        "estado": ("bottom", "x", 0),
        "lateral": ("left", "y", 0),
        "contenido": ("left", "both", 1),
    }
    for nombre, (side, fill, expand) in esperado.items():
        info = getattr(app, nombre).pack_info()
        assert (info["side"], info["fill"], info["expand"]) == (side, fill, expand), f"{nombre}: {info}"

    orden = raiz.pack_slaves()
    assert orden.index(app.estado) < orden.index(app.lateral), "Empaca la barra de estado antes que el lateral"
    assert int(app.lateral.cget("width")) == 150

    assert [b.cget("text") for b in app.botones] == ["Inicio", "Clientes", "Salir"]
    assert all(b.master is app.lateral for b in app.botones), "Los botones van dentro del lateral"
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        raiz.geometry("600x400")
        Estructura(raiz)
        raiz.mainloop()
