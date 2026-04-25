import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Ejemplo de Entry")
root.geometry("300x100")
frame = ttk.Frame(root, padding="10")
frame.pack()

# Etiqueta alineada a la izquierda
ttk.Label(frame, text="Nombre:").grid(row=0, column=0,
                                    sticky=tk.W,  # Alineado a la izquierda
                                    pady=5)       # Espacio vertical

# Entry que se estira horizontalmente
ttk.Entry(frame).grid(row=0, column=1,
                     sticky=tk.EW,      # Se estira horizontalmente
                     padx=5, pady=5)    # Espacio en todos lados

# Etiqueta alineada a la izquierda
ttk.Label(frame, text="Email:").grid(row=1, column=0,
                                   sticky=tk.W,
                                   pady=5)

# Entry que se estira horizontalmente
ttk.Entry(frame).grid(row=1, column=1,
                     sticky=tk.EW,
                     padx=5, pady=5)

# Etiqueta alineada a la izquierda
ttk.Label(frame, text="Documento:").grid(row=2, column=0,
                                   sticky=tk.W,
                                   pady=5)

# Entry que se estira horizontalmente
ttk.Entry(frame).grid(row=2, column=1,
                     sticky=tk.EW,
                     padx=5, pady=5)


# Hacer que la segunda columna sea expandible
frame.columnconfigure(1, weight=1)

root.mainloop()