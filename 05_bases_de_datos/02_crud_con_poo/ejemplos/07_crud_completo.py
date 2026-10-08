import mysql.connector
from tabulate import tabulate


class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                auth_plugin='mysql_native_password'
            )
            self.cursor = self.connection.cursor()
            return True
        except mysql.connector.Error as error:
            print(f"Error de conexión: {error}")
            return False

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()

    def execute_query(self, query, data=None):
        try:
            if data:
                self.cursor.execute(query, data)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            return self.cursor.rowcount
        except mysql.connector.Error as error:
            print(f"Error al ejecutar consulta: {error}")
            return 0

    def fetch_query(self, query, data=None):
        try:
            if data:
                self.cursor.execute(query, data)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except mysql.connector.Error as error:
            print(f"Error al ejecutar consulta: {error}")
            return None

    def fetch_columns(self):
        if self.cursor:
            return [desc[0] for desc in self.cursor.description]
        return None


class EmployeeCRUD:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    # ========== READ ==========
    def read_all_employees(self):
        """Muestra todos los empleados"""
        query = """
        SELECT EmployeeID, LastName, FirstName, BirthDate 
        FROM Employees 
        ORDER BY LastName, FirstName
        """
        results = self.db_manager.fetch_query(query)
        if results:
            columns = self.db_manager.fetch_columns()
            print(f"\nTODOS LOS EMPLEADOS")
            print(f"Total: {len(results)} empleados")
            print("-" * 60)
            print(tabulate(results, headers=columns, tablefmt='grid'))
        else:
            print("No se encontraron empleados")

    def read_employee_by_id(self, employee_id):
        """Muestra un empleado específico"""
        query = "SELECT EmployeeID, LastName, FirstName, BirthDate, Photo, Notes FROM Employees WHERE EmployeeID = %s"
        results = self.db_manager.fetch_query(query, (employee_id,))

        if results:
            emp = results[0]
            print(f"\nEMPLEADO ID: {employee_id}")
            print("-" * 40)
            print(f"ID: {emp[0]}")
            print(f"Apellido: {emp[1]}")
            print(f"Nombre: {emp[2]}")
            print(f"Fecha Nacimiento: {emp[3]}")
            print(f"Foto: {emp[4]}")
            print(f"Notas: {emp[5]}")
            return True
        else:
            print(f"No se encontró empleado con ID: {employee_id}")
            return False

    # ========== CREATE ==========
    def create_employee(self, last_name, first_name, birth_date, photo="", notes=""):
        """Crea un nuevo empleado"""
        query = """
        INSERT INTO Employees (LastName, FirstName, BirthDate, Photo, Notes)
        VALUES (%s, %s, %s, %s, %s)
        """
        data = (last_name, first_name, birth_date, photo, notes)

        # Obtener el último ID antes de insertar
        self.db_manager.execute_query(query, data)

        # Obtener el ID del registro insertado
        last_id_query = "SELECT LAST_INSERT_ID()"
        result = self.db_manager.fetch_query(last_id_query)

        if result:
            new_id = result[0][0]
            print(f"Empleado creado exitosamente con ID: {new_id}")
            print(f"{first_name} {last_name}")
            return new_id
        else:
            print("Error al crear empleado")
            return None

    # ========== UPDATE ==========
    def update_employee(self, employee_id, last_name=None, first_name=None, birth_date=None, photo=None, notes=None):
        """Actualiza un empleado existente"""
        # Verificar si existe
        if not self.read_employee_by_id(employee_id):
            return False

        # Preparar campos a actualizar
        update_fields = []
        update_values = []

        if last_name is not None:
            update_fields.append("LastName = %s")
            update_values.append(last_name)
        if first_name is not None:
            update_fields.append("FirstName = %s")
            update_values.append(first_name)
        if birth_date is not None:
            update_fields.append("BirthDate = %s")
            update_values.append(birth_date)
        if photo is not None:
            update_fields.append("Photo = %s")
            update_values.append(photo)
        if notes is not None:
            update_fields.append("Notes = %s")
            update_values.append(notes)

        if not update_fields:
            print("No hay campos para actualizar")
            return False

        update_values.append(employee_id)
        query = f"UPDATE Employees SET {', '.join(update_fields)} WHERE EmployeeID = %s"

        rows_affected = self.db_manager.execute_query(query, tuple(update_values))

        if rows_affected > 0:
            print(f"\nEmpleado ID {employee_id} actualizado correctamente")
            self.read_employee_by_id(employee_id)  # Mostrar datos actualizados
            return True
        else:
            print(f"Error al actualizar empleado ID {employee_id}")
            return False

    # ========== DELETE ==========
    def delete_employee(self, employee_id):
        """Elimina un empleado"""
        # Mostrar información antes de eliminar
        if not self.read_employee_by_id(employee_id):
            return False

        query = "DELETE FROM Employees WHERE EmployeeID = %s"
        rows_affected = self.db_manager.execute_query(query, (employee_id,))

        if rows_affected > 0:
            print(f"\nEmpleado ID {employee_id} eliminado correctamente")
            return True
        else:
            print(f"Error al eliminar empleado ID {employee_id}")
            return False

    # ========== SEARCH ==========
    def search_employees(self, search_term):
        """Busca empleados por nombre o apellido"""
        query = """
        SELECT EmployeeID, LastName, FirstName, BirthDate 
        FROM Employees 
        WHERE LastName LIKE %s OR FirstName LIKE %s
        ORDER BY LastName, FirstName
        """
        pattern = f"%{search_term}%"
        results = self.db_manager.fetch_query(query, (pattern, pattern))

        if results:
            columns = self.db_manager.fetch_columns()
            print(f"\nBÚSQUEDA: '{search_term}'")
            print(f"Resultados: {len(results)} empleados")
            print("-" * 60)
            print(tabulate(results, headers=columns, tablefmt='grid'))
            return True
        else:
            print(f"No se encontraron empleados que contengan '{search_term}'")
            return False


