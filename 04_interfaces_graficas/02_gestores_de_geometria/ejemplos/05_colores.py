import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Colores en Tkinter")
root.geometry("400x300")
root.configure(bg='#E6E6FA')  # Lavanda claro

# Crear y colocar widgets
label = tk.Label(root, text="Bienvenido", bg='#FA8072', fg='#000080', font=('Arial', 16))  # Oro y azul marino
label.pack(pady=10)

entry = tk.Entry(root, bg='#F0FFF0', fg='#2F4F4F', insertbackground='#FF69B4')  # Miel rocío, gris pizarra oscuro, rosa intenso
entry.pack(pady=10)

button = tk.Button(root, text="Presionar", bg='#20B2AA', fg='white',
                   activebackground='#48D1CC', activeforeground='#191970')  # Verde mar claro, blanco, turquesa medio, azul medianoche
button.pack(pady=10)

frame = tk.Frame(root, bg='#BF00BF', width=200, height=100)  # Ciruela
frame.pack(pady=10)

label_in_frame = tk.Label(frame, text="Dentro del frame", bg='#DDA0DD', fg='#4B0082')  # Ciruela, índigo
label_in_frame.place(relx=0.5, rely=0.5, anchor='center')

root.mainloop()