import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector


class NorthwindGUI:
    def __init__(self, master):
        self.master = master
        master.title("Northwind Database Manager")
        master.geometry("1000x700")

        self.db_config = {
            "host": "localhost",
            "user": "root",
            "password": "",
            "database": "Northwind"
        }

        self.create_menu()
        self.create_main_frame()

    def create_menu(self):
        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)

        self.table_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Tablas", menu=self.table_menu)

        tables = ["Categories", "Customers", "Employees", "OrderDetails", "Orders", "Products", "Shippers", "Suppliers"]
        for table in tables:
            self.table_menu.add_command(label=table, command=lambda t=table: self.open_table_window(t))

    def create_main_frame(self):
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        welcome_label = tk.Label(self.main_frame, text="Bienvenido al gestor de la base de datos Northwind",
                                 font=("Arial", 18, "bold"))
        welcome_label.pack(pady=30)

        instruction_label = tk.Label(self.main_frame, text="Seleccione una tabla del menú 'Tablas' para comenzar",
                                     font=("Arial", 12))
        instruction_label.pack(pady=10)

    def open_table_window(self, table_name):
        window = tk.Toplevel(self.master)
        window.title(f"Gestionar {table_name}")
        window.geometry("1000x700+100+100")

        main_frame = tk.Frame(window, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        title_label = tk.Label(main_frame, text=f"Tabla: {table_name}", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        columns = self.get_table_structure(table_name)

        left_frame = tk.Frame(main_frame)
        left_frame.grid(row=1, column=0, sticky="nsew", padx=(0, 10))

        right_frame = tk.Frame(main_frame)
        right_frame.grid(row=1, column=1, sticky="nsew", padx=(10, 0))

        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

        entries = self.create_entry_fields(left_frame, columns)
        self.create_buttons(right_frame, table_name, columns, entries)
        self.create_search_field(right_frame, table_name, columns, entries)

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

    def create_entry_fields(self, parent, columns):
        entries = []
        for i, col in enumerate(columns):
            tk.Label(parent, text=col, font=("Arial", 10, "bold")).grid(row=i, column=0, sticky="e", padx=5, pady=5)
            entry = tk.Entry(parent, width=50)
            entry.grid(row=i, column=1, padx=5, pady=5)
            entries.append(entry)
        return entries

    def create_buttons(self, parent, table_name, columns, entries):
        button_frame = tk.Frame(parent)
        button_frame.pack(pady=20)

        buttons = [
            ("Crear", lambda: self.create_record(table_name, columns, entries)),
            ("Leer", lambda: self.read_record(table_name, columns, entries)),
            ("Actualizar", lambda: self.update_record(table_name, columns, entries)),
            ("Eliminar", lambda: self.delete_record(table_name, columns, entries))
        ]

        for text, command in buttons:
            tk.Button(button_frame, text=text, command=command, width=10).pack(side=tk.LEFT, padx=5)

    def create_search_field(self, parent, table_name, columns, entries):
        search_frame = tk.Frame(parent)
        search_frame.pack(pady=20)

        tk.Label(search_frame, text="Buscar por ID:", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
        search_entry = tk.Entry(search_frame, width=20)
        search_entry.pack(side=tk.LEFT, padx=5)
        tk.Button(search_frame, text="Buscar",
                  command=lambda: self.search_by_id(table_name, columns, entries, search_entry.get())).pack(
            side=tk.LEFT, padx=5)

    def create_record(self, table_name, columns, entries):
        values = [entry.get() for entry in entries]
        query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})"

        self.execute_query(query, values, "Registro creado correctamente", "Error al crear el registro")
        for entry in entries:
            entry.delete(0, tk.END)

    def read_record(self, table_name, columns, entries):
        id_value = entries[0].get()
        if not id_value:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un ID para leer")
            return

        query = f"SELECT * FROM {table_name} WHERE {columns[0]} = %s"
        self.execute_query(query, (id_value,), "Registro leído correctamente", "Error al leer el registro",
                           self.populate_entries, entries)

    def update_record(self, table_name, columns, entries):
        values = [entry.get() for entry in entries]
        id_value = values[0]
        update_values = values[1:]
        query = f"UPDATE {table_name} SET {', '.join([f'{col} = %s' for col in columns[1:]])} WHERE {columns[0]} = %s"

        self.execute_query(query, update_values + [id_value], "Registro actualizado correctamente",
                           "Error al actualizar el registro")

    def delete_record(self, table_name, columns, entries):
        id_value = entries[0].get()
        if not id_value:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un ID para eliminar")
            return

        query = f"DELETE FROM {table_name} WHERE {columns[0]} = %s"
        self.execute_query(query, (id_value,), "Registro eliminado correctamente", "Error al eliminar el registro")
        for entry in entries:
            entry.delete(0, tk.END)

    def search_by_id(self, table_name, columns, entries, id_value):
        if not id_value:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un ID para buscar")
            return

        query = f"SELECT * FROM {table_name} WHERE {columns[0]} = %s"
        self.execute_query(query, (id_value,), "Registro encontrado", "Error al buscar el registro",
                           self.populate_entries, entries)

    def execute_query(self, query, values, success_message, error_message, callback=None, callback_args=None):
        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()
            cursor.execute(query, values)

            if callback:
                result = cursor.fetchone()
                if result:
                    callback(callback_args, result)
                    messagebox.showinfo("Éxito", success_message)
                else:
                    messagebox.showinfo("Info", "No se encontró el registro")
            else:
                connection.commit()
                if cursor.rowcount > 0:
                    messagebox.showinfo("Éxito", success_message)
                else:
                    messagebox.showinfo("Info", "No se encontró el registro para realizar la operación")

        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"{error_message}: {error}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def populate_entries(self, entries, values):
        for entry, value in zip(entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, str(value))


root = tk.Tk()
gui = NorthwindGUI(root)
root.mainloop()
