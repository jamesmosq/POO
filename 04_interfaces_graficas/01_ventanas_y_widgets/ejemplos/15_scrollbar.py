#13. Scrollbar (Barra de desplazamiento)
from tkinter import Tk
from tkinter import Scrollbar
root = Tk()
root.geometry("400x300")
scroll = Scrollbar(root)
scroll.pack(side="right", fill="y")
root.mainloop()  # Inicia el bucle de eventos de la ventana
