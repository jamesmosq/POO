import tkinter as tk
from tkinter import ttk

class VentanaBase(tk.Tk):
    def __init__(self, titulo, geometria):
        super().__init__()
        self.title(titulo)
        self.geometry(geometria)
        self.crear_widgets()

    def crear_widgets(self):
        # Método que será sobrescrito por las clases hijas
        pass

class VentanaPrincipal(VentanaBase):
    def __init__(self):
        super().__init__("Ventana Principal", "300x200")

    def crear_widgets(self):
        self.label = ttk.Label(self, text="Esta es la ventana principal")
        self.label.pack(pady=20)

        self.boton_abrir = ttk.Button(self, text="Abrir ventana secundaria", command=self.abrir_secundaria)
        self.boton_abrir.pack()

    def abrir_secundaria(self):
        VentanaSecundaria()

class VentanaSecundaria(VentanaBase):
    def __init__(self):
        super().__init__("Ventana Secundaria", "250x150")

    def crear_widgets(self):
        self.label = ttk.Label(self, text="Esta es una ventana secundaria")
        self.label.pack(pady=20)

        self.boton_cerrar = ttk.Button(self, text="Cerrar", command=self.destroy)
        self.boton_cerrar.pack()

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()