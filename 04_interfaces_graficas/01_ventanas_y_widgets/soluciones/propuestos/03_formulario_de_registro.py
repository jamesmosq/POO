"""
Solución - Ejercicio propuesto 03 - Formulario de registro
"""

import tkinter as tk
from tkinter import ttk

PROGRAMAS = ["Software", "Redes", "Diseño"]


class Formulario:
    def __init__(self, raiz):
        raiz.title("Registro")
        self.registros = []

        tk.Label(raiz, text="Nombre").pack(anchor="w", padx=10)
        self.nombre = tk.Entry(raiz, width=35)
        self.nombre.pack(padx=10)

        tk.Label(raiz, text="Email").pack(anchor="w", padx=10)
        self.email = tk.Entry(raiz, width=35)
        self.email.pack(padx=10)

        tk.Label(raiz, text="Programa").pack(anchor="w", padx=10)
        self.programa = ttk.Combobox(raiz, values=PROGRAMAS, state="readonly")
        self.programa.pack(padx=10, fill="x")

        self.acepta = tk.BooleanVar(value=False)
        self.check = tk.Checkbutton(raiz, text="Acepto los términos", variable=self.acepta)
        self.check.pack(pady=5)

        self.boton = tk.Button(raiz, text="Registrar", command=self.registrar)
        self.boton.pack()
        self.estado = tk.Label(raiz, text="")
        self.estado.pack(pady=5)

    def validar(self):
        if not self.nombre.get().strip():
            return "Falta el nombre"
        if "@" not in self.email.get():
            return "Email inválido"
        if not self.programa.get():
            return "Elige un programa"
        if not self.acepta.get():
            return "Debes aceptar los términos"
        return None

    def registrar(self):
        error = self.validar()
        if error:
            self.estado.config(text=error)
            return
        nombre = self.nombre.get().strip()
        self.registros.append({"nombre": nombre, "email": self.email.get().strip(), "programa": self.programa.get()})
        self.estado.config(text=f"Registrado: {nombre}")
        self.limpiar()

    def limpiar(self):
        self.nombre.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.programa.set("")
        self.acepta.set(False)


# ----------------------------------------------------------------------
# Pruebas
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
