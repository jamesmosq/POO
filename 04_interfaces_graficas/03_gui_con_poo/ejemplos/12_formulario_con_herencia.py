import tkinter as tk
from tkinter import ttk, messagebox

class VentanaBase(tk.Toplevel):
    def __init__(self, parent, titulo):
        super().__init__(parent)
        self.title(titulo)
        self.geometry("300x200")
        self.resizable(False, False)
        self.parent = parent
        self.crear_widgets()

    def crear_widgets(self):
        pass

class FormularioUsuario(VentanaBase):
    def __init__(self, parent, titulo, callback):
        self.callback = callback
        super().__init__(parent, titulo)

    def crear_widgets(self):
        ttk.Label(self, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        self.nombre = ttk.Entry(self)
        self.nombre.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self, text="Edad:").grid(row=1, column=0, padx=5, pady=5)
        self.edad = ttk.Entry(self)
        self.edad.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(self, text="Guardar", command=self.guardar).grid(row=2, column=0, columnspan=2, pady=10)

    def guardar(self):
        nombre = self.nombre.get()
        edad = self.edad.get()
        if nombre and edad:
            self.callback(f"{nombre} ({edad})")
            self.destroy()
        else:
            messagebox.showerror("Error", "Por favor, completa todos los campos.")

class ListaUsuarios(VentanaBase):
    def __init__(self, parent, titulo):
        super().__init__(parent, titulo)

    def crear_widgets(self):
        self.lista = tk.Listbox(self, width=40)
        self.lista.pack(padx=10, pady=10)

        ttk.Button(self, text="Cerrar", command=self.destroy).pack(pady=5)

    def agregar_usuario(self, usuario):
        self.lista.insert(tk.END, usuario)

class AplicacionPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Usuarios")
        self.geometry("300x200")
        self.resizable(False, False)
        self.crear_widgets()

    def crear_widgets(self):
        ttk.Button(self, text="Nuevo Usuario", command=self.abrir_formulario).pack(pady=20)
        ttk.Button(self, text="Ver Usuarios", command=self.ver_usuarios).pack(pady=10)
        ttk.Button(self, text="Salir", command=self.quit).pack(pady=10)

        self.usuarios = []

    def abrir_formulario(self):
        FormularioUsuario(self, "Nuevo Usuario", self.agregar_usuario)

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
        messagebox.showinfo("Éxito", f"Usuario {usuario} agregado correctamente.")

    def ver_usuarios(self):
        ventana_lista = ListaUsuarios(self, "Lista de Usuarios")
        for usuario in self.usuarios:
            ventana_lista.agregar_usuario(usuario)

if __name__ == "__main__":
    app = AplicacionPrincipal()
    app.mainloop()
