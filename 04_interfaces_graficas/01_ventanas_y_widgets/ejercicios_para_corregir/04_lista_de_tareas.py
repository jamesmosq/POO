"""
Ejercicio para corregir 04 - Lista de tareas
Nivel: intermedio
Errores a encontrar: 3

Qué debería hacer el programa:
    - agregar(): pasa el texto del Entry al Listbox y deja el Entry vacío.
    - eliminar(): borra la tarea seleccionada; si no hay selección, no hace
      nada.
    - La etiqueta contador siempre muestra "N tareas".

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
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
            self.entrada.delete(0)
            self.actualizar_contador()

    def eliminar(self):
        indice = self.lista.curselection()[0]
        self.lista.delete(indice)


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
