"""
Solución - Ejercicio propuesto 02 - Lógica separada de la vista
"""

import tkinter as tk
from tkinter import ttk


class Carrito:
    """Lógica del negocio: no sabe nada de Tkinter."""

    def __init__(self):
        self.items = []

    def agregar(self, producto, precio):
        if not isinstance(precio, (int, float)) or precio <= 0:
            raise ValueError("El precio debe ser un número mayor que 0")
        self.items.append((producto, precio))

    def total(self):
        return sum(precio for _, precio in self.items)


class VistaCarrito(tk.Frame):
    """Interfaz: muestra los datos y le pasa las acciones al carrito."""

    def __init__(self, master, carrito):
        super().__init__(master)
        self.carrito = carrito

        tk.Label(self, text="Producto").grid(row=0, column=0)
        self.producto = tk.Entry(self)
        self.producto.grid(row=0, column=1)
        tk.Label(self, text="Precio").grid(row=1, column=0)
        self.precio = tk.Entry(self)
        self.precio.grid(row=1, column=1)
        self.boton = tk.Button(self, text="Agregar", command=self.agregar)
        self.boton.grid(row=2, column=0, columnspan=2, pady=5)

        self.tabla = ttk.Treeview(self, columns=("producto", "precio"), show="headings", height=6)
        self.tabla.heading("producto", text="Producto")
        self.tabla.heading("precio", text="Precio")
        self.tabla.grid(row=3, column=0, columnspan=2)

        self.total = tk.Label(self, text="Total: $0")
        self.total.grid(row=4, column=0, columnspan=2)
        self.error = tk.Label(self, text="", fg="red")
        self.error.grid(row=5, column=0, columnspan=2)

    def agregar(self):
        producto = self.producto.get().strip()
        try:
            precio = float(self.precio.get())
            self.carrito.agregar(producto, precio)
        except ValueError:
            self.error.config(text="Precio inválido")
            return
        self.error.config(text="")
        self.tabla.insert("", tk.END, values=(producto, f"{precio:,.0f}"))
        self.total.config(text=f"Total: ${self.carrito.total():,.0f}")
        self.producto.delete(0, tk.END)
        self.precio.delete(0, tk.END)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    carrito = Carrito()
    carrito.agregar("Libro", 50000)
    assert carrito.total() == 50000
    try:
        carrito.agregar("Gratis", 0)
        raise AssertionError("Un precio de 0 debe lanzar ValueError")
    except ValueError:
        pass

    raiz = tk.Tk()
    raiz.withdraw()
    carrito = Carrito()
    vista = VistaCarrito(raiz, carrito)

    def agregar(producto, precio):
        vista.producto.insert(0, producto)
        vista.precio.insert(0, precio)
        vista.boton.invoke()

    agregar("Café", "12000")
    agregar("Pan", "3500")
    filas = [vista.tabla.item(i, "values") for i in vista.tabla.get_children()]
    assert [fila[0] for fila in filas] == ["Café", "Pan"], filas
    assert vista.total.cget("text") == "Total: $15,500"
    assert carrito.items == [("Café", 12000), ("Pan", 3500)]
    assert vista.producto.get() == "" and vista.precio.get() == ""

    agregar("Error", "abc")
    assert vista.error.cget("text") == "Precio inválido"
    assert len(carrito.items) == 2 and len(vista.tabla.get_children()) == 2
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        VistaCarrito(raiz, Carrito()).pack(padx=10, pady=10)
        raiz.mainloop()
