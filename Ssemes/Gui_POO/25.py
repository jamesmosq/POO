import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class AplicacionPersonal:
    def __init__(self, root):
        self.root = root
        self.root.title("Datos personales")
        self.root.geometry("400x300")

        # Frame principal con padding
        self.frame_principal = ttk.Frame(root, padding="20")
        self.frame_principal.pack(fill=tk.BOTH, expand=True)

        # Frame para datos personales
        frame_personal = ttk.LabelFrame(self.frame_principal, text="Datos Personales", padding="10")
        frame_personal.pack(fill=tk.X, pady=5)

        # Grid para organizar elementos
        # Nombre
        ttk.Label(frame_personal, text="Nombre:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.entry_nombre = ttk.Entry(frame_personal)
        self.entry_nombre.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=5)

        # Apellido
        ttk.Label(frame_personal, text="Apellido:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.entry_apellido = ttk.Entry(frame_personal)
        self.entry_apellido.grid(row=1, column=1, sticky=tk.EW, padx=5, pady=5)

        # Edad
        ttk.Label(frame_personal, text="Edad:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.entry_edad = ttk.Entry(frame_personal, width=10)
        self.entry_edad.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

        # Configurar el grid
        frame_personal.columnconfigure(1, weight=1)

        # Botones
        frame_botones = ttk.Frame(self.frame_principal)
        frame_botones.pack(fill=tk.X, pady=20)

        # Botones principales
        ttk.Button(frame_botones, text="Guardar", command=self.guardar).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Limpiar", command=self.limpiar).pack(side=tk.LEFT, padx=5)

    def guardar(self):
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        if nombre and apellido:
            messagebox.showinfo("Éxito", "Datos guardados correctamente")
        else:
            messagebox.showwarning("Error", "Por favor complete los campos obligatorios")

    def limpiar(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_apellido.delete(0, tk.END)
        self.entry_edad.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionPersonal(root)
    root.mainloop()