"""
Solución - Ejercicio para corregir 04 - Lista de tareas

CORRECCIÓN 1 (el Entry no quedaba vacío): delete(0) borra solo el primer
carácter. Para borrar todo se indica el rango completo: delete(0, tk.END).

CORRECCIÓN 2 (IndexError: tuple index out of range): sin selección,
curselection() retorna una tupla vacía y [0] falla. Hay que revisar antes.

CORRECCIÓN 3 (el contador no se actualizaba al eliminar): después de cada
cambio en la lista hay que actualizar la vista.
"""

import tkinter as tk


class ListaDeTareas:
    def __init__(self, raiz):
        self.entrada = tk.Entry(raiz)
        self.entrada.pack()
        tk.Button(raiz, text="Agregar", command=self.agregar).pack()
        self.lista = tk.Listbox(raiz)
        self.lista.pack()
        tk.Button(raiz, text="Eliminar", command=self.eliminar).pack()
        self.contador = tk.Label(raiz, text="0 tareas")
        self.contador.pack()

    def actualizar_contador(self):
        self.contador.config(text=f"{self.lista.size()} tareas")

    def agregar(self):
        texto = self.entrada.get().strip()
        if texto:
            self.lista.insert(tk.END, texto)
            self.entrada.delete(0, tk.END)  # CORRECCIÓN 1
            self.actualizar_contador()

    def eliminar(self):
        seleccion = self.lista.curselection()
        if not seleccion:  # CORRECCIÓN 2
            return
        self.lista.delete(seleccion[0])
        self.actualizar_contador()  # CORRECCIÓN 3


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    app = ListaDeTareas(raiz)

    app.entrada.insert(0, "Estudiar")
    app.agregar()
    assert app.entrada.get() == "", f"El Entry quedó con {app.entrada.get()!r}"
    app.entrada.insert(0, "Programar")
    app.agregar()

    app.eliminar()
    assert app.lista.size() == 2, "Sin selección no se debe eliminar nada"

    app.lista.selection_set(0)
    app.eliminar()
    assert app.lista.get(0, tk.END) == ("Programar",)
    assert app.contador.cget("text") == "1 tareas", f"El contador dice {app.contador.cget('text')!r}"
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        ListaDeTareas(raiz)
        raiz.mainloop()
