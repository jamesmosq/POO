"""
Ejercicio propuesto 01 - Contador como Frame
Nivel: básico

En aplicaciones reales cada parte de la interfaz es una clase que hereda de
tk.Frame. Así se puede reutilizar y probar por separado.

Requisitos. Crea la clase Contador(tk.Frame):
1. __init__(self, master): llama a super().__init__(master) y se ubica a sí
   misma con self.pack().
2. self.valor: un tk.IntVar con valor inicial 0.
3. self.etiqueta: Label que muestra el valor usando textvariable=self.valor
   (se actualiza sola cuando cambia la variable).
4. self.boton_sumar ("+1") y self.boton_reiniciar ("Reiniciar"), que
   llaman a los métodos sumar() y reiniciar().
5. Los widgets hijos se crean dentro de self (el Frame), no de la raíz.

Conceptos: heredar de tk.Frame, super(), variables de control, textvariable.
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
    app = Contador(raiz)

    assert isinstance(app, tk.Frame), "Contador debe heredar de tk.Frame"
    assert app.winfo_manager() == "pack", "El Frame debe ubicarse con self.pack()"
    assert app.etiqueta.master is app, "Los widgets van dentro del Frame"
    assert str(app.etiqueta.cget("text")) == "0"

    for _ in range(3):
        app.boton_sumar.invoke()
    assert app.valor.get() == 3
    assert str(app.etiqueta.cget("text")) == "3", "Usa textvariable para que la etiqueta se actualice sola"

    app.boton_reiniciar.invoke()
    assert str(app.etiqueta.cget("text")) == "0"

    otro = Contador(raiz)
    otro.boton_sumar.invoke()
    assert app.valor.get() == 0 and otro.valor.get() == 1, "Cada contador es independiente"
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        raiz.title("Dos contadores")
        Contador(raiz)
        Contador(raiz)
        raiz.mainloop()
