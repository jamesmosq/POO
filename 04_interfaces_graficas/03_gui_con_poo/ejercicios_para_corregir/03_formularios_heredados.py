"""
Ejercicio para corregir 03 - Formularios heredados
Nivel: intermedio
Errores a encontrar: 2

Qué debería hacer el programa:
    - FormularioBase crea los campos de CAMPOS y el botón Guardar. Su
      validar() exige que ningún campo esté vacío.
    - FormularioCliente agrega un campo de observaciones (un Text) a lo que
      ya crea la base, y su validar() exige además un "@" en el correo.

        Nombre vacío              -> "Falta Nombre"
        Correo sin @              -> "Correo inválido"
        Todo bien                 -> "Guardado"

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
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
        self.observaciones = tk.Text(self, height=3, width=30)
        self.observaciones.grid(row=10, column=0, columnspan=2)

    def validar(self, datos):
        super().validar(datos)
        if "@" not in datos["Correo"]:
            return "Correo inválido"
        return None


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
