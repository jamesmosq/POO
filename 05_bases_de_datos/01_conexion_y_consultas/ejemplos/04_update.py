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

    # Datos para actualizar
    employee_id = 6  # ID del empleado a actualizar
    nuevo_apellido = 'García'  # Nuevo apellido

    update_query = "UPDATE Employees SET LastName = %s WHERE EmployeeID = %s"
    cursor.execute(update_query, (nuevo_apellido, employee_id))

    # Confirmar la actualización
    conexion.commit()

    if cursor.rowcount > 0:
        print(f"Empleado con ID {employee_id} actualizado correctamente")
    else:
        print(f"No se encontró empleado con ID {employee_id}")

except mysql.connector.Error as error:
    print("Error al actualizar el empleado:", error)
    if 'conexion' in locals():
        conexion.rollback()
except Exception as e:
    print("Error inesperado:", e)
    if 'conexion' in locals():
        conexion.rollback()
finally:
    if 'conexion' in locals() or 'conexion' in globals():
        conexion.close()