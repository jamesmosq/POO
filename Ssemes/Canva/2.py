import tkinter as tk

root = tk.Tk()
root.title("Ejemplo con grid()")
root.geometry('400x300')
# Crear tres etiquetas y distribuirlas en una cuadrícula
label1 = tk.Label(root, text="Etiqueta 1", bg="red")
label2 = tk.Label(root, text="Etiqueta 2", bg="green")
label3 = tk.Label(root, text="Etiqueta 3", bg="blue")

# Colocar los widgets en la cuadrícula (fila, columna)
label1.grid(row=0, column=0, sticky="nsew")
label2.grid(row=0, column=1, sticky="nsew")
label3.grid(row=1, column=0, columnspan=2, sticky="nsew")

# Hacer que las filas y columnas se expandan
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

root.mainloop()
