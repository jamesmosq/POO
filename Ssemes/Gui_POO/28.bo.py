import tkinter as tk
from tkinter import messagebox


class VentanaSimple:
    def __init__(self, root):
        self.root = root
        self.root.title("Botones Simples")
        self.root.geometry("300x200")

        # Botón que muestra un mensaje
        self.boton1 = tk.Button(root,
                                text="Mostrar mensaje",
                                command=self.mostrar_mensaje)
        self.boton1.pack(pady=10)

        # Botón que cambia su texto
        self.boton2 = tk.Button(root,
                                text="Clic para cambiar",
                                command=self.cambiar_texto)
        self.boton2.pack(pady=10)

        # Botón que lee un Entry
        self.entrada = tk.Entry(root)
        self.entrada.pack(pady=10)

        self.boton3 = tk.Button(root,
                                text="Leer texto",
                                command=self.leer_texto)
        self.boton3.pack(pady=10)

    def mostrar_mensaje(self):
        messagebox.showinfo("Mensaje", "¡Hola! Has presionado el botón")

    def cambiar_texto(self):
        if self.boton2['text'] == "Clic para cambiar":
            self.boton2['text'] = "¡jghjgvjghvjhvjb!"
        else:
            self.boton2['text'] = "Clic para cambiar"

    def leer_texto(self):
        texto = self.entrada.get()
        messagebox.showinfo("Texto ingresado", f"El texto es: {texto}")


root = tk.Tk()
app = VentanaSimple(root)
root.mainloop()


