"""
Ejercicio propuesto 02 - Lógica separada de la vista
Nivel: intermedio

Buena práctica: la lógica del negocio no debe depender de Tkinter. Así se
puede probar sola y reutilizar en otra interfaz (web, consola, móvil).

Requisitos:
1. Clase Carrito (SIN nada de Tkinter):
   - agregar(producto, precio): precio debe ser un número mayor que 0 (si
     no, ValueError).
   - items: lista de tuplas (producto, precio).
   - total(): suma de los precios.
2. Clase VistaCarrito(tk.Frame) que recibe (master, carrito):
   - self.producto y self.precio: Entry.
   - self.boton: Button "Agregar".
   - self.tabla: ttk.Treeview con columnas ("producto", "precio") y
     show="headings".
   - self.total: Label "Total: $0".
   - self.error: Label para mensajes de error.
   - Al agregar: convierte el precio, llama a carrito.agregar(...),
     inserta la fila en la tabla, actualiza el total ("Total: $15,500") y
     limpia los Entry. Si el precio no es válido, muestra
     "Precio inválido" en self.error y no agrega nada.

La vista NO calcula el total: se lo pide al carrito.

Conceptos: separación de responsabilidades, Treeview, MVC sencillo.
"""
import tkinter as tk
from tkinter import ttk

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
