import os
import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from tabulate import tabulate
from tkcalendar import DateEntry
from PIL import Image, ImageTk


# librerias
class DatabaseConnector:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None
        # clases objeto de conexion

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("Conexión establecida a la base de datos")
        except mysql.connector.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            messagebox.showerror("Error de conexión", f"Error al conectar a la base de datos: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada")

    def execute_procedure(self, procedure_name, *args):
        try:
            self.cursor.callproc(procedure_name, args)
            results = []
            for result in self.cursor.stored_results():
                rows = result.fetchall()
                if rows:
                    headers = [i[0] for i in result.description]
                    results.append((headers, rows))
            self.connection.commit()
            return results
        except mysql.connector.Error as e:
            self.connection.rollback()
            print(f"Error al ejecutar el procedimiento {procedure_name}: {e}")
            messagebox.showerror("Error", f"Error al ejecutar el procedimiento {procedure_name}: {e}")
            return None

class EmployeeApp(tk.Tk):
    def __init__(self, db_connector):
        super().__init__()
        self.db_connector = db_connector
        self.title("Gestión de Empleados")
        self.geometry("800x600")
        self.resizable(False, False)

        # Favicon
        favicon_path = os.path.join(os.path.dirname(__file__), "favicon.ico")
        if os.path.exists(favicon_path):
            self.iconbitmap(favicon_path)

        self._photo_path = None   # ruta original seleccionada
        self._photo_image = None  # referencia PhotoImage para preview

        self.create_widgets()

    def create_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Campos de entrada
        self.fields = ['EmployeeID', 'LastName', 'FirstName', 'BirthDate', 'Photo', 'Notes']
        self.entries = {}

        for i, field in enumerate(self.fields):
            ttk.Label(main_frame, text=field).grid(row=i, column=0, sticky=tk.W, padx=5, pady=2)
            if field == 'BirthDate':
                entry = DateEntry(main_frame, width=12, background='darkblue',
                                  foreground='white', borderwidth=2)
                entry.grid(row=i, column=1, sticky=tk.W, padx=5, pady=2)
            elif field == 'Photo':
                # Frame contenedor del campo Photo
                photo_frame = ttk.Frame(main_frame)
                photo_frame.grid(row=i, column=1, sticky=tk.W, padx=5, pady=2)

                entry = ttk.Entry(photo_frame, width=38, state='readonly')
                entry.pack(side=tk.LEFT)

                ttk.Button(photo_frame, text="Seleccionar foto",
                           command=self._select_photo).pack(side=tk.LEFT, padx=4)

                # Preview de la foto
                self._preview_label = ttk.Label(main_frame)
                self._preview_label.grid(row=i, column=2, rowspan=2, padx=10, pady=2)
            else:
                entry = ttk.Entry(main_frame, width=50)
                entry.grid(row=i, column=1, sticky=tk.W, padx=5, pady=2)
            self.entries[field] = entry

        # Botones
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=len(self.fields), column=0, columnspan=2, pady=10)

        ttk.Button(button_frame, text="Buscar", command=self.search_employee).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Insertar", command=self.insert_employee).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Actualizar", command=self.update_employee).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Borrar", command=self.delete_employee).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Mostrar Todos", command=self.show_all_employees).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Limpiar", command=self.clear_fields).pack(side=tk.LEFT, padx=5)

        # Área de resultados
        self.result_text = tk.Text(main_frame, height=20, width=80)
        self.result_text.grid(row=len(self.fields)+1, column=0, columnspan=2, pady=10)

    def _select_photo(self):
        """Abre un explorador de archivos, copia la imagen a img/ y muestra preview."""
        file_path = filedialog.askopenfilename(
            title="Seleccionar foto del empleado",
            filetypes=[("Imágenes", "*.jpg *.jpeg *.png *.bmp *.gif"), ("Todos", "*.*")]
        )
        if not file_path:
            return

        # Carpeta destino img/
        img_dir = os.path.join(os.path.dirname(__file__), "img")
        os.makedirs(img_dir, exist_ok=True)

        # Copiar con Pillow: convertir a JPEG estandarizado
        filename = os.path.basename(file_path)
        dest_path = os.path.join(img_dir, filename)
        img = Image.open(file_path).convert("RGB")
        img.save(dest_path, format="JPEG")

        # Guardar ruta relativa en el Entry
        self._photo_path = dest_path
        entry = self.entries['Photo']
        entry.config(state='normal')
        entry.delete(0, tk.END)
        entry.insert(0, f"img/{filename}")
        entry.config(state='readonly')

        # Preview 100x100
        preview = img.resize((100, 100), Image.LANCZOS)
        self._photo_image = ImageTk.PhotoImage(preview)
        self._preview_label.config(image=self._photo_image)

    def search_employee(self):
        employee_id = self.entries['EmployeeID'].get()
        if not employee_id:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un ID de empleado")
            return

        results = self.db_connector.execute_procedure('sp_GetEmployee', employee_id)
        if results:
            self.display_results(results)
        else:
            messagebox.showinfo("Información", "No se encontró el empleado")

    def insert_employee(self):
        values = [self.entries[field].get() for field in self.fields[1:]]  # Excluimos EmployeeID
        results = self.db_connector.execute_procedure('sp_InsertEmployee', *values)
        if results is not None:
            messagebox.showinfo("Éxito", "Empleado insertado correctamente")
            self.clear_fields()
            self.show_all_employees()

    def update_employee(self):
        values = [self.entries[field].get() for field in self.fields]
        results = self.db_connector.execute_procedure('sp_UpdateEmployee', *values)
        if results is not None:
            messagebox.showinfo("Éxito", "Empleado actualizado correctamente")
            self.show_all_employees()

    def delete_employee(self):
        employee_id = self.entries['EmployeeID'].get()
        if not employee_id:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un ID de empleado")
            return

        if messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este empleado?"):
            results = self.db_connector.execute_procedure('sp_DeleteEmployee', employee_id)
            if results is not None:
                messagebox.showinfo("Éxito", "Empleado eliminado correctamente")
                self.clear_fields()
                self.show_all_employees()

    def show_all_employees(self):
        results = self.db_connector.execute_procedure('sp_GetAllEmployees')
        if results:
            self.display_results(results)

    def clear_fields(self):
        for field, entry in self.entries.items():
            if field == 'Photo':
                entry.config(state='normal')
                entry.delete(0, tk.END)
                entry.config(state='readonly')
            else:
                entry.delete(0, tk.END)
        self._photo_path = None
        self._photo_image = None
        self._preview_label.config(image='')

    def display_results(self, results):
        self.result_text.delete(1.0, tk.END)
        for headers, rows in results:
            table = tabulate(rows, headers=headers, tablefmt="grid")
            self.result_text.insert(tk.END, table + "\n\n")

# Configuración de la base de datos
user = 'root'
password = 'base1234'
host = 'localhost'
database = 'Northwindx'

# Crear y conectar a la base de datos(los objetos de conexion se deben crear antes de la app(ojala los olviden))
db_connector = DatabaseConnector(host, user, password, database)
db_connector.connect()

# Crear y ejecutar la aplicación(esto la abre y la mantiene abierta)
app = EmployeeApp(db_connector)
app.mainloop()

# Cerrar la conexión a la base de datos al cerrar la aplicación(esto se debe hacer siempre)
db_connector.disconnect()