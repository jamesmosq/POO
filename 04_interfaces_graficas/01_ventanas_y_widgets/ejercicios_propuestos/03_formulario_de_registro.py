"""
Ejercicio propuesto 03 - Formulario de registro
Nivel: intermedio

Requisitos. Crea la clase Formulario(raiz) con:
1. self.nombre y self.email: Entry.
2. self.programa: ttk.Combobox de solo lectura (state="readonly") con los
   valores PROGRAMAS.
3. self.acepta: tk.BooleanVar, asociada a un Checkbutton
   "Acepto los términos" (self.check).
4. self.boton: Button "Registrar" que llama a registrar().
5. self.estado: Label con el resultado.
6. registrar() valida en este orden y muestra el primer error:
       nombre vacío            -> "Falta el nombre"
       email sin "@"           -> "Email inválido"
       programa sin elegir     -> "Elige un programa"
       términos sin aceptar    -> "Debes aceptar los términos"
   Si todo está bien:
       - agrega un diccionario {"nombre", "email", "programa"} a la lista
         self.registros,
       - muestra "Registrado: Ana",
       - limpia los campos (Entry vacíos, combobox sin elegir, check en
         False).

Conceptos: ttk.Combobox, Checkbutton, variables de control, validación.
"""
import tkinter as tk
from tkinter import ttk

PROGRAMAS = ["Software", "Redes", "Diseño"]

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    app = Formulario(raiz)
    assert list(app.programa.cget("values")) == PROGRAMAS

    def estado():
        app.boton.invoke()
        return app.estado.cget("text")

    assert estado() == "Falta el nombre"
    app.nombre.insert(0, "Ana")
    app.email.insert(0, "ana.mail.com")
    assert estado() == "Email inválido"
    app.email.delete(0, tk.END)
    app.email.insert(0, "ana@mail.com")
    assert estado() == "Elige un programa"
    app.programa.set("Redes")
    assert estado() == "Debes aceptar los términos"
    app.check.invoke()
    assert app.acepta.get() is True, "El Checkbutton debe usar la variable self.acepta"
    assert estado() == "Registrado: Ana"

    assert app.registros == [{"nombre": "Ana", "email": "ana@mail.com", "programa": "Redes"}]
    assert app.nombre.get() == "" and app.email.get() == "" and app.programa.get() == ""
    assert app.acepta.get() is False
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        Formulario(raiz)
        raiz.mainloop()
