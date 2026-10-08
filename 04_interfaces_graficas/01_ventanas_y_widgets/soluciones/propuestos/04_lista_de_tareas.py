"""
Solución - Ejercicio propuesto 04 - Lista de tareas
"""

import tkinter as tk


class ListaDeTareas:
    def __init__(self, raiz):
        raiz.title("Tareas")
        self.entrada = tk.Entry(raiz, width=30)
        self.entrada.pack(padx=10, pady=5)
        self.boton_agregar = tk.Button(raiz, text="Agregar", command=self.agregar)
        self.boton_agregar.pack()

        marco = tk.Frame(raiz)
        marco.pack(padx=10, pady=5, fill="both", expand=True)
        barra = tk.Scrollbar(marco, orient="vertical")
        self.lista = tk.Listbox(marco, height=8, yscrollcommand=barra.set)
        barra.config(command=self.lista.yview)
        self.lista.pack(side="left", fill="both", expand=True)
        barra.pack(side="right", fill="y")

        self.boton_eliminar = tk.Button(raiz, text="Eliminar", command=self.eliminar)
        self.boton_eliminar.pack()
        self.contador = tk.Label(raiz, text="")
        self.contador.pack(pady=5)
        self.actualizar_contador()

    def actualizar_contador(self):
        self.contador.config(text=f"{self.lista.size()} tareas")

    def agregar(self):
        texto = self.entrada.get().strip()
        if texto and texto not in self.lista.get(0, tk.END):
            self.lista.insert(tk.END, texto)
            self.actualizar_contador()
        self.entrada.delete(0, tk.END)

    def eliminar(self):
        seleccion = self.lista.curselection()
        if not seleccion:
            return
        self.lista.delete(seleccion[0])
        self.actualizar_contador()


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    app = ListaDeTareas(raiz)
    assert app.contador.cget("text") == "0 tareas"

    for tarea in ("Estudiar", "", "Programar", "Estudiar", "Descansar"):
        app.entrada.insert(0, tarea)
        app.boton_agregar.invoke()
        assert app.entrada.get() == "", "El Entry debe quedar vacío después de agregar"
    assert app.lista.get(0, tk.END) == ("Estudiar", "Programar", "Descansar")
    assert app.contador.cget("text") == "3 tareas"

    app.boton_eliminar.invoke()
    assert app.lista.size() == 3, "Sin selección no se elimina nada"

    app.lista.selection_set(1)
    app.boton_eliminar.invoke()
    assert app.lista.get(0, tk.END) == ("Estudiar", "Descansar")
    assert app.contador.cget("text") == "2 tareas"

    assert app.lista.cget("yscrollcommand"), "Conecta una Scrollbar al Listbox"
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        ListaDeTareas(raiz)
        raiz.mainloop()
