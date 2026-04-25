import mysql.connector
user = 'root'
password = 'base1234'
host = 'localhost'
database = 'Northwind'

try:

    conexion = mysql.connector.connect(
        host=host,
        user=user,
        passwd=password,
        database=database
    )
    cursor = conexion.cursor()

    select_query = "SELECT  EmployeeID, LastName, firstname FROM Employees"
    cursor.execute(select_query) # esto ejecuta la consulta

    empleados = cursor.fetchall() # eso ttra los resultados de la consulta

    for empleado in empleados:
        print(empleado)

except mysql.connector.Error as error:
    print("Error al obtener los empleados:", error)
except Exception as e:
    print("Error inesperado:", e)
finally:
    # Cerrar la conexión
    if 'conexion' in locals() or 'conexion' in globals():
        conexion.close()
