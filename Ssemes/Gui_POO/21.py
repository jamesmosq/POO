import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, colorchooser, filedialog
from tkinter import scrolledtext


class DemoWidgets:
    def __init__(self, root):
        self.root = root
        self.root.title("Demostración de Widgets Tkinter")
        self.root.geometry("800x600")

        # Crear notebook para organizar los widgets en pestañas
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)

        # === PESTAÑA 1: WIDGETS BÁSICOS ===
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text='Widgets Básicos')

        # Labels (Etiquetas)
        tk.Label(self.tab1, text="Label normal").pack(pady=5)
        tk.Label(self.tab1, text="Label con color", fg="red", bg="yellow").pack(pady=5)
        tk.Label(self.tab1, text="Label con fuente", font=("Arial", 14, "bold")).pack(pady=5)

        # Entry (Campos de texto)
        self.entry_normal = tk.Entry(self.tab1)
        self.entry_normal.pack(pady=5)
        self.entry_normal.insert(0, "Entry normal")

        self.entry_pass = tk.Entry(self.tab1, show="*")  # Para contraseñas
        self.entry_pass.pack(pady=5)
        self.entry_pass.insert(0, "contraseña")

        # Buttons (Botones)
        tk.Button(self.tab1, text="Botón normal", command=self.mostrar_mensaje).pack(pady=5)
        ttk.Button(self.tab1, text="Botón ttk").pack(pady=5)  # Estilo más moderno

        # === PESTAÑA 2: SELECCIÓN ===
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text='Widgets de Selección')

        # Checkbuttons
        self.var_check = tk.BooleanVar()
        tk.Checkbutton(self.tab2, text="Checkbox normal", variable=self.var_check).pack(pady=5)
        ttk.Checkbutton(self.tab2, text="Checkbox ttk").pack(pady=5)

        # Radiobuttons
        self.var_radio = tk.StringVar(value="1")
        tk.Radiobutton(self.tab2, text="Opción 1", variable=self.var_radio, value="1").pack(pady=5)
        tk.Radiobutton(self.tab2, text="Opción 2", variable=self.var_radio, value="2").pack(pady=5)

        # Combobox
        self.combo = ttk.Combobox(self.tab2, values=["Opción 1", "Opción 2", "Opción 3"])
        self.combo.pack(pady=5)
        self.combo.set("Selecciona una opción")

        # Listbox
        self.listbox = tk.Listbox(self.tab2, height=4)
        for item in ["Item 1", "Item 2", "Item 3", "Item 4"]:
            self.listbox.insert(tk.END, item)
        self.listbox.pack(pady=5)

        # === PESTAÑA 3: CONTENEDORES ===
        self.tab3 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab3, text='Contenedores')

        # Frame
        frame = tk.Frame(self.tab3, bd=2, relief=tk.SUNKEN)
        frame.pack(pady=10, padx=10, fill=tk.X)
        tk.Label(frame, text="Frame con borde").pack(pady=5)

        # LabelFrame
        label_frame = tk.LabelFrame(self.tab3, text="Grupo de opciones")
        label_frame.pack(pady=10, padx=10, fill=tk.X)
        tk.Button(label_frame, text="Botón 1").pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(label_frame, text="Botón 2").pack(side=tk.LEFT, padx=5, pady=5)

        # === PESTAÑA 4: WIDGETS AVANZADOS ===
        self.tab4 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab4, text='Widgets Avanzados')

        # Text (editor de texto multilinea)
        self.text = tk.Text(self.tab4, height=4, width=30)
        self.text.pack(pady=5)
        self.text.insert(tk.END, "Widget Text para\ntexto multilínea")

        # Scrolled Text
        self.scrolled_text = scrolledtext.ScrolledText(self.tab4, height=4, width=30)
        self.scrolled_text.pack(pady=5)
        self.scrolled_text.insert(tk.END, "ScrolledText con barras de desplazamiento")

        # Scale (deslizador)
        self.scale = tk.Scale(self.tab4, from_=0, to=100, orient=tk.HORIZONTAL)
        self.scale.pack(pady=5)

        # Progressbar
        self.progress = ttk.Progressbar(self.tab4, length=200, mode='determinate')
        self.progress.pack(pady=5)
        self.progress['value'] = 70

        # Spinbox
        self.spinbox = tk.Spinbox(self.tab4, from_=0, to=10)
        self.spinbox.pack(pady=5)

        # Botones para diálogos
        tk.Button(self.tab4, text="Abrir archivo", command=self.abrir_archivo).pack(pady=5)
        tk.Button(self.tab4, text="Selector de color", command=self.elegir_color).pack(pady=5)

    def mostrar_mensaje(self):
        messagebox.showinfo("Mensaje", "¡Hola! Este es un mensaje de ejemplo")

    def abrir_archivo(self):
        filedialog.askopenfilename()

    def elegir_color(self):
        colorchooser.askcolor(title="Selecciona un color")


if __name__ == "__main__":
    root = tk.Tk()
    app = DemoWidgets(root)
    root.mainloop()