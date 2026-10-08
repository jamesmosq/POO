"""
Ejercicio propuesto 01 - Saludo
Nivel: básico

Requisitos. Crea la clase Aplicacion que recibe la ventana principal
(raiz) y construye:
1. Título de la ventana: "Saludo"  (raiz.title(...))
2. self.entrada: un Entry donde se escribe el nombre.
3. self.boton: un Button con el texto "Saludar" que llama al método
   saludar.
4. self.mensaje: un Label, inicialmente vacío.
5. saludar(): lee el nombre (sin espacios al inicio y al final) y muestra
   en self.mensaje "Hola, Ana!". Si el nombre está vacío, muestra
   "Escribe tu nombre".

Ubica los widgets con pack(). Para cambiar el texto de un Label:
    self.mensaje.config(text="...")

Cuando las pruebas pasan, se abre la ventana para que la uses.

Conceptos: Tk, Entry, Button, Label, command, config.
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
    app = Aplicacion(raiz)

    assert raiz.title() == "Saludo"
    assert app.boton.cget("text") == "Saludar"
    for widget in (app.entrada, app.boton, app.mensaje):
        assert widget.winfo_manager() == "pack", "Ubica todos los widgets con pack()"

    app.boton.invoke()
    assert app.mensaje.cget("text") == "Escribe tu nombre"

    app.entrada.insert(0, "  Ana ")
    app.boton.invoke()
    assert app.mensaje.cget("text") == "Hola, Ana!"
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        Aplicacion(raiz)
        raiz.mainloop()
