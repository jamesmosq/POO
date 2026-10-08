"""
Ejercicio propuesto 01 - Franjas con pack
Nivel: básico

pack() apila los widgets uno tras otro. Sus opciones principales:
    side    "top" (por defecto), "bottom", "left", "right"
    fill    "x", "y", "both": estirarse para llenar el espacio
    expand  True: tomar el espacio sobrante cuando la ventana crece

Requisitos. Crea la clase Bandera(raiz) que dibuje la bandera de Colombia
con tres Labels:
1. self.amarillo (bg="#FCD116"), self.azul (bg="#003893") y
   self.rojo (bg="#CE1126"), en ese orden de arriba hacia abajo.
2. Los tres con fill="both" y expand=True, para que llenen la ventana.
3. La franja amarilla debe ocupar el doble de alto que las otras. Pista:
   usa la opción height de los Label (en líneas de texto): 4 para la
   amarilla y 2 para las demás.
4. Tamaño inicial de la ventana: 300x200 (raiz.geometry).

Conceptos: pack, side, fill, expand.
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
    app = Bandera(raiz)
    franjas = [app.amarillo, app.azul, app.rojo]
    colores = [f.cget("bg").upper() for f in franjas]
    assert colores == ["#FCD116", "#003893", "#CE1126"], colores

    assert raiz.pack_slaves() == franjas, "Las franjas deben estar en orden de arriba hacia abajo"
    for franja in franjas:
        info = franja.pack_info()
        assert info["fill"] == "both" and info["expand"] == 1, info
        assert info["side"] == "top"
    assert app.amarillo.cget("height") == 2 * app.azul.cget("height")
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        Bandera(raiz)
        raiz.mainloop()
