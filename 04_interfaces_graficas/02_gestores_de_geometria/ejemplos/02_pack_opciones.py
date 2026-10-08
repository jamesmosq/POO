import tkinter as tk

root = tk.Tk()
root.title("Ejemplo de pack()")
root.geometry("300x200")

# Crear widgets
label1 = tk.Label(root, text="Etiqueta 1", bg="red")
label2 = tk.Label(root, text="Etiqueta 2", bg="green")
label3 = tk.Label(root, text="Etiqueta 3", bg="blue")
button = tk.Button(root, text="Botón")

# Posicionar widgets con pack()
label1.pack(side="top", fill="x", padx=5, pady=5)
label2.pack(side="left", fill="y", padx=5, pady=5)
label3.pack(side="right", fill="y", padx=5, pady=5)
button.pack(side="bottom", fill="x", padx=5, pady=5)

root.mainloop()