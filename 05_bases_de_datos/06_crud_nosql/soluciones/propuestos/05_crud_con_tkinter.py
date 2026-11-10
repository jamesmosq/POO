"""
Solución - Ejercicio propuesto 05 - CRUD con Tkinter
"""
import os
import re
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

        formulario = tk.Frame(self)
        formulario.pack(fill="x")
        self.nombre = tk.Entry(formulario, width=30)
        self.precio = tk.Entry(formulario, width=30)
        self.stock = tk.Entry(formulario, width=30)
        for fila, (texto, entrada) in enumerate((("Nombre", self.nombre), ("Precio", self.precio),
                                                  ("Stock", self.stock))):
            tk.Label(formulario, text=texto).grid(row=fila, column=0, sticky="e")
            entrada.grid(row=fila, column=1, pady=2)

        botones = tk.Frame(self)
        botones.pack(pady=5)
        self.boton_agregar = tk.Button(botones, text="Agregar", command=self.agregar)
        self.boton_actualizar = tk.Button(botones, text="Actualizar", command=self.actualizar)
        self.boton_eliminar = tk.Button(botones, text="Eliminar", command=self.eliminar)
        for boton in (self.boton_agregar, self.boton_actualizar, self.boton_eliminar):
            boton.pack(side="left", padx=2)

        self.estado = tk.Label(self, text="", fg="red")
        self.estado.pack()

        busqueda = tk.Frame(self)
        busqueda.pack(fill="x")
        tk.Label(busqueda, text="Buscar").pack(side="left")
        self.buscador = tk.Entry(busqueda)
        self.buscador.pack(side="left", fill="x", expand=True)
        self.buscador.bind("<KeyRelease>", lambda evento: self.cargar())

        self.tabla = ttk.Treeview(self, columns=("nombre", "precio", "stock"), show="headings", height=8)
        for columna in ("nombre", "precio", "stock"):
            self.tabla.heading(columna, text=columna.capitalize())
        self.tabla.pack(fill="both", expand=True)
        self.tabla.bind("<<TreeviewSelect>>", lambda evento: self.al_seleccionar())
        self.cargar()

    def _seleccionado(self):
        seleccion = self.tabla.selection()
        return ObjectId(seleccion[0]) if seleccion else None

    def _datos_formulario(self):
        nombre = self.nombre.get().strip()
        if not nombre:
            self.estado.config(text="El nombre es obligatorio")
            return None
        try:
            precio = float(self.precio.get())
            stock = int(self.stock.get())
        except ValueError:
            self.estado.config(text="Precio y stock deben ser números")
            return None
        self.estado.config(text="")
        return {"nombre": nombre, "precio": precio, "stock": stock}

    def cargar(self):
        self.tabla.delete(*self.tabla.get_children())
        filtro = {}
        texto = self.buscador.get().strip()
        if texto:
            filtro["nombre"] = {"$regex": re.escape(texto), "$options": "i"}
        for doc in self.coleccion.find(filtro).sort("nombre", ASCENDING):
            self.tabla.insert("", tk.END, iid=str(doc["_id"]),
                              values=(doc["nombre"], doc.get("precio", ""), doc.get("stock", "")))

    def al_seleccionar(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            return
        valores = self.tabla.item(seleccion[0], "values")
        for entrada, valor in zip((self.nombre, self.precio, self.stock), valores):
            entrada.delete(0, tk.END)
            entrada.insert(0, valor)

    def agregar(self):
        datos = self._datos_formulario()
        if datos is None:
            return
        self.coleccion.insert_one(datos)
        self.cargar()

    def actualizar(self):
        oid = self._seleccionado()
        if oid is None:
            return
        datos = self._datos_formulario()
        if datos is None:
            return
        self.coleccion.update_one({"_id": oid}, {"$set": datos})
        self.cargar()

    def eliminar(self):
        oid = self._seleccionado()
        if oid is None:
            return
        self.coleccion.delete_one({"_id": oid})
        self.cargar()


# ----------------------------------------------------------------------
# Pruebas
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
