#10. Cuadro de mensajes (Messagebox)
from tkinter import Tk
from tkinter import messagebox
root = Tk()
messagebox.showinfo("Título", "Mensaje de información")
root.mainloop()  # Inicia el bucle de eventos de la ventana
