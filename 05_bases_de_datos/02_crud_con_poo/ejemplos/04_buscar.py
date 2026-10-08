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
            print("Conexión establecida correctamente.")
        except mysql.connector.Error as error:
            print("Error de conexión:", error)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada correctamente.")

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

    def fetch_columns(self):
        if self.cursor:
            return [desc[0] for desc in self.cursor.description]
        else:
            return None

class EmployeeSearcher:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def search_by_name(self, search_term):
        """Busca empleados por nombre o apellido"""
        search_query = """
        SELECT EmployeeID, LastName, FirstName, BirthDate 
        FROM Employees 
        WHERE LastName LIKE %s OR FirstName LIKE %s
        ORDER BY LastName, FirstName
        """
        search_pattern = f"%{search_term}%"
        return self.db_manager.fetch_query(search_query, (search_pattern, search_pattern))

    def search_by_lastname(self, lastname):
        """Busca empleados por apellido específico"""
        search_query = """
        SELECT EmployeeID, LastName, FirstName, BirthDate 
        FROM Employees 
        WHERE LastName LIKE %s
        ORDER BY FirstName
        """
        search_pattern = f"%{lastname}%"
        return self.db_manager.fetch_query(search_query, (search_pattern,))

    def search_by_firstname(self, firstname):
        """Busca empleados por nombre específico"""
        search_query = """
        SELECT EmployeeID, LastName, FirstName, BirthDate 
        FROM Employees 
        WHERE FirstName LIKE %s
        ORDER BY LastName
        """
        search_pattern = f"%{firstname}%"
        return self.db_manager.fetch_query(search_query, (search_pattern,))

    def search_by_birth_year(self, year):
        """Busca empleados por año de nacimiento"""
        search_query = """
        SELECT EmployeeID, LastName, FirstName, BirthDate 
        FROM Employees 
        WHERE YEAR(BirthDate) = %s
        ORDER BY BirthDate
        """
        return self.db_manager.fetch_query(search_query, (year,))

    def search_by_id_range(self, start_id, end_id):
        """Busca empleados en un rango de IDs"""
        search_query = """
        SELECT EmployeeID, LastName, FirstName, BirthDate 
        FROM Employees 
        WHERE EmployeeID BETWEEN %s AND %s
        ORDER BY EmployeeID
        """
        return self.db_manager.fetch_query(search_query, (start_id, end_id))

    def display_results(self, results, search_description):
        """Muestra los resultados de búsqueda en formato tabla"""
        if results:
            columns = self.db_manager.fetch_columns()
            print(f"\n{search_description}")
            print(f"Resultados encontrados: {len(results)}")
            print("-" * 60)
            print(tabulate(results, headers=columns, tablefmt='grid'))
        else:
            print(f"\n{search_description}")
            print("No se encontraron resultados.")

# Configuración de la conexión
user = 'root'
password = 'base1234'
host = 'localhost'
database = 'Northwind'

db_manager = DatabaseManager(host, user, password, database)
employee_searcher = EmployeeSearcher(db_manager)

try:
    db_manager.connect()

    # Búsqueda por nombre (busca en nombre y apellido)
    search_term = "an"  # Cambiar por el término que quieras buscar
    results = employee_searcher.search_by_name(search_term)
    employee_searcher.display_results(results, f"Búsqueda por nombre que contenga '{search_term}'")

    # Búsqueda por apellido específico
    lastname = "Pérez"  # Cambiar por el apellido que quieras buscar
    results = employee_searcher.search_by_lastname(lastname)
    employee_searcher.display_results(results, f"Búsqueda por apellido que contenga '{lastname}'")

    # Búsqueda por nombre específico
    firstname = "xxxx"  # Cambiar por el nombre que quieras buscar
    results = employee_searcher.search_by_firstname(firstname)
    employee_searcher.display_results(results, f"Búsqueda por nombre que contenga '{firstname}'")

    # Búsqueda por año de nacimiento
    birth_year = 1963  # Cambiar por el año que quieras buscar
    results = employee_searcher.search_by_birth_year(birth_year)
    employee_searcher.display_results(results, f"Empleados nacidos en {birth_year}")

    # Búsqueda por rango de IDs
    start_id = 1
    end_id = 5
    results = employee_searcher.search_by_id_range(start_id, end_id)
    employee_searcher.display_results(results, f"Empleados con ID entre {start_id} y {end_id}")

except Exception as e:
    print("Error inesperado:", e)
finally:
    db_manager.disconnect()