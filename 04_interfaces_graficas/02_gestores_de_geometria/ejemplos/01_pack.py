import tkinter as tk

root = tk.Tk()
root.title("Ejemplo con pack()")
root.geometry('400x300')

# Crear tres etiquetas y distribuirlas en la ventana
label1 = tk.Label(root, text="Etiqueta 1", bg="red")
label2 = tk.Label(root, text="Etiqueta 2", bg="green")
label3 = tk.Label(root, text="Etiqueta 3", bg="blue")

# Empaquetar las etiquetas para que ocupen todo el ancho y altura
label1.pack(expand=True, fill="both")  # Ocupará todo el ancho y alto disponible
label2.pack(expand=True, fill="both")
label3.pack(expand=True, fill="both")

root.mainloop()
