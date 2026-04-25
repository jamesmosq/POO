import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.geometry('900x600')
root.title("Northwind Management")

# Crear el widget Notebook (pestañas)
notebook = ttk.Notebook(root)

# Frames que para las pestañas
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

# Añadir las pestañas al Notebook
notebook.add(tab1, text="Products")
notebook.add(tab2, text="Customers")
notebook.add(tab3, text="Employees")

# Empaquetar el Notebook para que se muestre en la ventana
notebook.pack(expand=True, fill="both")

# =================== FUNCIONES PARA PRODUCTS ===================
def save_product():
    messagebox.showinfo("Guardar", "Producto guardado correctamente")

def update_product():
    messagebox.showinfo("Actualizar", "Producto actualizado correctamente")

def delete_product():
    if messagebox.askyesno("Eliminar", "¿Está seguro de eliminar este producto?"):
        messagebox.showinfo("Eliminar", "Producto eliminado correctamente")

def clear_product_form():
    ProductID.delete(0, tk.END)
    ProductName.delete(0, tk.END)
    SupplierID.delete(0, tk.END)
    CategoryID.delete(0, tk.END)
    Unit.delete(0, tk.END)
    Price.delete(0, tk.END)

# =================== CONTENIDO DE LA PESTAÑA 1 (PRODUCTS) ===================
# Título
titulo = tk.Label(tab1,
                  text="FORM PRODUCTS",
                  font=("Arial", 16, "bold"),
                  fg="green")
titulo.pack(pady=20)

# Frame para contener el formulario
form_frame_products = tk.Frame(tab1)
form_frame_products.pack(pady=20, anchor="w", padx=50)

