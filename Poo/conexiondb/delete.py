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

    # ID del empleado a eliminar
    employee_id_eliminar = 9

    # Primero verificamos si el empleado existe
    check_query = "SELECT COUNT(*) FROM Employees WHERE EmployeeID = %s"
    cursor.execute(check_query, (employee_id_eliminar,))
    if cursor.fetchone()[0] == 0:
        print(f"No existe empleado con ID {employee_id_eliminar}")
        exit()

    # Verificamos si tiene órdenes asociadas
    check_orders_query = "SELECT COUNT(*) FROM Orders WHERE EmployeeID = %s"
    cursor.execute(check_orders_query, (employee_id_eliminar,))
    num_orders = cursor.fetchone()[0]

    if num_orders > 0:
        print(f"El empleado tiene {num_orders} órdenes asociadas.")
        print("\nOpciones disponibles:")
        print("1. Transferir órdenes a otro empleado")
        print("2. Cancelar operación")

        opcion = input("\nSeleccione una opción (1-2): ")

        if opcion == "1":
            # Mostrar lista de empleados disponibles
            cursor.execute("""
                SELECT EmployeeID, CONCAT(FirstName, ' ', LastName) as Nombre 
                FROM Employees 
                WHERE EmployeeID != %s
            """, (employee_id_eliminar,))

            empleados_disponibles = cursor.fetchall()
            print("\nEmpleados disponibles para transferir órdenes:")
            for emp_id, nombre in empleados_disponibles:
                print(f"ID: {emp_id} - Nombre: {nombre}")

            nuevo_employee_id = input("\nIngrese el ID del empleado que recibirá las órdenes: ")

            # Verificar que el ID ingresado existe
            cursor.execute("SELECT COUNT(*) FROM Employees WHERE EmployeeID = %s", (nuevo_employee_id,))
            if cursor.fetchone()[0] > 0:
                # Transferir órdenes
                update_orders_query = "UPDATE Orders SET EmployeeID = %s WHERE EmployeeID = %s"
                cursor.execute(update_orders_query, (nuevo_employee_id, employee_id_eliminar))

                # Eliminar el empleado
                delete_employee_query = "DELETE FROM Employees WHERE EmployeeID = %s"
                cursor.execute(delete_employee_query, (employee_id_eliminar,))

                conexion.commit()
                print(f"\nSe transfirieron {num_orders} órdenes al empleado ID {nuevo_employee_id}")
                print(f"Empleado con ID {employee_id_eliminar} eliminado correctamente")
            else:
                print("ID de empleado inválido. Operación cancelada.")
        else:
            print("Operación cancelada.")
    else:
        # Si no tiene órdenes, podemos eliminar directamente
        delete_employee_query = "DELETE FROM Employees WHERE EmployeeID = %s"
        cursor.execute(delete_employee_query, (employee_id_eliminar,))
        conexion.commit()
        print(f"Empleado con ID {employee_id_eliminar} eliminado correctamente")

except mysql.connector.Error as error:
    print("Error en la operación de base de datos:", error)
    if 'conexion' in locals():
        conexion.rollback()
except Exception as e:
    print("Error inesperado:", e)
    if 'conexion' in locals():
        conexion.rollback()
finally:
    if 'conexion' in locals() or 'conexion' in globals():
        conexion.close()
        print("\nConexión cerrada")