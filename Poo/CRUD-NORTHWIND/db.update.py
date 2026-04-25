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


class EmployeeUpdater:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def get_employee_by_id(self, employee_id):
        """Obtiene un empleado por ID"""
        select_query = "SELECT EmployeeID, LastName, FirstName, BirthDate, Photo, Notes FROM Employees WHERE EmployeeID = %s"
        return self.db_manager.fetch_query(select_query, (employee_id,))

    def show_employee_info(self, employee_data):
        """Muestra información del empleado"""
        if employee_data:
            emp = employee_data[0]
            print(f"ID: {emp[0]}")
            print(f"Apellido: {emp[1]}")
            print(f"Nombre: {emp[2]}")
            print(f"Fecha Nacimiento: {emp[3]}")
            print(f"Foto: {emp[4]}")
            print(f"Notas: {emp[5]}")

    def update_employee(self, employee_id, last_name=None, first_name=None, birth_date=None, photo=None, notes=None):
        """Actualiza un empleado por su ID"""
        # Verificar si el empleado existe
        employee = self.get_employee_by_id(employee_id)

        if not employee:
            print(f"❌ No se encontró empleado con ID: {employee_id}")
            return False

        # Mostrar información actual
        print("📋 Información actual del empleado:")
        print("-" * 40)
        self.show_employee_info(employee)

        # Preparar la consulta de actualización
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
            print("⚠️ No se proporcionaron campos para actualizar")
            return False

        # Agregar el ID al final para la condición WHERE
        update_values.append(employee_id)

        # Construir la consulta
        update_query = f"UPDATE Employees SET {', '.join(update_fields)} WHERE EmployeeID = %s"

        # Ejecutar actualización
        rows_affected = self.db_manager.execute_query(update_query, tuple(update_values))

        if rows_affected > 0:
            print(f"\n✅ Empleado con ID {employee_id} actualizado correctamente")

            # Mostrar información actualizada
            updated_employee = self.get_employee_by_id(employee_id)
            print("\n📋 Información actualizada:")
            print("-" * 40)
            self.show_employee_info(updated_employee)
            return True
        else:
            print(f"❌ No se pudo actualizar el empleado con ID {employee_id}")
            return False


# Configuración de la conexión
user = 'root'
password = 'base1234'
host = 'localhost'
database = 'Northwind'

db_manager = DatabaseManager(host, user, password, database)
employee_updater = EmployeeUpdater(db_manager)

# Datos para actualizar
employee_id_to_update = 28  # aqui va el ID por el que se va a actualizar

# Nuevos datos (solo los que quieras cambiar, los demás déjalos como None), pilas con las restricciones de la base de datos cuando las tenga
new_last_name = 'Montes'  # Ejemplo: 'García'
new_first_name = 'Jaimito'  # Ejemplo: 'Carlos'
new_birth_date = None  # Ejemplo: '1985-05-15'
new_photo = None  # Ejemplo: 'carlos.jpg'
new_notes = 'Empleado actualizado via Python'  # Ejemplo de actualización

try:
    db_manager.connect()

    employee_updater.update_employee(
        employee_id_to_update,
        last_name=new_last_name,
        first_name=new_first_name,
        birth_date=new_birth_date,
        photo=new_photo,
        notes=new_notes
    )

except Exception as e:
    print("Error inesperado:", e)
finally:
    db_manager.disconnect()