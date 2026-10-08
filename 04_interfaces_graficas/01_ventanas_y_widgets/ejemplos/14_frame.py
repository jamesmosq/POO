#12. Frame (Marco)
from tkinter import Tk
from tkinter import Frame
root = Tk()
root.geometry("400x300")
frame = Frame(root)
frame.pack()
root.mainloop()  # Inicia el bucle de eventos de la ventana
