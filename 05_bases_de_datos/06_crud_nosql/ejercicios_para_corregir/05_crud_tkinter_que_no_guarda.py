"""
Ejercicio para corregir 05 - CRUD con Tkinter que no guarda
Nivel: avanzado
Errores a encontrar: 3

Qué debería hacer el programa:
    GestorProductos agrega, actualiza y elimina productos en la COLECCIÓN
    de MongoDB. La tabla de la interfaz siempre refleja lo que hay en la
    base. Cada fila del Treeview usa str(_id) como iid.

Ojo: la interfaz puede "verse bien" aunque la base no haya cambiado.
Las pruebas revisan la colección directamente.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""
import os
import tkinter as tk
from tkinter import ttk

from bson import ObjectId
from pymongo import ASCENDING, MongoClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "curso_poo")


class GestorProductos(tk.Frame):
    def __init__(self, master, coleccion):
        super().__init__(master)
        self.coleccion = coleccion
        self.nombre = tk.Entry(self)
        self.nombre.pack()
        self.precio = tk.Entry(self)
        self.precio.pack()
        self.tabla = ttk.Treeview(self, columns=("nombre", "precio"), show="headings")
        self.tabla.pack()
        self.cargar()

    def cargar(self):
        self.tabla.delete(*self.tabla.get_children())
        for doc in self.coleccion.find().sort("nombre", ASCENDING):
            self.tabla.insert("", tk.END, iid=str(doc["_id"]), values=(doc["nombre"], doc.get("precio", "")))

    def agregar(self):
        self.coleccion.insert_one({"nombre": self.nombre.get(), "precio": float(self.precio.get())})

    def actualizar(self):
        seleccion = self.tabla.selection()
        if seleccion:
            self.coleccion.update_one({"_id": ObjectId(seleccion)},
                                      {"$set": {"nombre": self.nombre.get(),
                                                "precio": float(self.precio.get())}})
            self.cargar()

    def eliminar(self):
        seleccion = self.tabla.selection()
        if seleccion:
            self.tabla.delete(seleccion[0])


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
def de_prueba(nombres):
    """Deja solo los nombres creados por las pruebas (la colección puede tener otros)."""
    return [n for n in nombres if n.startswith("PRUEBA_EJ_")]


if __name__ == "__main__":
    cliente = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
    coleccion = cliente[MONGO_DB]["ej_productos"]
    coleccion.delete_many({"nombre": {"$regex": "^PRUEBA_EJ_"}})
    try:
        raiz = tk.Tk()
        raiz.withdraw()
        try:
            app = GestorProductos(raiz, coleccion)
            app.nombre.insert(0, "PRUEBA_EJ_Corrige")
            app.precio.insert(0, "1000")
            app.agregar()
            documento = coleccion.find_one({"nombre": "PRUEBA_EJ_Corrige"})
            id_nuevo = str(documento["_id"])
            assert app.tabla.exists(id_nuevo), "Después de agregar, la tabla debe mostrar el nuevo producto"

            app.tabla.selection_set(id_nuevo)
            app.precio.delete(0, tk.END)
            app.precio.insert(0, "2000")
            app.actualizar()
            assert coleccion.find_one({"nombre": "PRUEBA_EJ_Corrige"})["precio"] == 2000

            app.tabla.selection_set(id_nuevo)
            app.eliminar()
            assert coleccion.find_one({"nombre": "PRUEBA_EJ_Corrige"}) is None, \
                "eliminar() debe borrar de la colección"
            assert not app.tabla.exists(id_nuevo)
        finally:
            raiz.destroy()
    finally:
        coleccion.delete_many({"nombre": {"$regex": "^PRUEBA_EJ_"}})
        cliente.close()
    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        cliente = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
        raiz = tk.Tk()
        GestorProductos(raiz, cliente[MONGO_DB]["ej_productos"]).pack(fill="both", expand=True)
        raiz.mainloop()
        cliente.close()
