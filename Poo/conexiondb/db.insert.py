import mysql.connector
user = 'root'
password = ''
host = 'localhost'
database = 'Northwind'


try:
    conexion = mysql.connector.connect(
        host=host,
        user=user,
        passwd=password,
        database=database
    )

    last_name = 'Rave'
    first_name = 'Alejandro'
    birth_date = '1999-01-01'
    photo = 'las-fotos-del-colegio-MR.jpg'
    notes = 'No le gusta madrugar, pero es muy puntual.'

    cursor = conexion.cursor()


    insert_query = """INSERT INTO Employees (LastName, FirstName, BirthDate, Photo, Notes)
                      VALUES (%s, %s, %s, %s, %s)"""

    empleado_data = (last_name, first_name, birth_date, photo, notes)

    cursor.execute(insert_query, empleado_data)

    # Confirmar la transacción
    conexion.commit()

    print("Nuevo empleado insertado correctamente.")

except mysql.connector.Error as error:
    print("Error al insertar el nuevo empleado:", error)

finally:
    if 'conexion' in locals() or 'conexion' in globals():
        conexion.close()