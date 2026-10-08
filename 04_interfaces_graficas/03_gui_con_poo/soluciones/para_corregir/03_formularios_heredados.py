"""
Solución - Ejercicio para corregir 03 - Formularios heredados

CORRECCIÓN 1 (AttributeError: 'FormularioCliente' object has no attribute
'entradas'): la hija sobrescribía crear_widgets() y la base ya no creaba
sus campos. Para AGREGAR a lo que hace el padre se llama primero a
super().crear_widgets().

CORRECCIÓN 2 (con el nombre vacío decía "Guardado"): la hija llamaba a la
validación del padre pero ignoraba lo que retornaba. Si el padre encuentra
un error, hay que retornarlo.
"""

import tkinter as tk


class FormularioBase(tk.Frame):
    CAMPOS = []

    def __init__(self, master):
        super().__init__(master)
        self.crear_widgets()

    def crear_widgets(self):
        self.entradas = {}
        for fila, campo in enumerate(self.CAMPOS):
            tk.Label(self, text=campo).grid(row=fila, column=0)
            entrada = tk.Entry(self)
            entrada.grid(row=fila, column=1)
            self.entradas[campo] = entrada
        self.boton = tk.Button(self, text="Guardar", command=self.guardar)
        self.boton.grid(row=len(self.CAMPOS) + 1, column=0, columnspan=2)
        self.mensaje = tk.Label(self, text="")
        self.mensaje.grid(row=len(self.CAMPOS) + 2, column=0, columnspan=2)

    def validar(self, datos):
        for campo, valor in datos.items():
            if not valor:
                return f"Falta {campo}"
        return None

    def guardar(self):
        datos = {campo: entrada.get().strip() for campo, entrada in self.entradas.items()}
        error = self.validar(datos)
        self.mensaje.config(text=error or "Guardado")


class FormularioCliente(FormularioBase):
    CAMPOS = ["Nombre", "Correo"]

    def crear_widgets(self):
        super().crear_widgets()  # CORRECCIÓN 1
        self.observaciones = tk.Text(self, height=3, width=30)
        self.observaciones.grid(row=10, column=0, columnspan=2)

    def validar(self, datos):
        error = super().validar(datos)  # CORRECCIÓN 2
        if error:
            return error
        if "@" not in datos["Correo"]:
            return "Correo inválido"
        return None


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    form = FormularioCliente(raiz)

    def enviar(nombre, correo):
        form.entradas["Nombre"].delete(0, tk.END)
        form.entradas["Nombre"].insert(0, nombre)
        form.entradas["Correo"].delete(0, tk.END)
        form.entradas["Correo"].insert(0, correo)
        form.boton.invoke()
        return form.mensaje.cget("text")

    assert hasattr(form, "observaciones")
    assert enviar("", "ana@mail.com") == "Falta Nombre"
    assert enviar("Ana", "ana") == "Correo inválido"
    assert enviar("Ana", "ana@mail.com") == "Guardado"
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        FormularioCliente(raiz).pack(padx=10, pady=10)
        raiz.mainloop()
