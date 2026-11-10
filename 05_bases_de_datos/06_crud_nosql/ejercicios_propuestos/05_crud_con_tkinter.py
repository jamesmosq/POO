"""
Ejercicio propuesto 05 - CRUD con Tkinter
Nivel: avanzado

Es el CRUD de transportadoras del tema 04_crud_con_interfaz, pero ahora
los datos viven en una colección de MongoDB.

Requisitos. Crea la clase GestorProductos(tk.Frame) que recibe
(master, coleccion):
1. self.nombre, self.precio y self.stock: Entry del formulario.
2. self.buscador: Entry para filtrar por nombre.
3. self.estado: Label donde se muestran los mensajes de error.
4. Botones self.boton_agregar, self.boton_actualizar y self.boton_eliminar.
5. self.tabla: Treeview con columnas ("nombre", "precio", "stock"). Usa
   el _id del documento EN TEXTO como iid de cada fila:
       self.tabla.insert("", tk.END, iid=str(doc["_id"]), values=(...))
6. cargar(): vacía la tabla y la llena con los documentos ordenados por
   nombre. Si self.buscador tiene texto, solo los que lo contienen en el
   nombre (sin distinguir mayúsculas, texto escapado).
7. agregar(), actualizar() y eliminar(): modifican la COLECCIÓN y después
   llaman a cargar(). actualizar y eliminar trabajan sobre la fila
   seleccionada (selection() devuelve una TUPLA); sin selección no hacen
   nada. Si el nombre está vacío o precio/stock no son números válidos
   (precio float, stock int), no tocan la base y escriben un mensaje en
   self.estado. Si todo sale bien, dejan self.estado vacío.
8. al_seleccionar(): copia los datos de la fila seleccionada a los Entry.

No uses messagebox: las pruebas corren con la ventana oculta y un cuadro
de diálogo las dejaría esperando.

Conceptos: CRUD con interfaz y MongoDB, ObjectId como iid, la base de
datos como fuente de verdad.
"""
import os
import re
import tkinter as tk
from tkinter import ttk

from bson import ObjectId
from pymongo import ASCENDING, MongoClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "curso_poo")

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
def debe_fallar(funcion, *argumentos, **nombrados):
    try:
        funcion(*argumentos, **nombrados)
    except ValueError:
        return
    raise AssertionError(f"{funcion.__name__}{argumentos} debía lanzar ValueError")


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

            def escribir(nombre, precio, stock):
                for entrada, valor in ((app.nombre, nombre), (app.precio, precio), (app.stock, stock)):
                    entrada.delete(0, tk.END)
                    entrada.insert(0, valor)

            def en_base(nombre):
                return coleccion.find_one({"nombre": nombre})

            escribir("PRUEBA_EJ_Parlante", "85000", "4")
            app.boton_agregar.invoke()
            documento = en_base("PRUEBA_EJ_Parlante")
            assert documento is not None, "agregar() debe guardar en la colección"
            assert documento["precio"] == 85000 and documento["stock"] == 4, \
                "Guarda el precio como número (float) y el stock como entero (int)"
            id_nuevo = str(documento["_id"])
            assert app.tabla.exists(id_nuevo), "La fila debe usar str(_id) como iid"
            assert app.estado.cget("text") == ""

            app.buscador.insert(0, "prueba_ej_PAR")
            app.cargar()
            assert list(app.tabla.get_children()) == [id_nuevo], \
                "cargar() debe filtrar por el texto del buscador, sin distinguir mayúsculas"
            app.buscador.delete(0, tk.END)
            app.buscador.insert(0, "PRUEBA_EJ_.")
            app.cargar()
            assert list(app.tabla.get_children()) == [], "Escapa el texto del buscador"
            app.buscador.delete(0, tk.END)
            app.cargar()

            app.tabla.selection_set(id_nuevo)
            app.al_seleccionar()
            assert app.nombre.get() == "PRUEBA_EJ_Parlante"

            escribir("PRUEBA_EJ_Parlante", "79000", "6")
            app.tabla.selection_set(id_nuevo)
            app.boton_actualizar.invoke()
            documento = en_base("PRUEBA_EJ_Parlante")
            assert documento["precio"] == 79000 and documento["stock"] == 6, \
                "actualizar() debe modificar la colección"
            assert str(app.tabla.item(id_nuevo, "values")[2]) == "6", "Y después recargar la tabla"

            cantidad = coleccion.count_documents({})
            escribir("", "1", "1")
            app.boton_agregar.invoke()
            escribir("PRUEBA_EJ_Malo", "caro", "1")
            app.boton_agregar.invoke()
            assert coleccion.count_documents({}) == cantidad, "Con datos inválidos no se inserta"
            assert app.estado.cget("text") != "", "Muestra el error en self.estado"

            app.tabla.selection_set(id_nuevo)
            app.boton_eliminar.invoke()
            assert en_base("PRUEBA_EJ_Parlante") is None, "eliminar() debe borrar de la colección"
            assert not app.tabla.exists(id_nuevo)

            filas = len(app.tabla.get_children())
            app.tabla.selection_remove(app.tabla.selection())
            app.boton_eliminar.invoke()
            app.boton_actualizar.invoke()
            assert len(app.tabla.get_children()) == filas
        finally:
            raiz.destroy()
    finally:
        coleccion.delete_many({"nombre": {"$regex": "^PRUEBA_EJ_"}})
        cliente.close()
    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        cliente = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
        raiz = tk.Tk()
        raiz.title("Productos (MongoDB)")
        GestorProductos(raiz, cliente[MONGO_DB]["ej_productos"]).pack(fill="both", expand=True,
                                                                       padx=10, pady=10)
        raiz.mainloop()
        cliente.close()
