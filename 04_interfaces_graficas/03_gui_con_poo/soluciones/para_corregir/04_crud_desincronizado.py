"""
Solución - Ejercicio para corregir 04 - CRUD desincronizado

CORRECCIÓN 1 (el nombre salía partido en columnas): values espera una
tupla con un valor por columna. Si recibe un texto, Tcl lo separa por los
espacios: "Ana Pérez 300..." se convierte en tres valores.

CORRECCIÓN 2 (seleccionado() retornaba una tupla): selection() siempre
retorna una tupla de ids, aunque haya uno solo. El id es el elemento [0].

CORRECCIÓN 3 (la tabla y el diccionario dejaban de coincidir): eliminar()
borraba la fila de la tabla pero no del diccionario. Cada cambio debe
hacerse en los dos lugares.
"""

import tkinter as tk
from tkinter import ttk


class Contactos(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.tabla = ttk.Treeview(self, columns=("nombre", "telefono"), show="headings")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("telefono", text="Teléfono")
        self.tabla.pack(fill="both", expand=True)
        self.contactos = {}

    def agregar(self, nombre, telefono):
        fila = self.tabla.insert("", tk.END, values=(nombre, telefono))  # CORRECCIÓN 1
        self.contactos[fila] = {"nombre": nombre, "telefono": telefono}
        return fila

    def seleccionado(self):
        seleccion = self.tabla.selection()
        return seleccion[0] if seleccion else None  # CORRECCIÓN 2

    def eliminar(self):
        fila = self.seleccionado()
        if fila is not None:
            self.tabla.delete(fila)
            del self.contactos[fila]  # CORRECCIÓN 3


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    app = Contactos(raiz)
    ana = app.agregar("Ana Pérez", "3001112233")
    app.agregar("Luis", "3104445566")

    assert tuple(app.tabla.item(ana, "values")) == ("Ana Pérez", "3001112233"), app.tabla.item(ana, "values")

    app.tabla.selection_set(ana)
    assert app.seleccionado() == ana, f"seleccionado() retornó {app.seleccionado()!r}"

    app.eliminar()
    assert len(app.tabla.get_children()) == 1
    assert ana not in app.contactos, "El contacto se borró de la tabla pero no del diccionario"
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        app = Contactos(raiz)
        app.pack(fill="both", expand=True)
        app.agregar("Ana Pérez", "3001112233")
        raiz.mainloop()
