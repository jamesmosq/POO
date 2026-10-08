"""
Solución - Ejercicio propuesto 03 - Herencia de formularios
"""

import tkinter as tk


class FormularioBase(tk.Frame):
    CAMPOS = []

    def __init__(self, master):
        super().__init__(master, padx=10, pady=10)
        self.entradas = {}
        self.guardados = []
        for fila, campo in enumerate(self.CAMPOS):
            tk.Label(self, text=campo).grid(row=fila, column=0, sticky="e")
            entrada = tk.Entry(self)
            entrada.grid(row=fila, column=1, pady=2)
            self.entradas[campo] = entrada
        self.boton = tk.Button(self, text="Guardar", command=self.guardar)
        self.boton.grid(row=len(self.CAMPOS), column=0, columnspan=2, pady=5)
        self.mensaje = tk.Label(self, text="")
        self.mensaje.grid(row=len(self.CAMPOS) + 1, column=0, columnspan=2)

    def validar(self, datos):
        for campo in self.CAMPOS:
            if not datos[campo]:
                return f"Falta {campo}"
        return None

    def guardar(self):
        datos = {campo: entrada.get().strip() for campo, entrada in self.entradas.items()}
        error = self.validar(datos)
        if error:
            self.mensaje.config(text=error)
            return
        self.guardados.append(datos)
        self.mensaje.config(text="Guardado")


class FormularioCliente(FormularioBase):
    CAMPOS = ["Nombre", "Correo"]

    def validar(self, datos):
        error = super().validar(datos)
        if error:
            return error
        if "@" not in datos["Correo"]:
            return "Correo inválido"
        return None


class FormularioProducto(FormularioBase):
    CAMPOS = ["Nombre", "Precio"]

    def validar(self, datos):
        error = super().validar(datos)
        if error:
            return error
        try:
            float(datos["Precio"])
        except ValueError:
            return "Precio inválido"
        return None


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()

    def enviar(formulario, valores):
        for campo, valor in valores.items():
            formulario.entradas[campo].delete(0, tk.END)
            formulario.entradas[campo].insert(0, valor)
        formulario.boton.invoke()
        return formulario.mensaje.cget("text")

    cliente = FormularioCliente(raiz)
    assert list(cliente.entradas) == ["Nombre", "Correo"]
    assert enviar(cliente, {"Nombre": "", "Correo": "a@b.co"}) == "Falta Nombre"
    assert enviar(cliente, {"Nombre": "Ana", "Correo": "ana"}) == "Correo inválido"
    assert enviar(cliente, {"Nombre": " Ana ", "Correo": "ana@mail.com"}) == "Guardado"
    assert cliente.guardados == [{"Nombre": "Ana", "Correo": "ana@mail.com"}]

    producto = FormularioProducto(raiz)
    assert list(producto.entradas) == ["Nombre", "Precio"]
    assert enviar(producto, {"Nombre": "Café", "Precio": ""}) == "Falta Precio"
    assert enviar(producto, {"Nombre": "Café", "Precio": "doce"}) == "Precio inválido"
    assert enviar(producto, {"Nombre": "Café", "Precio": "12000"}) == "Guardado"

    for clase in (FormularioCliente, FormularioProducto):
        assert "__init__" not in clase.__dict__, f"{clase.__name__} no necesita su propio __init__"
        assert "guardar" not in clase.__dict__
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        FormularioCliente(raiz).pack(padx=10, pady=10)
        FormularioProducto(raiz).pack(padx=10, pady=10)
        raiz.mainloop()
