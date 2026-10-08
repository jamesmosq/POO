from tkinter import Tk
root = Tk()  # Creas la ventana principal
root.geometry('600x400')
#root.attributes('-alpha',0.99)
root.configure(bg='#CD5C5C') # se recomienda cargar configuraciiones basicas al inicio
root.title('Mi primera ventana') # title
root.resizable(False,False)

# Otras opciones de la ventana. Deben ir ANTES de mainloop(): lo que se escribe
# después solo se ejecuta cuando la ventana ya se cerró.
root.attributes('-topmost',True)  # Coloca la ventana en primer plano
# root.state('zoomed')            # Maximiza la ventana (Windows)
# root.attributes('-zoomed',True) # Maximiza la ventana (Linux)
# root.iconify()                  # Minimiza la ventana

root.mainloop()  # Inicia el bucle de eventos de la ventana. Siempre al final.


#1. Ventana principal (Tk)
