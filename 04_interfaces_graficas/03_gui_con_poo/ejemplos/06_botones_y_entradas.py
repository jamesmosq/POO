import tkinter as tk
from tkinter import messagebox


class EjemploButtonsEntries:
    def __init__(self, root):
        self.root = root
        self.root.title("Tutorial de Buttons y Entries")
        self.root.geometry("400x500")

        # === ENTRIES (CAMPOS DE ENTRADA) ===
        # Entry básico
        tk.Label(root, text="Entry básico:").pack(pady=5)
        self.entry_basico = tk.Entry(root)
        self.entry_basico.pack(pady=5)
        self.entry_basico.insert(0, "Texto por defecto")  # Insertar texto inicial

        # Entry para contraseña
        tk.Label(root, text="Entry para contraseña:").pack(pady=5)
        self.entry_password = tk.Entry(root, show="*")  # Los caracteres se muestran como *
        self.entry_password.pack(pady=5)

        # Entry con placeholder
        tk.Label(root, text="Entry con placeholder:").pack(pady=5)
        self.entry_placeholder = tk.Entry(root)
        self.entry_placeholder.pack(pady=5)
        self.entry_placeholder.insert(0, "Escribe aquí...")
        self.entry_placeholder.bind('<FocusIn>', self.on_entry_click)
        self.entry_placeholder.bind('<FocusOut>', self.on_focus_out)
        self.entry_placeholder.config(fg='grey')

        # Entry con validación
        tk.Label(root, text="Entry solo números:").pack(pady=5)
        vcmd = (root.register(self.validar_numero), '%P')
        self.entry_numerico = tk.Entry(root, validate='key', validatecommand=vcmd)
        self.entry_numerico.pack(pady=5)

        # === BUTTONS (BOTONES) ===
        # Botón básico
        self.boton_basico = tk.Button(root, text="Botón básico",
                                      command=self.accion_boton_basico)
        self.boton_basico.pack(pady=10)

        # Botón con colores
        self.boton_color = tk.Button(root, text="Botón con colores",
                                     bg="lightblue", fg="navy",
                                     activebackground="blue",
                                     activeforeground="white",
                                     command=self.accion_boton_color)
        self.boton_color.pack(pady=10)

        # Botón que lee Entry
        self.boton_leer = tk.Button(root, text="Leer Entry básico",
                                    command=self.leer_entry)
        self.boton_leer.pack(pady=10)

        # Botón que se habilita/deshabilita
        self.boton_toggle = tk.Button(root, text="Botón deshabilitado")
        self.boton_toggle.pack(pady=10)
        self.boton_toggle.config(state='disabled')  # Deshabilitar botón

        # Botón para habilitar/deshabilitar el anterior
        self.boton_control = tk.Button(root, text="Habilitar/Deshabilitar",
                                       command=self.toggle_boton)
        self.boton_control.pack(pady=10)

        # Botón con evento de ratón
        self.boton_evento = tk.Button(root, text="Botón con eventos")
        self.boton_evento.pack(pady=10)
        self.boton_evento.bind('<Enter>', self.on_enter)  # Ratón encima
        self.boton_evento.bind('<Leave>', self.on_leave)  # Ratón fuera

    # === FUNCIONES PARA ENTRIES ===
    def on_entry_click(self, event):
        """Función para gestionar el placeholder"""
        if self.entry_placeholder.get() == "Escribe aquí...":
            self.entry_placeholder.delete(0, tk.END)
            self.entry_placeholder.config(fg='black')

    def on_focus_out(self, event):
        """Función para restaurar el placeholder"""
        if self.entry_placeholder.get() == "":
            self.entry_placeholder.insert(0, "Escribe aquí...")
            self.entry_placeholder.config(fg='grey')

    def validar_numero(self, nuevo_valor):
        """Validar que solo se introduzcan números"""
        if nuevo_valor == "":
            return True
        try:
            float(nuevo_valor)
            return True
        except ValueError:
            return False

    # === FUNCIONES PARA BOTONES ===
    def accion_boton_basico(self):
        """Acción del botón básico"""
        messagebox.showinfo("Info", "¡Has pulsado el botón básico!")

    def accion_boton_color(self):
        """Acción del botón con colores"""
        messagebox.showinfo("Info", "¡Has pulsado el botón de colores!")

    def leer_entry(self):
        """Leer el contenido del entry básico"""
        texto = self.entry_basico.get()
        messagebox.showinfo("Contenido", f"El entry contiene: {texto}")

    def toggle_boton(self):
        """Habilitar/deshabilitar botón"""
        estado_actual = self.boton_toggle['state']
        nuevo_estado = 'normal' if estado_actual == 'disabled' else 'disabled'
        self.boton_toggle.config(state=nuevo_estado)

    def on_enter(self, e):
        """Cuando el ratón está sobre el botón"""
        self.boton_evento.config(bg='lightgreen')

    def on_leave(self, e):
        """Cuando el ratón sale del botón"""
        self.boton_evento.config(bg='SystemButtonFace')


if __name__ == "__main__":
    root = tk.Tk()
    app = EjemploButtonsEntries(root)
    root.mainloop()