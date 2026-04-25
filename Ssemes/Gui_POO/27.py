import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class EjemploBotones:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejemplos de Botones")
        self.root.geometry("400x500")

        # Frame principal con padding
        self.frame = ttk.Frame(root, padding="20")
        self.frame.pack(fill=tk.BOTH, expand=True)

        # 1. Botón básico
        ttk.Label(self.frame, text="1. Botón básico:").pack(anchor=tk.W, pady=5)
        ttk.Button(self.frame,
                   text="Haz clic",
                   command=self.boton_basico_click).pack(pady=5)

        # 2. Botón que cambia de texto
        ttk.Label(self.frame, text="2. Botón que cambia de texto:").pack(anchor=tk.W, pady=5)
        self.boton_cambiar = ttk.Button(self.frame,
                                        text="Cambiar texto",
                                        command=self.cambiar_texto)
        self.boton_cambiar.pack(pady=5)

        # 3. Botón que se habilita/deshabilita
        ttk.Label(self.frame, text="3. Botón que se habilita/deshabilita:").pack(anchor=tk.W, pady=5)
        self.boton_control = ttk.Button(self.frame,
                                        text="Botón controlado",
                                        state='disabled')
        self.boton_control.pack(pady=5)

        ttk.Button(self.frame,
                   text="Habilitar/Deshabilitar",
                   command=self.toggle_boton).pack(pady=5)

        # 4. Botón que interactúa con un entry
        ttk.Label(self.frame, text="4. Botón que lee entry:").pack(anchor=tk.W, pady=5)
        self.entry = ttk.Entry(self.frame)
        self.entry.pack(pady=5)

        ttk.Button(self.frame,
                   text="Leer Entry",
                   command=self.leer_entry).pack(pady=5)

        # 5. Botón con confirmación
        ttk.Label(self.frame, text="5. Botón con confirmación:").pack(anchor=tk.W, pady=5)
        ttk.Button(self.frame,
                   text="Acción importante",
                   command=self.confirmar_accion).pack(pady=5)

        # 6. Botón con diferentes estilos
        ttk.Label(self.frame, text="6. Botones con diferentes estilos:").pack(anchor=tk.W, pady=5)

        # Botón tk normal (permite más personalización)
        tk.Button(self.frame,
                  text="Botón tk",
                  bg="lightblue",
                  fg="navy",
                  activebackground="blue",
                  activeforeground="white").pack(pady=5)

        # Botón ttk (estilo más moderno)
        ttk.Button(self.frame,
                   text="Botón ttk").pack(pady=5)

    def boton_basico_click(self):
        messagebox.showinfo("Info", "¡Has hecho clic en el botón básico!")

    def cambiar_texto(self):
        texto_actual = self.boton_cambiar['text']
        nuevo_texto = "Texto original" if texto_actual == "Texto cambiado" else "Texto cambiado"
        self.boton_cambiar['text'] = nuevo_texto

    def toggle_boton(self):
        estado_actual = self.boton_control['state']
        nuevo_estado = 'normal' if estado_actual == 'disabled' else 'disabled'
        self.boton_control['state'] = nuevo_estado

    def leer_entry(self):
        texto = self.entry.get()
        if texto:
            messagebox.showinfo("Contenido", f"El entry contiene: {texto}")
        else:
            messagebox.showwarning("Atención", "El entry está vacío")

    def confirmar_accion(self):
        if messagebox.askyesno("Confirmar", "¿Estás seguro de realizar esta acción?"):
            messagebox.showinfo("Éxito", "Acción realizada")
        else:
            messagebox.showinfo("Cancelado", "Acción cancelada")


if __name__ == "__main__":
    root = tk.Tk()
    app = EjemploBotones(root)
    root.mainloop()