# Fila 1: ProductID
tk.Label(form_frame_products, text="ProductID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
ProductID = tk.Entry(form_frame_products, width=25, font=("Arial", 12), relief="solid", bd=1)
ProductID.grid(row=1, column=1, sticky="w", pady=10)

# Fila 2: ProductName
tk.Label(form_frame_products, text="ProductName:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
ProductName = tk.Entry(form_frame_products, width=25, font=("Arial", 12), relief="solid", bd=1)
ProductName.grid(row=2, column=1, sticky="w", pady=10)

# Fila 3: SupplierID
tk.Label(form_frame_products, text="SupplierID:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
SupplierID = tk.Entry(form_frame_products, width=25, font=("Arial", 12), relief="solid", bd=1)
SupplierID.grid(row=3, column=1, sticky="w", pady=10)

# Fila 4: CategoryID
tk.Label(form_frame_products, text="CategoryID:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
CategoryID = tk.Entry(form_frame_products, width=25, font=("Arial", 12), relief="solid", bd=1)
CategoryID.grid(row=4, column=1, sticky="w", pady=10)

# Fila 5: Unit
tk.Label(form_frame_products, text="Unit:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
Unit = tk.Entry(form_frame_products, width=25, font=("Arial", 12), relief="solid", bd=1)
Unit.grid(row=5, column=1, sticky="w", pady=10)

# Fila 6: Price
tk.Label(form_frame_products, text="Price:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
Price = tk.Entry(form_frame_products, width=25, font=("Arial", 12), relief="solid", bd=1)
Price.grid(row=6, column=1, sticky="w", pady=10)

# Frame para botones
button_frame_products = tk.Frame(tab1)
button_frame_products.pack(pady=20)

# Botones de acción
btn_save_product = tk.Button(button_frame_products, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10, command=save_product)
btn_save_product.pack(side=tk.LEFT, padx=5)

btn_update_product = tk.Button(button_frame_products, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10, command=update_product)
btn_update_product.pack(side=tk.LEFT, padx=5)

btn_delete_product = tk.Button(button_frame_products, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10, command=delete_product)
btn_delete_product.pack(side=tk.LEFT, padx=5)

btn_clear_product = tk.Button(button_frame_products, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10, command=clear_product_form)
btn_clear_product.pack(side=tk.LEFT, padx=5)

# =================== FUNCIONES PARA CUSTOMERS ===================
def save_customer():
    messagebox.showinfo("Guardar", "Cliente guardado correctamente")

def update_customer():
    messagebox.showinfo("Actualizar", "Cliente actualizado correctamente")

def delete_customer():
    if messagebox.askyesno("Eliminar", "¿Está seguro de eliminar este cliente?"):
        messagebox.showinfo("Eliminar", "Cliente eliminado correctamente")

def clear_customer_form():
    CustomerID.delete(0, tk.END)
    CustomerName.delete(0, tk.END)
    ContactName.delete(0, tk.END)
    Address.delete(0, tk.END)
    City.delete(0, tk.END)
    PostalCode.delete(0, tk.END)
    Country.delete(0, tk.END)

# =================== CONTENIDO DE LA PESTAÑA 2 (CUSTOMERS) ===================
titulo2 = tk.Label(tab2, text="GESTIÓN DE CUSTOMERS", font=("Arial", 16, "bold"), fg="green")
titulo2.pack(pady=20)

form_frame_customers = tk.Frame(tab2)
form_frame_customers.pack(pady=20, anchor="w", padx=50)

# Fila 1: CustomerID
tk.Label(form_frame_customers, text="CustomerID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
CustomerID = tk.Entry(form_frame_customers, width=25, font=("Arial", 12), relief="solid", bd=1)
CustomerID.grid(row=1, column=1, sticky="w", pady=10)

# Fila 2: CustomerName
tk.Label(form_frame_customers, text="CustomerName:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
CustomerName = tk.Entry(form_frame_customers, width=25, font=("Arial", 12), relief="solid", bd=1)
CustomerName.grid(row=2, column=1, sticky="w", pady=10)

# Fila 3: ContactName
tk.Label(form_frame_customers, text="ContactName:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
ContactName = tk.Entry(form_frame_customers, width=25, font=("Arial", 12), relief="solid", bd=1)
ContactName.grid(row=3, column=1, sticky="w", pady=10)

# Fila 4: Address
tk.Label(form_frame_customers, text="Address:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
Address = tk.Entry(form_frame_customers, width=25, font=("Arial", 12), relief="solid", bd=1)
Address.grid(row=4, column=1, sticky="w", pady=10)

# Fila 5: City
tk.Label(form_frame_customers, text="City:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
City = tk.Entry(form_frame_customers, width=25, font=("Arial", 12), relief="solid", bd=1)
City.grid(row=5, column=1, sticky="w", pady=10)

# Fila 6: PostalCode
tk.Label(form_frame_customers, text="PostalCode:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
PostalCode = tk.Entry(form_frame_customers, width=25, font=("Arial", 12), relief="solid", bd=1)
PostalCode.grid(row=6, column=1, sticky="w", pady=10)

# Fila 7: Country
tk.Label(form_frame_customers, text="Country:", font=("Arial", 12)).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
Country = tk.Entry(form_frame_customers, width=25, font=("Arial", 12), relief="solid", bd=1)
Country.grid(row=7, column=1, sticky="w", pady=10)

# Frame para botones de customers
button_frame_customers = tk.Frame(tab2)
button_frame_customers.pack(pady=20)

# Botones de acción para customers
btn_save_customer = tk.Button(button_frame_customers, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10, command=save_customer)
btn_save_customer.pack(side=tk.LEFT, padx=5)

btn_update_customer = tk.Button(button_frame_customers, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10, command=update_customer)
btn_update_customer.pack(side=tk.LEFT, padx=5)

btn_delete_customer = tk.Button(button_frame_customers, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10, command=delete_customer)
btn_delete_customer.pack(side=tk.LEFT, padx=5)

btn_clear_customer = tk.Button(button_frame_customers, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10, command=clear_customer_form)
btn_clear_customer.pack(side=tk.LEFT, padx=5)

# =================== FUNCIONES PARA EMPLOYEES ===================
def save_employee():
    messagebox.showinfo("Guardar", "Empleado guardado correctamente")

def update_employee():
    messagebox.showinfo("Actualizar", "Empleado actualizado correctamente")

def delete_employee():
    if messagebox.askyesno("Eliminar", "¿Está seguro de eliminar este empleado?"):
        messagebox.showinfo("Eliminar", "Empleado eliminado correctamente")

def clear_employee_form():
    EmployeeID.delete(0, tk.END)
    LastName.delete(0, tk.END)
    FirstName.delete(0, tk.END)
    BirthDate.delete(0, tk.END)
    Photo.delete(0, tk.END)
    Notes.delete('1.0', tk.END)

# =================== CONTENIDO DE LA PESTAÑA 3 (EMPLOYEES) ===================
titulo3 = tk.Label(tab3, text="GESTIÓN DE EMPLOYEES", font=("Arial", 16, "bold"), fg="red")
titulo3.pack(pady=20)

form_frame_employees = tk.Frame(tab3)
form_frame_employees.pack(pady=20, anchor="w", padx=50)

# Fila 1: EmployeeID
tk.Label(form_frame_employees, text="EmployeeID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
EmployeeID = tk.Entry(form_frame_employees, width=25, font=("Arial", 12), relief="solid", bd=1)
EmployeeID.grid(row=1, column=1, sticky="w", pady=10)

# Fila 2: LastName
tk.Label(form_frame_employees, text="LastName:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
LastName = tk.Entry(form_frame_employees, width=25, font=("Arial", 12), relief="solid", bd=1)
LastName.grid(row=2, column=1, sticky="w", pady=10)

# Fila 3: FirstName
tk.Label(form_frame_employees, text="FirstName:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
FirstName = tk.Entry(form_frame_employees, width=25, font=("Arial", 12), relief="solid", bd=1)
FirstName.grid(row=3, column=1, sticky="w", pady=10)

# Fila 4: BirthDate
tk.Label(form_frame_employees, text="BirthDate:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
BirthDate = tk.Entry(form_frame_employees, width=25, font=("Arial", 12), relief="solid", bd=1)
BirthDate.grid(row=4, column=1, sticky="w", pady=10)

# Fila 5: Photo
tk.Label(form_frame_employees, text="Photo:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
Photo = tk.Entry(form_frame_employees, width=25, font=("Arial", 12), relief="solid", bd=1)
Photo.grid(row=5, column=1, sticky="w", pady=10)

# Fila 6: Notes (Text widget para texto largo)
tk.Label(form_frame_employees, text="Notes:", font=("Arial", 12)).grid(row=6, column=0, sticky="nw", padx=(0, 10), pady=10)
Notes = tk.Text(form_frame_employees, width=25, height=4, font=("Arial", 12), relief="solid", bd=1)
Notes.grid(row=6, column=1, sticky="w", pady=10)

# Frame para botones de employees
button_frame_employees = tk.Frame(tab3)
button_frame_employees.pack(pady=20)

# Botones de acción para employees
btn_save_employee = tk.Button(button_frame_employees, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10, command=save_employee)
btn_save_employee.pack(side=tk.LEFT, padx=5)

btn_update_employee = tk.Button(button_frame_employees, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10, command=update_employee)
btn_update_employee.pack(side=tk.LEFT, padx=5)

btn_delete_employee = tk.Button(button_frame_employees, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10, command=delete_employee)
btn_delete_employee.pack(side=tk.LEFT, padx=5)

btn_clear_employee = tk.Button(button_frame_employees, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10, command=clear_employee_form)
btn_clear_employee.pack(side=tk.LEFT, padx=5)

# Ejecutar la aplicación
root.mainloop()