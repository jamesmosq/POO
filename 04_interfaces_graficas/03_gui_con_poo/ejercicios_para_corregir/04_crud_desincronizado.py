"""
Ejercicio para corregir 04 - CRUD desincronizado
Nivel: intermedio
Errores a encontrar: 3

Qué debería hacer el programa:
    Una tabla de contactos (Treeview) con columnas nombre y teléfono. El
    diccionario self.contactos (id de fila -> datos) siempre debe coincidir
    con lo que muestra la tabla.

    - agregar(nombre, telefono): inserta en la tabla y en el diccionario.
    - seleccionado(): retorna el id de la fila seleccionada, o None.
    - eliminar(): borra la fila seleccionada de la tabla y del diccionario.

Pista: si un nombre con espacios aparece "partido" en dos columnas, revisa
qué tipo de dato espera el parámetro values de Treeview.insert.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
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
        fila = self.tabla.insert("", tk.END, values=f"{nombre} {telefono}")
        self.contactos[fila] = {"nombre": nombre, "telefono": telefono}
        return fila

    def seleccionado(self):
        seleccion = self.tabla.selection()
        return seleccion if seleccion else None

    def eliminar(self):
        fila = self.seleccionado()
        if fila is not None:
            self.tabla.delete(fila)


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
