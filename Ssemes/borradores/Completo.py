import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector


class NorthwindGUI:
    def __init__(self, master):
        self.master = master
        master.title("Northwind Database Manager")
        master.geometry("800x600")

        self.db_config = {
            "host": "localhost",
            "user": "root",
            "password": "",
            "database": "Northwind"
        }

        # Crear menú
        self.menu = tk.Menu(master)
        master.config(menu=self.menu)

        # Menú de tablas
        self.table_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Tablas", menu=self.table_menu)

        # Añadir opciones de tablas
        tables = ["Categories", "Customers", "Employees", "OrderDetails", "Orders", "Products", "Shippers", "Suppliers"]
        for table in tables:
            self.table_menu.add_command(label=table, command=lambda t=table: self.open_table_window(t))

        # Frame principal
        self.main_frame = tk.Frame(master)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Label de bienvenida
        tk.Label(self.main_frame, text="Bienvenido al gestor de la base de datos Northwind", font=("Arial", 16)).pack(
            pady=20)

    def open_table_window(self, table_name):
        window = tk.Toplevel(self.master)
        window.title(f"Gestionar {table_name}")
        window.geometry("800x600")

        frame = tk.Frame(window)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Obtener estructura de la tabla
        columns = self.get_table_structure(table_name)

        # Crear campos de entrada
        entries = []
        for i, col in enumerate(columns):
            tk.Label(frame, text=col).grid(row=i, column=0, sticky="e", padx=5, pady=5)
            entry = tk.Entry(frame, width=50)
            entry.grid(row=i, column=1, padx=5, pady=5)
            entries.append(entry)

        # Botones CRUD
        tk.Button(frame, text="Crear", command=lambda: self.create_record(table_name, columns, entries)).grid(
            row=len(columns), column=0, pady=10)
        tk.Button(frame, text="Leer", command=lambda: self.read_record(table_name, columns, entries)).grid(
            row=len(columns), column=1, pady=10)
        tk.Button(frame, text="Actualizar", command=lambda: self.update_record(table_name, columns, entries)).grid(
            row=len(columns) + 1, column=0, pady=10)
        tk.Button(frame, text="Eliminar", command=lambda: self.delete_record(table_name, columns, entries)).grid(
            row=len(columns) + 1, column=1, pady=10)

        # Campo de búsqueda por ID
        tk.Label(frame, text="Buscar por ID:").grid(row=len(columns) + 2, column=0, sticky="e", padx=5, pady=5)
        search_entry = tk.Entry(frame, width=20)
        search_entry.grid(row=len(columns) + 2, column=1, sticky="w", padx=5, pady=5)
        tk.Button(frame, text="Buscar",
                  command=lambda: self.search_by_id(table_name, columns, entries, search_entry.get())).grid(
            row=len(columns) + 2, column=1, sticky="e", padx=5, pady=5)

    def get_table_structure(self, table_name):
        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()
            cursor.execute(f"DESCRIBE {table_name}")
            return [column[0] for column in cursor.fetchall()]
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error al obtener la estructura de la tabla: {error}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def create_record(self, table_name, columns, entries):
        values = [entry.get() for entry in entries]
        query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})"

        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()
            cursor.execute(query, values)
            connection.commit()
            messagebox.showinfo("Éxito", "Registro creado correctamente")
            for entry in entries:
                entry.delete(0, tk.END)
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error al crear el registro: {error}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def read_record(self, table_name, columns, entries):
        id_value = entries[0].get()
        if not id_value:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un ID para leer")
            return

        query = f"SELECT * FROM {table_name} WHERE {columns[0]} = %s"

        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()
            cursor.execute(query, (id_value,))
            result = cursor.fetchone()
            if result:
                for i, value in enumerate(result):
                    entries[i].delete(0, tk.END)
                    entries[i].insert(0, str(value))
            else:
                messagebox.showinfo("Info", "No se encontró el registro")
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error al leer el registro: {error}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def update_record(self, table_name, columns, entries):
        values = [entry.get() for entry in entries]
        id_value = values[0]
        update_values = values[1:]
        query = f"UPDATE {table_name} SET {', '.join([f'{col} = %s' for col in columns[1:]])} WHERE {columns[0]} = %s"

        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()
            cursor.execute(query, update_values + [id_value])
            connection.commit()
            if cursor.rowcount > 0:
                messagebox.showinfo("Éxito", "Registro actualizado correctamente")
            else:
                messagebox.showinfo("Info", "No se encontró el registro para actualizar")
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error al actualizar el registro: {error}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def delete_record(self, table_name, columns, entries):
        id_value = entries[0].get()
        if not id_value:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un ID para eliminar")
            return

        query = f"DELETE FROM {table_name} WHERE {columns[0]} = %s"

        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()
            cursor.execute(query, (id_value,))
            connection.commit()
            if cursor.rowcount > 0:
                messagebox.showinfo("Éxito", "Registro eliminado correctamente")
                for entry in entries:
                    entry.delete(0, tk.END)
            else:
                messagebox.showinfo("Info", "No se encontró el registro para eliminar")
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error al eliminar el registro: {error}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def search_by_id(self, table_name, columns, entries, id_value):
        if not id_value:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un ID para buscar")
            return

        query = f"SELECT * FROM {table_name} WHERE {columns[0]} = %s"

        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()
            cursor.execute(query, (id_value,))
            result = cursor.fetchone()
            if result:
                for i, value in enumerate(result):
                    entries[i].delete(0, tk.END)
                    entries[i].insert(0, str(value))
            else:
                messagebox.showinfo("Info", "No se encontró el registro")
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error al buscar el registro: {error}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


root = tk.Tk()
gui = NorthwindGUI(root)
root.mainloop()