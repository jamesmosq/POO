"""
DROP TABLE IF EXISTS OrderDetails;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Categories;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS Shippers;
DROP TABLE IF EXISTS Suppliers;
"""

import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.geometry('800x400')
root.title("Northwind Management")

# Crear el widget Notebook (pestañas)
notebook = ttk.Notebook(root)

# Crear los frames que irán dentro de las pestañas
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

# Añadir las pestañas al Notebook
notebook.add(tab1, text="Products")
notebook.add(tab2, text="Customers")
notebook.add(tab3, text="Employees")

# Empaquetar el Notebook para que se muestre en la ventana
notebook.pack(expand=True, fill="both")

# CONTENIDO DE LA PESTAÑA 1 (PRODUCTS)
# Título
titulo = tk.Label(tab1,
                  text="FORMULARIO DE PRODUCTS",
                  font=("Arial", 16, "bold"),
                  fg="blue")
titulo.pack(pady=20)

# Frame para contener el formulario
form_frame = tk.Frame(tab1)
form_frame.pack(pady=20, anchor="w", padx=50)

# Fila 1: ProductID
tk.Label(form_frame, text="ProductID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
CustomerID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
CustomerID.grid(row=1, column=1, sticky="w", pady=10)

# Fila 2: ProductName
tk.Label(form_frame, text="ProductName:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
ProductName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
ProductName.grid(row=2, column=1, sticky="w", pady=10)

# Fila 3: SupplierID
tk.Label(form_frame, text="SupplierID:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
SupplierID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
SupplierID.grid(row=3, column=1, sticky="w", pady=10)

# Fila 4: CategoryID
tk.Label(form_frame, text="CategoryID:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
CategoryID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
CategoryID.grid(row=4, column=1, sticky="w", pady=10)

# Fila 5: Unit
tk.Label(form_frame, text="Unit:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
Unit = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
Unit.grid(row=5, column=1, sticky="w", pady=10)

# Fila 6: Price
tk.Label(form_frame, text="Price:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
Price = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
Price.grid(row=6, column=1, sticky="w", pady=10)

# Frame para botones
button_frame = tk.Frame(tab1)
button_frame.pack(pady=20)

# Botones de acción
btn_save = tk.Button(button_frame, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10)
btn_save.pack(side=tk.LEFT, padx=5)

btn_update = tk.Button(button_frame, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10)
btn_update.pack(side=tk.LEFT, padx=5)

btn_delete = tk.Button(button_frame, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10)
btn_delete.pack(side=tk.LEFT, padx=5)

btn_clear = tk.Button(button_frame, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10)
btn_clear.pack(side=tk.LEFT, padx=5)

# CONTENIDO DE LA PESTAÑA 2 (CUSTOMERS)
titulo2 = tk.Label(tab2, text="GESTIÓN DE CUSTOMERS", font=("Arial", 16, "bold"), fg="green")
titulo2.pack(pady=20)

form_frame = tk.Frame(tab2)
form_frame.pack(pady=20, anchor="w", padx=50)

# Fila 1: CustomerID
tk.Label(form_frame, text="CustomerID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
CustomerID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
CustomerID.grid(row=1, column=1, sticky="w", pady=10)

# Fila 2: CustomerName
tk.Label(form_frame, text="CustomerName:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
CustomerName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
CustomerName.grid(row=2, column=1, sticky="w", pady=10)

# Fila 3: ContactName
tk.Label(form_frame, text="ContactName:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
ContactName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
ContactName.grid(row=3, column=1, sticky="w", pady=10)



# PESTAÑA 3 (EMPLOYEES)
titulo3 = tk.Label(tab3, text="GESTIÓN DE EMPLOYEES", font=("Arial", 16, "bold"), fg="red")
titulo3.pack(pady=20)

label3 = tk.Label(tab3, text="Formulario de empleados - En desarrollo", font=("Arial", 12))
label3.pack(pady=10)


root.mainloop()