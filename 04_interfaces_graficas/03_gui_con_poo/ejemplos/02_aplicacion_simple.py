import tkinter as tk
from tkinter import messagebox


class AplicacionSimple:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejemplo Básico")
        self.root.geometry("300x400")

        # Entry para el nombre
        self.label_nombre = tk.Label(root, text="Escribe tu nombre:")
        self.label_nombre.pack(pady=10)

        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.pack(pady=5)

        # Entry para la edad
        self.label_edad = tk.Label(root, text="Escribe tu edad:")
        self.label_edad.pack(pady=10)

        self.entry_edad = tk.Entry(root)
        self.entry_edad.pack(pady=5)

        # Botón para saludar
        self.boton_saludar = tk.Button(root,
                                       text="¡Saludar!",
                                       command=self.saludar)
        self.boton_saludar.pack(pady=20)

        # Botón para limpiar
        self.boton_limpiar = tk.Button(root,
                                       text="Limpiar campos",
                                       command=self.limpiar_campos)
        self.boton_limpiar.pack(pady=10)

        # Etiqueta para mostrar resultado
        self.label_resultado = tk.Label(root, text="")
        self.label_resultado.pack(pady=20)

    def saludar(self):
        """Función que se ejecuta al presionar el botón saludar"""
        nombre = self.entry_nombre.get()
        edad = self.entry_edad.get()

        if nombre and edad:
            mensaje = f"¡Hola {nombre}! Tienes {edad} años."
            self.label_resultado.config(text=mensaje)
        else:
            messagebox.showwarning("Atención", "Por favor, completa todos los campos")

    def limpiar_campos(self):
        """Función que limpia todos los campos"""
        self.entry_nombre.delete(0, tk.END)
        self.entry_edad.delete(0, tk.END)
        self.label_resultado.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionSimple(root)
    root.mainloop()