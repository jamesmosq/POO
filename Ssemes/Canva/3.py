import tkinter as tk

root = tk.Tk()
root.title("Ejemplo con place()")
root.geometry('400x300')
# Crear tres etiquetas y posicionarlas usando coordenadas relativas
label1 = tk.Label(root, text="Etiqueta 1", bg="red")
label2 = tk.Label(root, text="Etiqueta 2", bg="green")
label3 = tk.Label(root, text="Etiqueta 3", bg="blue")

# Colocar los widgets con coordenadas relativas
label1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.2)
label2.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.2)
label3.place(relx=0.1, rely=0.7, relwidth=0.8, relheight=0.2)

root.mainloop()
