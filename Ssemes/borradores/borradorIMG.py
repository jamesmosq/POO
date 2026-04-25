import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import mysql.connector
import os
import shutil
from PIL import Image, ImageTk


class EmployeeGUI:
    def __init__(self, master):
        self.master = master
        master.title("Gestión de Empleados")

        # Configuración de la conexión a la base de datos
        self.db_config = {
            "host": "localhost",
            "user": "root",
            "password": "",
            "database": "Northwind"
        }

        # Campos de entrada
        self.labels = ["ID:", "Apellido:", "Nombre:", "Fecha de Nacimiento (YYYY-MM-DD):", "Notas:"]
        self.entries = []

        for i, label in enumerate(self.labels):
            tk.Label(master, text=label).grid(row=i, column=0, sticky="e", padx=5, pady=5)
            entry = tk.Entry(master, width=50)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries.append(entry)

        # El campo ID será de solo lectura
        self.entries[0].config(state='readonly')

        # Botón para seleccionar imagen
        self.image_path = ""
        self.image_button = tk.Button(master, text="Seleccionar Foto", command=self.select_image)
        self.image_button.grid(row=len(self.labels), column=0, padx=5, pady=5)

        # Label para mostrar la imagen seleccionada
        self.image_label = tk.Label(master)
        self.image_label.grid(row=len(self.labels), column=1, padx=5, pady=5)

        # Botones CRUD
        self.create_button = tk.Button(master, text="Crear", command=self.create_employee)
        self.create_button.grid(row=len(self.labels) + 1, column=0, pady=5)

        self.read_button = tk.Button(master, text="Leer", command=self.read_employee)
        self.read_button.grid(row=len(self.labels) + 1, column=1, pady=5)

        self.update_button = tk.Button(master, text="Actualizar", command=self.update_employee)
        self.update_button.grid(row=len(self.labels) + 2, column=0, pady=5)

        self.delete_button = tk.Button(master, text="Eliminar", command=self.delete_employee)
        self.delete_button.grid(row=len(self.labels) + 2, column=1, pady=5)

        # Treeview para mostrar empleados
        self.tree = ttk.Treeview(master, columns=("ID", "Apellido", "Nombre", "Fecha de Nacimiento", "Foto", "Notas"),
                                 show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Apellido", text="Apellido")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Fecha de Nacimiento", text="Fecha de Nacimiento")
        self.tree.heading("Foto", text="Foto")
        self.tree.heading("Notas", text="Notas")
        self.tree.grid(row=len(self.labels) + 3, column=0, columnspan=2, pady=10)

        # Cargar datos iniciales
        self.load_employees()

    def select_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")])
        if self.image_path:
            image = Image.open(self.image_path)
            image.thumbnail((100, 100))
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo

    def create_employee(self):
        last_name = self.entries[1].get()
        first_name = self.entries[2].get()
        birth_date = self.entries[3].get()
        notes = self.entries[4].get()

        if not self.image_path:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una imagen.")
            return

        if not os.path.exists('../../img'):
            os.makedirs('../../img')

        file_name = os.path.basename(self.image_path)
        new_image_path = os.path.join('../../img', file_name)
        shutil.copy(self.image_path, new_image_path)

        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()

            query = """INSERT INTO Employees (LastName, FirstName, BirthDate, Photo, Notes)
                       VALUES (%s, %s, %s, %s, %s)"""
            values = (last_name, first_name, birth_date, new_image_path, notes)

            cursor.execute(query, values)
            connection.commit()

            messagebox.showinfo("Éxito", "Empleado agregado correctamente")
            self.clear_entries()
            self.load_employees()

        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error al agregar empleado: {error}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def read_employee(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un empleado.")
            return

        employee_id = self.tree.item(selected_item)['values'][0]

        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()

            query = "SELECT * FROM Employees WHERE EmployeeID = %s"
            cursor.execute(query, (employee_id,))
            employee = cursor.fetchone()

            if employee:
                # Cargar datos en los campos de entrada
                self.entries[0].config(state='normal')
                self.entries[0].delete(0, tk.END)
                self.entries[0].insert(0, employee[0])
                self.entries[0].config(state='readonly')
                self.entries[1].delete(0, tk.END)
                self.entries[1].insert(0, employee[1])
                self.entries[2].delete(0, tk.END)
                self.entries[2].insert(0, employee[2])
                self.entries[3].delete(0, tk.END)
                self.entries[3].insert(0, employee[3].strftime('%Y-%m-%d') if employee[3] else '')
                self.entries[4].delete(0, tk.END)
                self.entries[4].insert(0, employee[5])

                # Manejar la imagen
                self.image_path = employee[4]
                print(f"Ruta de la imagen en la base de datos: {self.image_path}")

                if self.image_path:
                    full_path = os.path.abspath(self.image_path)
                    print(f"Ruta completa de la imagen: {full_path}")

                    if os.path.exists(full_path):
                        print("La imagen existe en el sistema de archivos.")
                        try:
                            image = Image.open(full_path)
                            image.thumbnail((100, 100))
                            photo = ImageTk.PhotoImage(image)
                            self.image_label.config(image=photo)
                            self.image_label.image = photo
                            print("Imagen cargada y mostrada con éxito.")
                        except Exception as e:
                            print(f"Error al cargar la imagen: {e}")
                            self.image_label.config(image="")
                            messagebox.showwarning("Advertencia", f"Error al cargar la imagen: {e}")
                    else:
                        print("La imagen no existe en el sistema de archivos.")
                        self.image_label.config(image="")
                        messagebox.showwarning("Advertencia", "La imagen no se encuentra en la ruta especificada.")
                else:
                    print("No hay ruta de imagen guardada para este empleado.")
                    self.image_label.config(image="")

        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error al leer empleado: {error}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    def update_employee(self):
        employee_id = self.entries[0].get()
        if not employee_id:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un empleado para actualizar.")
            return

        last_name = self.entries[1].get()
        first_name = self.entries[2].get()
        birth_date = self.entries[3].get()
        notes = self.entries[4].get()

        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()

            if self.image_path:
                if not os.path.exists('../../img'):
                    os.makedirs('../../img')
                file_name = os.path.basename(self.image_path)
                new_image_path = os.path.join('../../img', file_name)
                shutil.copy(self.image_path, new_image_path)

                query = """UPDATE Employees 
                           SET LastName = %s, FirstName = %s, BirthDate = %s, Photo = %s, Notes = %s
                           WHERE EmployeeID = %s"""
                values = (last_name, first_name, birth_date, new_image_path, notes, employee_id)
            else:
                query = """UPDATE Employees 
                           SET LastName = %s, FirstName = %s, BirthDate = %s, Notes = %s
                           WHERE EmployeeID = %s"""
                values = (last_name, first_name, birth_date, notes, employee_id)

            cursor.execute(query, values)
            connection.commit()

            messagebox.showinfo("Éxito", "Empleado actualizado correctamente")
            self.clear_entries()
            self.load_employees()

        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error al actualizar empleado: {error}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def delete_employee(self):
        employee_id = self.entries[0].get()
        if not employee_id:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un empleado para eliminar.")
            return

        if messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este empleado?"):
            try:
                connection = mysql.connector.connect(**self.db_config)
                cursor = connection.cursor()

                query = "DELETE FROM Employees WHERE EmployeeID = %s"
                cursor.execute(query, (employee_id,))
                connection.commit()

                messagebox.showinfo("Éxito", "Empleado eliminado correctamente")
                self.clear_entries()
                self.load_employees()

            except mysql.connector.Error as error:
                messagebox.showerror("Error", f"Error al eliminar empleado: {error}")

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

    def load_employees(self):
        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()

            query = "SELECT EmployeeID, LastName, FirstName, BirthDate, Photo, Notes FROM Employees"
            cursor.execute(query)
            employees = cursor.fetchall()

            self.tree.delete(*self.tree.get_children())
            for employee in employees:
                self.tree.insert("", "end", values=employee)

        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error al cargar empleados: {error}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def clear_entries(self):
        for entry in self.entries:
            entry.delete(0, tk.END)
        self.image_path = ""
        self.image_label.config(image="")


root = tk.Tk()
gui = EmployeeGUI(root)
root.mainloop()