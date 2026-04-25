import mysql.connector
user = 'root'
password = 'base1234'
host = 'localhost'
database = 'northwind'
port = 3306
try:
    conexion = mysql.connector.connect(
        host=host,
        user=user,
        passwd = password,
        database=database,
    )
    print("Conexión exitosa")
except mysql.connector.Error as error:
    print("Error de conexión:", error)
