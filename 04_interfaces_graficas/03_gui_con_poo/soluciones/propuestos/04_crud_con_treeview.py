"""
Solución - Ejercicio propuesto 04 - CRUD con Treeview
"""

import tkinter as tk
from tkinter import ttk


class GestorContactos(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.contactos = {}

        formulario = tk.Frame(self)
        formulario.pack(fill="x")
        tk.Label(formulario, text="Nombre").grid(row=0, column=0)
        self.nombre = tk.Entry(formulario)
        self.nombre.grid(row=0, column=1)
        tk.Label(formulario, text="Teléfono").grid(row=1, column=0)
        self.telefono = tk.Entry(formulario)
        self.telefono.grid(row=1, column=1)

        botones = tk.Frame(self)
        botones.pack(pady=5)
        self.boton_agregar = tk.Button(botones, text="Agregar", command=self.agregar)
        self.boton_actualizar = tk.Button(botones, text="Actualizar", command=self.actualizar)
        self.boton_eliminar = tk.Button(botones, text="Eliminar", command=self.eliminar)
        for boton in (self.boton_agregar, self.boton_actualizar, self.boton_eliminar):
            boton.pack(side="left", padx=2)

        self.tabla = ttk.Treeview(self, columns=("nombre", "telefono"), show="headings", height=8)
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("telefono", text="Teléfono")
        self.tabla.pack(fill="both", expand=True)
        self.tabla.bind("<<TreeviewSelect>>", lambda evento: self.al_seleccionar())

    def _leer_formulario(self):
        nombre = self.nombre.get().strip()
        telefono = self.telefono.get().strip()
        if not nombre or not telefono:
            return None
        return {"nombre": nombre, "telefono": telefono}

    def _limpiar(self):
        self.nombre.delete(0, tk.END)
        self.telefono.delete(0, tk.END)

    def _seleccionado(self):
        seleccion = self.tabla.selection()
        return seleccion[0] if seleccion else None

    def agregar(self):
        datos = self._leer_formulario()
        if datos is None:
            return
        fila = self.tabla.insert("", tk.END, values=(datos["nombre"], datos["telefono"]))
        self.contactos[fila] = datos
        self._limpiar()

    def al_seleccionar(self):
        fila = self._seleccionado()
        if fila is None:
            return
        datos = self.contactos[fila]
        self._limpiar()
        self.nombre.insert(0, datos["nombre"])
        self.telefono.insert(0, datos["telefono"])

    def actualizar(self):
        fila = self._seleccionado()
        datos = self._leer_formulario()
        if fila is None or datos is None:
            return
        self.tabla.item(fila, values=(datos["nombre"], datos["telefono"]))
        self.contactos[fila] = datos

    def eliminar(self):
        fila = self._seleccionado()
        if fila is None:
            return
        self.tabla.delete(fila)
        del self.contactos[fila]
        self._limpiar()


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    app = GestorContactos(raiz)

    def escribir(nombre, telefono):
        for entrada, valor in ((app.nombre, nombre), (app.telefono, telefono)):
            entrada.delete(0, tk.END)
            entrada.insert(0, valor)

    def filas():
        return [tuple(app.tabla.item(i, "values")) for i in app.tabla.get_children()]

    escribir("Ana Pérez", "3001112233")
    app.boton_agregar.invoke()
    escribir("Luis", "3104445566")
    app.boton_agregar.invoke()
    escribir("", "123")
    app.boton_agregar.invoke()
    assert filas() == [("Ana Pérez", "3001112233"), ("Luis", "3104445566")], filas()
    assert len(app.contactos) == 2

    app.boton_eliminar.invoke()
    assert len(filas()) == 2, "Sin selección no se elimina nada"

    primera = app.tabla.get_children()[0]
    app.tabla.selection_set(primera)
    app.al_seleccionar()
    assert app.nombre.get() == "Ana Pérez" and app.telefono.get() == "3001112233"

    app.telefono.delete(0, tk.END)
    app.telefono.insert(0, "3009998877")
    app.boton_actualizar.invoke()
    assert filas()[0] == ("Ana Pérez", "3009998877")
    assert app.contactos[primera] == {"nombre": "Ana Pérez", "telefono": "3009998877"}

    app.tabla.selection_set(primera)
    app.boton_eliminar.invoke()
    assert filas() == [("Luis", "3104445566")]
    assert primera not in app.contactos
    assert app.tabla.bind("<<TreeviewSelect>>"), "Conecta al_seleccionar al evento <<TreeviewSelect>>"
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        GestorContactos(raiz).pack(padx=10, pady=10)
        raiz.mainloop()
