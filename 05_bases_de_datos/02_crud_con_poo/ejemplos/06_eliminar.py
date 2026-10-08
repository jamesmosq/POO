import mysql.connector


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
            print("Conexión establecida correctamente.")
        except mysql.connector.Error as error:
            print("Error de conexión:", error)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada correctamente.")

    def execute_query(self, query, data=None):
        try:
            if data:
                self.cursor.execute(query, data)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            return self.cursor.rowcount  # Retorna el número de filas afectadas
        except mysql.connector.Error as error:
            print("Error al ejecutar la consulta:", error)
            return 0

    def fetch_query(self, query, data=None):
        try:
            if data:
                self.cursor.execute(query, data)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except mysql.connector.Error as error:
            print("Error al ejecutar la consulta:", error)
            return None


class EmployeeDeleter:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def get_employee_by_id(self, employee_id):
        """Obtiene un empleado por ID para mostrar información antes de eliminar"""
        select_query = "SELECT EmployeeID, LastName, FirstName FROM Employees WHERE EmployeeID = %s"
        return self.db_manager.fetch_query(select_query, (employee_id,))

    def delete_employee(self, employee_id):
        """Elimina un empleado por su ID"""
        # Primero verificar si el empleado existe
        employee = self.get_employee_by_id(employee_id)

        if not employee:
            print(f"No se encontró empleado con ID: {employee_id}")
            return False

        # Mostrar información del empleado a eliminar
        emp_data = employee[0]
        print(f"Empleado a eliminar: ID {emp_data[0]} - {emp_data[2]} {emp_data[1]}")

        # Ejecutar eliminación
        delete_query = "DELETE FROM Employees WHERE EmployeeID = %s"
        rows_affected = self.db_manager.execute_query(delete_query, (employee_id,))

        if rows_affected > 0:
            print(f"Empleado con ID {employee_id} eliminado correctamente")
            return True
        else:
            print(f"No se pudo eliminar el empleado con ID {employee_id}")
            return False


# Configuración de la conexión
user = 'root'
password = 'base1234'
host = 'localhost'
database = 'Northwind'

db_manager = DatabaseManager(host, user, password, database)
employee_deleter = EmployeeDeleter(db_manager)

# ID del empleado a eliminar
employee_id_to_delete = 29  # Cambia este ID por el que quieras eliminar

try:
    db_manager.connect()
    employee_deleter.delete_employee(employee_id_to_delete)

except Exception as e:
    print("Error inesperado:", e)
finally:
    db_manager.disconnect()