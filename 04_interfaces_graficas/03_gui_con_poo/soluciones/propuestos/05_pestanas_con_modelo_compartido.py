"""
Solución - Ejercicio propuesto 05 - Pestañas con modelo compartido
"""

import tkinter as tk
from tkinter import ttk


class ModeloTareas:
    def __init__(self):
        self.tareas = []
        self._suscriptores = []

    def suscribir(self, funcion):
        self._suscriptores.append(funcion)

    def agregar(self, tarea):
        self.tareas.append(tarea)
        for funcion in self._suscriptores:
            funcion()


class PestanaAgregar(tk.Frame):
    def __init__(self, master, modelo):
        super().__init__(master, padx=10, pady=10)
        self.modelo = modelo
        self.entrada = tk.Entry(self, width=30)
        self.entrada.pack()
        self.boton = tk.Button(self, text="Agregar", command=self.agregar)
        self.boton.pack(pady=5)

    def agregar(self):
        tarea = self.entrada.get().strip()
        if tarea:
            self.modelo.agregar(tarea)
        self.entrada.delete(0, tk.END)


class PestanaResumen(tk.Frame):
    def __init__(self, master, modelo):
        super().__init__(master, padx=10, pady=10)
        self.modelo = modelo
        self.contador = tk.Label(self, text="")
        self.contador.pack()
        self.lista = tk.Listbox(self, height=8)
        self.lista.pack(fill="both", expand=True)
        modelo.suscribir(self.refrescar)  # la función, sin paréntesis
        self.refrescar()

    def refrescar(self):
        self.lista.delete(0, tk.END)
        for tarea in self.modelo.tareas:
            self.lista.insert(tk.END, tarea)
        self.contador.config(text=f"{len(self.modelo.tareas)} tareas")


class Aplicacion(ttk.Notebook):
    def __init__(self, master, modelo):
        super().__init__(master)
        self.pestana_agregar = PestanaAgregar(self, modelo)
        self.pestana_resumen = PestanaResumen(self, modelo)
        self.add(self.pestana_agregar, text="Agregar")
        self.add(self.pestana_resumen, text="Resumen")


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    avisos = []
    m = ModeloTareas()
    m.suscribir(lambda: avisos.append(len(m.tareas)))
    m.agregar("a")
    m.agregar("b")
    assert avisos == [1, 2], "El modelo debe avisar a los suscritos en cada cambio"

    raiz = tk.Tk()
    raiz.withdraw()
    modelo = ModeloTareas()
    app = Aplicacion(raiz, modelo)
    assert [app.tab(t, "text") for t in app.tabs()] == ["Agregar", "Resumen"]
    assert app.pestana_resumen.contador.cget("text") == "0 tareas"

    for tarea in ("Leer", "Programar"):
        app.pestana_agregar.entrada.insert(0, tarea)
        app.pestana_agregar.boton.invoke()

    resumen = app.pestana_resumen
    assert resumen.contador.cget("text") == "2 tareas"
    assert resumen.lista.get(0, tk.END) == ("Leer", "Programar"), "La lista no debe repetir tareas"
    assert app.pestana_agregar.entrada.get() == ""
    assert modelo.tareas == ["Leer", "Programar"]
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        Aplicacion(raiz, ModeloTareas()).pack(fill="both", expand=True)
        raiz.mainloop()
