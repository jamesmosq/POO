import mysql.connector
import os


class DatabaseManager:
    def __init__(self, host, user, password, database):
        """
        Inicializa el manejador de base de datos
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        """
        Establece conexión con la base de datos

        Returns:
            bool: True si la conexión es exitosa, False en caso contrario
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                auth_plugin='mysql_native_password'  # Agregado para evitar problemas de autenticación
            )

            if self.connection.is_connected():
                print("✅ Conexión exitosa a la base de datos")

                # Información adicional de la conexión
                db_info = self.connection.get_server_info()
                print(f"📊 Versión del servidor MySQL: {db_info}")
                print(f"🏢 Base de datos conectada: {self.database}")

                return True
            else:
                print("❌ No se pudo establecer la conexión")
                return False

        except mysql.connector.Error as error:
            print(f"❌ Error de conexión MySQL: {error}")
            return False
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            return False

    def test_connection(self):
        """
        Prueba la conexión ejecutando una consulta simple

        Returns:
            bool: True si la prueba es exitosa
        """
        if not self.connection or not self.connection.is_connected():
            print("⚠️ No hay conexión activa")
            return False

        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            cursor.close()

            if result and result[0] == 1:
                print("✅ Test de conexión exitoso")
                return True
            else:
                print("❌ Test de conexión falló")
                return False

        except mysql.connector.Error as error:
            print(f"❌ Error en test de conexión: {error}")
            return False
        except Exception as e:
            print(f"❌ Error inesperado en test: {e}")
            return False

    def disconnect(self):
        """
        Cierra la conexión con la base de datos
        """
        try:
            if self.connection and self.connection.is_connected():
                self.connection.close()
                print("✅ Conexión cerrada correctamente")
            else:
                print("⚠️ No hay conexión activa para cerrar")

        except mysql.connector.Error as error:
            print(f"❌ Error al cerrar conexión: {error}")
        except Exception as e:
            print(f"❌ Error inesperado al cerrar: {e}")

    def get_connection_status(self):
        """
        Muestra el estado actual de la conexión
        """
        if self.connection and self.connection.is_connected():
            print("🟢 Estado: CONECTADO")
            print(f"🏢 Host: {self.host}")
            print(f"👤 Usuario: {self.user}")
            print(f"🗃️ Base de datos: {self.database}")
        else:
            print("🔴 Estado: DESCONECTADO")


def main():
    """
    Función principal para probar la conexión
    """
    print("=== PRUEBA DE CONEXIÓN A BASE DE DATOS ===\n")

    # Configuración de la conexión (puedes cambiar estos valores)
    HOST = 'localhost'
    USER = 'root'
    PASSWORD = 'base1234'  # Cambia por tu contraseña
    DATABASE = 'northwind'  # Cambia por tu base de datos

    # Crear el manejador de base de datos
    db_manager = DatabaseManager(HOST, USER, PASSWORD, DATABASE)

    try:
        print("🔄 Intentando conectar a la base de datos...")
        print(f"📡 Host: {HOST}")
        print(f"👤 Usuario: {USER}")
        print(f"🗃️ Base de datos: {DATABASE}")

        print("-" * 50)

        # Intentar conectar
        if db_manager.connect():
            print("\n🎉 ¡Conexión establecida exitosamente!")

            # Mostrar estado de la conexión
            print("\n--- Estado de la Conexión ---")
            db_manager.get_connection_status()

            # Hacer test adicional
            print("\n--- Test de Funcionalidad ---")
            db_manager.test_connection()

        else:
            print("\n💥 No se pudo establecer la conexión")
            print("\n🔧 Posibles soluciones:")
            print("   1. Verificar que MySQL esté ejecutándose")
            print("   2. Comprobar usuario y contraseña")
            print("   3. Verificar que la base de datos existe")
            print("   4. Revisar permisos del usuario")

    except KeyboardInterrupt:
        print("\n\n⏹️ Operación cancelada por el usuario")
    except Exception as e:
        print(f"\n💥 Error inesperado: {e}")
    finally:
        # Siempre intentar cerrar la conexión
        print("\n--- Cerrando Conexión ---")
        db_manager.disconnect()

        print("\n=== FIN DE LA PRUEBA ===")


# Función alternativa usando variables de entorno (más seguro)
def main_with_env():
    """
    Versión usando variables de entorno para mayor seguridad
    """
    print("=== PRUEBA CON VARIABLES DE ENTORNO ===\n")

    # Leer configuración desde variables de entorno
    HOST = os.getenv('DB_HOST', 'localhost')
    USER = os.getenv('DB_USER', 'root')
    PASSWORD = os.getenv('DB_PASSWORD', '')
    DATABASE = os.getenv('DB_NAME', 'northwind')

    if not PASSWORD:
        print("⚠️ Advertencia: No se encontró la variable DB_PASSWORD")
        print("💡 Para usar este método, configura las variables de entorno:")
        print("   export DB_HOST=localhost")
        print("   export DB_USER=root")
        print("   export DB_PASSWORD=tu_password")
        print("   export DB_NAME=tu_database")
        return

    db_manager = DatabaseManager(HOST, USER, PASSWORD, DATABASE)

    print("🔐 Usando configuración desde variables de entorno")
    if db_manager.connect():
        print("✅ Conexión exitosa con variables de entorno")
        db_manager.test_connection()

    db_manager.disconnect()


if __name__ == "__main__":
    main()
