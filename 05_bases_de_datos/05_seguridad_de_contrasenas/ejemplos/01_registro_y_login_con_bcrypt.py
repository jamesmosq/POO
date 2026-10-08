import mysql.connector
from mysql.connector import Error
import bcrypt


def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',  # usuario de MySQL
            password='',  # contraseña, recuerda que normlamente es ""
            database='gestion_u'
        )
        if conexion.is_connected():
            print("Conexión exitosa a MySQL")
            return conexion
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None


def crear_usuario(conexion, nombre, apellido, usuario, contrasena):
    try:
        cursor = conexion.cursor()

        # Verificar si el usuario ya existe
        cursor.execute("SELECT * FROM usuarios WHERE usuario = %s", (usuario,))
        if cursor.fetchone():
            print("Error: El nombre de usuario ya existe.")
            return

        # Hashear la contraseña
        sal = bcrypt.gensalt()
        contrasena_hasheada = bcrypt.hashpw(contrasena.encode('utf-8'), sal)

        query = """INSERT INTO usuarios (nombre, apellido, usuario, contrasena) 
                   VALUES (%s, %s, %s, %s)"""
        valores = (nombre, apellido, usuario, contrasena_hasheada)
        cursor.execute(query, valores)
        conexion.commit()
        print("Usuario creado exitosamente")
    except Error as e:
        print(f"Error al crear usuario: {e}")


def obtener_usuarios(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, apellido, usuario FROM usuarios")
        usuarios = cursor.fetchall()
        if not usuarios:
            print("No hay usuarios registrados.")
        else:
            for usuario in usuarios:
                print(f"ID: {usuario[0]}, Nombre: {usuario[1]}, Apellido: {usuario[2]}, Usuario: {usuario[3]}")
    except Error as e:
        print(f"Error al obtener usuarios: {e}")


def iniciar_sesion(conexion):
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre, apellido, contrasena FROM usuarios WHERE usuario = %s", (usuario,))
        resultado = cursor.fetchone()

        if resultado:
            nombre, apellido, contrasena_hasheada = resultado
            if bcrypt.checkpw(contrasena.encode('utf-8'), contrasena_hasheada.encode('utf-8')):
                print(f"Bienvenido, {nombre} {apellido}!")
                return True
            else:
                print("Contraseña incorrecta.")
        else:
            print("Usuario no encontrado.")
        return False
    except Error as e:
        print(f"Error al iniciar sesión: {e}")
        return False


def main():
    conexion = crear_conexion()
    if conexion is not None:
        while True:
            print("\n1. Crear usuario")
            print("2. Ver usuarios")
            print("3. Iniciar sesión")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                usuario = input("Usuario: ")
                contrasena = input("Contraseña: ")
                crear_usuario(conexion, nombre, apellido, usuario, contrasena)
            elif opcion == '2':
                obtener_usuarios(conexion)
            elif opcion == '3':
                iniciar_sesion(conexion)
            elif opcion == '4':
                break
            else:
                print("Opción no válida")

        conexion.close()


if __name__ == "__main__":
    main()