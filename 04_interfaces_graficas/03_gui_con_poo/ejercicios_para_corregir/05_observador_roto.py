"""
Ejercicio para corregir 05 - Observador roto
Nivel: avanzado
Errores a encontrar: 3

Qué debería hacer el programa:
    El modelo guarda tareas y avisa a sus suscriptores cada vez que cambia.
    El Resumen se suscribe y, al recibir el aviso, redibuja su lista.

        modelo.agregar("Leer"); modelo.agregar("Programar")
        resumen.lista -> ("Leer", "Programar")   (sin repetidos)

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""
import tkinter as tk


class ModeloTareas:
    def __init__(self):
        self.tareas = []
        self._suscriptores = []

    def suscribir(self, funcion):
        self._suscriptores.append(funcion)

    def _notificar(self):
        for funcion in self._suscriptores:
            funcion()

    def agregar(self, tarea):
        self.tareas.append(tarea)


class Resumen(tk.Frame):
    def __init__(self, master, modelo):
        super().__init__(master)
        self.modelo = modelo
        self.lista = tk.Listbox(self)
        self.lista.pack()
        modelo.suscribir(self.refrescar())

    def refrescar(self):
        for tarea in self.modelo.tareas:
            self.lista.insert(tk.END, tarea)


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    modelo = ModeloTareas()
    resumen = Resumen(raiz, modelo)

    modelo.agregar("Leer")
    assert resumen.lista.get(0, tk.END) == ("Leer",), f"La lista muestra {resumen.lista.get(0, tk.END)}"
    modelo.agregar("Programar")
    assert resumen.lista.get(0, tk.END) == ("Leer", "Programar"), f"La lista muestra {resumen.lista.get(0, tk.END)}"
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        modelo = ModeloTareas()
        Resumen(raiz, modelo).pack()
        modelo.agregar("Ejemplo")
        raiz.mainloop()