class EmployeeMenu:
    def __init__(self):
        # Configuración de la base de datos
        self.host = 'localhost'
        self.user = 'root'
        self.password = 'base1234'
        self.database = 'Northwind'

        self.db_manager = DatabaseManager(self.host, self.user, self.password, self.database)
        self.employee_crud = EmployeeCRUD(self.db_manager)

    def show_menu(self):
        """Muestra el menú principal"""
        print("\n" + "=" * 50)
        print("SISTEMA CRUD - EMPLEADOS NORTHWIND")
        print("=" * 50)
        print("1⃣  Ver todos los empleados (READ)")
        print("2⃣  Buscar empleado por ID")
        print("3⃣  Crear nuevo empleado (CREATE)")
        print("4⃣  Actualizar empleado (UPDATE)")
        print("5⃣  Eliminar empleado (DELETE)")
        print("6⃣  Buscar empleados (SEARCH)")
        print("0⃣  Salir")
        print("-" * 50)

    def get_input(self, prompt, input_type=str):
        """Obtiene entrada del usuario con validación"""
        while True:
            try:
                value = input(prompt).strip()
                if input_type == int:
                    return int(value)
                elif input_type == str:
                    return value
            except ValueError:
                print("Por favor ingresa un valor válido")

    def run(self):
        """Ejecuta el menú principal"""
        print("Iniciando sistema...")

        if not self.db_manager.connect():
            print("No se pudo conectar a la base de datos")
            return

        print("Conexión establecida correctamente")

        try:
            while True:
                self.show_menu()
                opcion = self.get_input("Selecciona una opción: ", str)

                if opcion == "0":
                    print("¡Hasta luego!")
                    break

                elif opcion == "1":
                    self.employee_crud.read_all_employees()

                elif opcion == "2":
                    employee_id = self.get_input("Ingresa el ID del empleado: ", int)
                    self.employee_crud.read_employee_by_id(employee_id)

                elif opcion == "3":
                    print("\nCREAR NUEVO EMPLEADO")
                    print("-" * 30)
                    last_name = self.get_input("Apellido: ")
                    first_name = self.get_input("Nombre: ")
                    birth_date = self.get_input("Fecha nacimiento (YYYY-MM-DD): ")
                    photo = self.get_input("Foto (opcional): ")
                    notes = self.get_input("Notas (opcional): ")

                    self.employee_crud.create_employee(last_name, first_name, birth_date, photo, notes)

                elif opcion == "4":
                    employee_id = self.get_input("ID del empleado a actualizar: ", int)

                    if self.employee_crud.read_employee_by_id(employee_id):
                        print("\nACTUALIZAR EMPLEADO (Enter para mantener valor actual)")
                        print("-" * 50)

                        last_name = self.get_input("Nuevo apellido: ")
                        first_name = self.get_input("Nuevo nombre: ")
                        birth_date = self.get_input("Nueva fecha nacimiento (YYYY-MM-DD): ")
                        photo = self.get_input("Nueva foto: ")
                        notes = self.get_input("Nuevas notas: ")

                        # Convertir strings vacíos a None
                        last_name = last_name if last_name else None
                        first_name = first_name if first_name else None
                        birth_date = birth_date if birth_date else None
                        photo = photo if photo else None
                        notes = notes if notes else None

                        self.employee_crud.update_employee(employee_id, last_name, first_name, birth_date, photo, notes)

                elif opcion == "5":
                    employee_id = self.get_input("ID del empleado a eliminar: ", int)

                    # Confirmación
                    confirm = self.get_input("¿Estás seguro? (s/N): ")
                    if confirm.lower() in ['s', 'si', 'sí', 'yes', 'y']:
                        self.employee_crud.delete_employee(employee_id)
                    else:
                        print("Eliminación cancelada")

                elif opcion == "6":
                    search_term = self.get_input("Término de búsqueda (nombre o apellido): ")
                    self.employee_crud.search_employees(search_term)

                else:
                    print("Opción inválida. Intenta de nuevo.")

                input("\nPresiona Enter para continuar...")

        except KeyboardInterrupt:
            print("\n\n¡Hasta luego!")
        except Exception as e:
            print(f"\nError inesperado: {e}")
        finally:
            self.db_manager.disconnect()
            print("Conexión cerrada")


if __name__ == "__main__":
    menu = EmployeeMenu()
    menu.run()