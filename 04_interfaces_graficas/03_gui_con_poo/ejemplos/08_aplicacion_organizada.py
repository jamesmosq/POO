import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class AplicacionOrganizada:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario Organizado")
        self.root.geometry("500x600")

        # Frame principal con padding
        self.frame_principal = ttk.Frame(root, padding="20")
        self.frame_principal.pack(fill=tk.BOTH, expand=True)

        # === SECCIÓN DE DATOS PERSONALES ===
        self.crear_seccion_personal()

        # Separador
        ttk.Separator(self.frame_principal, orient='horizontal').pack(fill=tk.X, pady=20)

        # === SECCIÓN DE CONTACTO ===
        self.crear_seccion_contacto()

        # Separador
        ttk.Separator(self.frame_principal, orient='horizontal').pack(fill=tk.X, pady=20)

        # === SECCIÓN DE BOTONES ===
        self.crear_seccion_botones()

    def crear_seccion_personal(self):
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

    def crear_seccion_contacto(self):
        # Frame para datos de contacto
        frame_contacto = ttk.LabelFrame(self.frame_principal, text="Datos de Contacto", padding="10")
        frame_contacto.pack(fill=tk.X, pady=5)

        # Email
        ttk.Label(frame_contacto, text="Email:").pack(anchor=tk.W)
        self.entry_email = ttk.Entry(frame_contacto)
        self.entry_email.pack(fill=tk.X, pady=5)

        # Teléfono - usando un frame interno para layout horizontal
        frame_telefono = ttk.Frame(frame_contacto)
        frame_telefono.pack(fill=tk.X, pady=5)

        ttk.Label(frame_telefono, text="Teléfono:").pack(side=tk.LEFT)
        self.entry_telefono = ttk.Entry(frame_telefono)
        self.entry_telefono.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)

        # Dirección
        ttk.Label(frame_contacto, text="Dirección:").pack(anchor=tk.W)
        self.text_direccion = tk.Text(frame_contacto, height=3)
        self.text_direccion.pack(fill=tk.X, pady=5)

    def crear_seccion_botones(self):
        # Frame para botones
        frame_botones = ttk.Frame(self.frame_principal)
        frame_botones.pack(fill=tk.X, pady=20)

        # Botones principales
        ttk.Button(frame_botones, text="Guardar", command=self.guardar).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Limpiar", command=self.limpiar).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Salir", command=self.root.quit).pack(side=tk.RIGHT, padx=5)

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
        self.entry_email.delete(0, tk.END)
        self.entry_telefono.delete(0, tk.END)
        self.text_direccion.delete('1.0', tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionOrganizada(root)
    root.mainloop()