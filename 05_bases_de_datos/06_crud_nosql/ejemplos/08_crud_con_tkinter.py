"""
Ejemplo 08 - CRUD completo con Tkinter y MongoDB
Paso 8 (final) de la ruta del CRUD con MongoDB.

Qué aprendes:
    - Unir la interfaz (Tkinter) con el repositorio del ejemplo 07.
    - Usar el id del documento (texto) como iid de cada fila del Treeview,
      para saber siempre a qué documento corresponde la fila.
    - La base de datos es la fuente de verdad: cada operación modifica
      MongoDB y después se recarga la tabla con lo que hay en la base.
    - Mostrar los errores de validación con messagebox.

Fíjate en que esta clase no importa pymongo: no sabe que los datos están
en MongoDB. Si mañana cambias a MySQL, solo cambia el repositorio.

Ejecuta antes 02_insertar.py para tener datos de muestra.
"""
import tkinter as tk
from tkinter import messagebox, ttk

from pymongo.errors import PyMongoError

from repositorio_productos import ConexionMongo, RepositorioProductos


class VentanaProductos(tk.Frame):
    COLUMNAS = ("nombre", "categoria", "precio", "stock")

    def __init__(self, master, repositorio):
        super().__init__(master)
        self.repositorio = repositorio
        self._crear_formulario()
        self._crear_botones()
        self._crear_buscador()
        self._crear_tabla()
        self.cargar()

    # ---- Construcción de la interfaz ----------------------------------
    def _crear_formulario(self):
        marco = ttk.LabelFrame(self, text="Producto")
        marco.pack(fill="x")
        self.entradas = {}
        for fila, (campo, etiqueta) in enumerate((("nombre", "Nombre"), ("categoria", "Categoría"),
                                                   ("precio", "Precio"), ("stock", "Stock"))):
            ttk.Label(marco, text=etiqueta).grid(row=fila, column=0, sticky="e", padx=5, pady=2)
            entrada = ttk.Entry(marco, width=35)
            entrada.grid(row=fila, column=1, sticky="w", padx=5, pady=2)
            self.entradas[campo] = entrada

    def _crear_botones(self):
        marco = ttk.Frame(self)
        marco.pack(pady=6)
        for texto, comando in (("Agregar", self.agregar), ("Actualizar", self.actualizar),
                               ("Eliminar", self.eliminar), ("Limpiar", self.limpiar_formulario)):
            ttk.Button(marco, text=texto, command=comando).pack(side="left", padx=3)

    def _crear_buscador(self):
        marco = ttk.Frame(self)
        marco.pack(fill="x")
        ttk.Label(marco, text="Buscar por nombre:").pack(side="left")
        self.buscador = ttk.Entry(marco)
        self.buscador.pack(side="left", fill="x", expand=True, padx=5)
        # Buscar mientras se escribe: cada tecla recarga la tabla filtrada.
        self.buscador.bind("<KeyRelease>", lambda evento: self.cargar())
        self.contador = ttk.Label(marco, text="")
        self.contador.pack(side="right")

    def _crear_tabla(self):
        self.tabla = ttk.Treeview(self, columns=self.COLUMNAS, show="headings", height=12)
        for columna, titulo, ancho in (("nombre", "Nombre", 220), ("categoria", "Categoría", 140),
                                       ("precio", "Precio", 110), ("stock", "Stock", 70)):
            self.tabla.heading(columna, text=titulo)
            self.tabla.column(columna, width=ancho, anchor="e" if columna in ("precio", "stock") else "w")
        self.tabla.pack(fill="both", expand=True, pady=(6, 0))
        self.tabla.bind("<<TreeviewSelect>>", lambda evento: self.al_seleccionar())

    # ---- Ayudas ---------------------------------------------------------
    def _datos_formulario(self):
        return {campo: entrada.get() for campo, entrada in self.entradas.items()}

    def _id_seleccionado(self):
        seleccion = self.tabla.selection()   # es una TUPLA de iids
        return seleccion[0] if seleccion else None

    def limpiar_formulario(self):
        for entrada in self.entradas.values():
            entrada.delete(0, tk.END)
        self.tabla.selection_remove(self.tabla.selection())

    # ---- Leer -----------------------------------------------------------
    def cargar(self):
        # 1. Vaciar la tabla (si no, las filas se duplican en cada recarga).
        self.tabla.delete(*self.tabla.get_children())
        # 2. Pedir los datos al repositorio y 3. insertar fila por fila.
        productos = self.repositorio.listar(self.buscador.get())
        for producto in productos:
            self.tabla.insert("", tk.END, iid=producto["id"], values=(
                producto["nombre"], producto.get("categoria", ""),
                f"{producto['precio']:,.0f}", producto["stock"]))
        self.contador.config(text=f"{len(productos)} producto(s)")

    def al_seleccionar(self):
        id_producto = self._id_seleccionado()
        if id_producto is None:
            return
        # Leemos de la base, no de la fila: la fila tiene el precio con
        # formato (separadores de miles) y no todos los campos.
        producto = self.repositorio.obtener(id_producto)
        if producto is None:
            return
        for campo, entrada in self.entradas.items():
            entrada.delete(0, tk.END)
            entrada.insert(0, str(producto.get(campo, "")))

    # ---- Crear, actualizar y eliminar -----------------------------------
    def agregar(self):
        try:
            id_nuevo = self.repositorio.crear(self._datos_formulario())
        except ValueError as error:
            messagebox.showwarning("Datos no válidos", str(error), parent=self)
            return
        self.cargar()
        if self.tabla.exists(id_nuevo):
            self.tabla.selection_set(id_nuevo)
            self.tabla.see(id_nuevo)

    def actualizar(self):
        id_producto = self._id_seleccionado()
        if id_producto is None:
            messagebox.showinfo("Actualizar", "Selecciona un producto de la tabla", parent=self)
            return
        try:
            self.repositorio.actualizar(id_producto, self._datos_formulario())
        except ValueError as error:
            messagebox.showwarning("Datos no válidos", str(error), parent=self)
            return
        self.cargar()

    def eliminar(self):
        id_producto = self._id_seleccionado()
        if id_producto is None:
            messagebox.showinfo("Eliminar", "Selecciona un producto de la tabla", parent=self)
            return
        nombre = self.tabla.item(id_producto, "values")[0]
        if not messagebox.askyesno("Eliminar", f"¿Eliminar {nombre}?", parent=self):
            return
        self.repositorio.eliminar(id_producto)
        self.limpiar_formulario()
        self.cargar()


def main():
    try:
        with ConexionMongo() as db:
            raiz = tk.Tk()
            raiz.title("Productos - MongoDB")
            VentanaProductos(raiz, RepositorioProductos(db)).pack(fill="both", expand=True,
                                                                  padx=10, pady=10)
            raiz.mainloop()
    except PyMongoError as error:
        # Si MongoDB está apagado, avisamos en vez de mostrar una traza.
        raiz_error = tk.Tk()
        raiz_error.withdraw()
        messagebox.showerror("MongoDB", f"No se pudo conectar a MongoDB:\n{error}")
        raiz_error.destroy()


if __name__ == "__main__":
    main()
