"""
Solución - Ejercicio para corregir 05 - Observador roto

CORRECCIÓN 1: suscribir(self.refrescar()) ejecutaba refrescar en ese
momento y suscribía su resultado (None). Se debe suscribir la función, sin
paréntesis, para que el modelo la llame después.

CORRECCIÓN 2: agregar() modificaba la lista pero nunca avisaba a los
suscriptores. Después de cada cambio hay que llamar a _notificar().

CORRECCIÓN 3 (tareas repetidas): refrescar() agregaba todas las tareas
sobre las que ya estaban en la lista. Al redibujar, primero se borra lo
anterior.
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
        self._notificar()  # CORRECCIÓN 2


class Resumen(tk.Frame):
    def __init__(self, master, modelo):
        super().__init__(master)
        self.modelo = modelo
        self.lista = tk.Listbox(self)
        self.lista.pack()
        modelo.suscribir(self.refrescar)  # CORRECCIÓN 1

    def refrescar(self):
        self.lista.delete(0, tk.END)  # CORRECCIÓN 3
        for tarea in self.modelo.tareas:
            self.lista.insert(tk.END, tarea)


# ----------------------------------------------------------------------
# Pruebas
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
