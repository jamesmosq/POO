"""
Ejercicio propuesto 04 - CRUD con Treeview
Nivel: avanzado

CRUD: Crear, Leer (Read), Actualizar (Update) y Eliminar (Delete). Aquí
los datos se guardan en memoria; en el tema 05 se guardarán en MySQL.

Requisitos. Crea la clase GestorContactos(tk.Frame):
1. self.nombre y self.telefono: Entry.
2. Botones self.boton_agregar, self.boton_actualizar, self.boton_eliminar.
3. self.tabla: ttk.Treeview con columnas ("nombre", "telefono").
4. self.contactos: diccionario id_de_fila -> {"nombre": ..., "telefono": ...}.
   El id de fila es el que retorna self.tabla.insert(...).
5. agregar(): valida que no haya campos vacíos, inserta en la tabla y en
   self.contactos, y limpia los Entry.
6. al_seleccionar(): carga en los Entry los datos de la fila seleccionada.
   Conéctalo al evento "<<TreeviewSelect>>" de la tabla.
7. actualizar(): modifica la fila seleccionada (tabla y diccionario) con
   lo que hay en los Entry.
8. eliminar(): borra la fila seleccionada de la tabla y del diccionario.
9. Si no hay fila seleccionada, actualizar y eliminar no hacen nada.

La vista (tabla) y los datos (diccionario) siempre deben coincidir.

Conceptos: CRUD, Treeview, eventos virtuales, mantener datos y vista
sincronizados.
"""
import tkinter as tk
from tkinter import ttk

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
