import os
import mysql.connector
from contextlib import contextmanager
from typing import List, Tuple, Optional
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DatabaseConfig:
    """Configuración de base de datos usando variables de entorno"""

    def __init__(self):
        self.host = os.getenv('DB_HOST', 'localhost')
        self.user = os.getenv('DB_USER', 'root')
        self.password = os.getenv('DB_PASSWORD', 'base1234')  # Valor por defecto para testing
        self.database = os.getenv('DB_NAME', 'Northwind')
        self.port = int(os.getenv('DB_PORT', '3306'))

    def get_connection_params(self) -> dict:
        """Retorna parámetros de conexión con configuraciones de autenticación"""
        return {
            'host': self.host,
            'user': self.user,
            'password': self.password,
            'database': self.database,
            'port': self.port,
            'auth_plugin': 'mysql_native_password',  # Forzar plugin de autenticación
            'autocommit': True,
            'charset': 'utf8mb4',
            'collation': 'utf8mb4_unicode_ci',
            'use_unicode': True,
            'sql_mode': 'TRADITIONAL',
            'connect_timeout': 60,
            'buffered': True
        }


class DatabaseManager:
    """Manejador de conexiones a base de datos con múltiples estrategias de conexión"""

    def __init__(self, config: DatabaseConfig):
        self.config = config

    def test_connection(self) -> bool:
        """Prueba la conexión a la base de datos"""
        try:
            with self.get_connection() as conexion:
                cursor = conexion.cursor()
                cursor.execute("SELECT 1")
                cursor.fetchone()
                logger.info("Conexión a base de datos exitosa")
                return True
        except Exception as e:
            logger.error(f"Error al probar conexión: {e}")
            return False

    @contextmanager
    def get_connection(self):
        """Context manager para manejo seguro de conexiones con múltiples estrategias"""
        conexion = None

        # Lista de configuraciones de autenticación para probar
        auth_strategies = [
            {'auth_plugin': 'mysql_native_password'},
            {'auth_plugin': 'sha256_password'},
            {'auth_plugin': 'caching_sha2_password'},
            {}  # Sin especificar plugin
        ]

        for i, auth_config in enumerate(auth_strategies):
            try:
                connection_params = self.config.get_connection_params()
                connection_params.update(auth_config)

                logger.info(f"Intentando conexión con estrategia {i + 1}: {auth_config}")
                conexion = mysql.connector.connect(**connection_params)

                if conexion.is_connected():
                    logger.info(f"Conexión exitosa con estrategia {i + 1}")
                    yield conexion
                    return

            except mysql.connector.Error as error:
                logger.warning(f"Estrategia {i + 1} falló: {error}")
                if conexion and conexion.is_connected():
                    conexion.close()
                conexion = None
                continue
            except Exception as e:
                logger.warning(f"Error inesperado en estrategia {i + 1}: {e}")
                if conexion and conexion.is_connected():
                    conexion.close()
                conexion = None
                continue
            finally:
                # Solo cerrar si no se hizo yield (conexión fallida)
                if conexion and conexion.is_connected() and 'yield' not in locals():
                    conexion.close()

        # Si llegamos aquí, todas las estrategias fallaron
        raise mysql.connector.Error("No se pudo establecer conexión con ninguna estrategia de autenticación")


class AlternativeDatabaseManager:
    """Manejador alternativo usando PyMySQL como fallback"""

    def __init__(self, config: DatabaseConfig):
        self.config = config

    @contextmanager
    def get_connection(self):
        """Context manager usando PyMySQL como alternativa"""
        try:
            import pymysql
            conexion = pymysql.connect(
                host=self.config.host,
                user=self.config.user,
                password=self.config.password,
                database=self.config.database,
                port=self.config.port,
                charset='utf8mb4'
            )
            logger.info("Conexión exitosa usando PyMySQL")
            yield conexion
        except ImportError:
            raise Exception("PyMySQL no está instalado. Instala con: pip install PyMySQL")
        except Exception as e:
            logger.error(f"Error con PyMySQL: {e}")
            raise
        finally:
            if 'conexion' in locals() and conexion:
                conexion.close()
                logger.info("Conexión PyMySQL cerrada")


class EmployeeRepository:
    """Repositorio para operaciones CRUD de empleados"""

    def __init__(self, db_manager):
        self.db_manager = db_manager

    def get_all_employees(self) -> List[Tuple]:
        """Obtiene todos los empleados con manejo robusto de errores"""
        query = """
        SELECT EmployeeID, LastName, FirstName 
        FROM Employees 
        ORDER BY LastName, FirstName
        """

        try:
            with self.db_manager.get_connection() as conexion:
                cursor = conexion.cursor()
                cursor.execute(query)
                empleados = cursor.fetchall()
                cursor.close()
                logger.info(f"Se obtuvieron {len(empleados)} empleados")
                return empleados

        except mysql.connector.Error as error:
            logger.error(f"Error MySQL al obtener empleados: {error}")
            raise
        except Exception as e:
            logger.error(f"Error inesperado al obtener empleados: {e}")
            raise

    def get_employee_by_id(self, employee_id: int) -> Optional[Tuple]:
        """Obtiene un empleado por su ID"""
        query = """
        SELECT EmployeeID, LastName, FirstName 
        FROM Employees 
        WHERE EmployeeID = %s
        """

        try:
            with self.db_manager.get_connection() as conexion:
                cursor = conexion.cursor()
                cursor.execute(query, (employee_id,))
                empleado = cursor.fetchone()
                cursor.close()
                return empleado

        except Exception as error:
            logger.error(f"Error al obtener empleado {employee_id}: {error}")
            raise


class EmployeeService:
    """Servicio para lógica de negocio de empleados"""

    def __init__(self, repository: EmployeeRepository):
        self.repository = repository

    def list_employees(self) -> List[dict]:
        """Lista empleados en formato más amigable"""
        empleados_raw = self.repository.get_all_employees()

        empleados = []
        for emp in empleados_raw:
            empleados.append({
                'id': emp[0],
                'apellido': emp[1],
                'nombre': emp[2],
                'nombre_completo': f"{emp[2]} {emp[1]}"
            })

        return empleados

    def find_employee(self, employee_id: int) -> Optional[dict]:
        """Busca un empleado específico"""
        empleado_raw = self.repository.get_employee_by_id(employee_id)

        if empleado_raw:
            return {
                'id': empleado_raw[0],
                'apellido': empleado_raw[1],
                'nombre': empleado_raw[2],
                'nombre_completo': f"{empleado_raw[2]} {empleado_raw[1]}"
            }
        return None


def main():
    """Función principal con manejo de múltiples estrategias de conexión"""

    print("=== SISTEMA DE GESTIÓN DE EMPLEADOS ===")
    config = DatabaseConfig()

    # Intentar con mysql-connector-python primero
    try:
        print("Intentando conexión con mysql-connector-python...")
        db_manager = DatabaseManager(config)

        # Probar conexión
        if db_manager.test_connection():
            print("✅ Conexión exitosa con mysql-connector-python")
        else:
            raise Exception("Test de conexión falló")

    except Exception as e:
        print(f"❌ mysql-connector-python falló: {e}")
        print("Intentando con PyMySQL como alternativa...")

        try:
            db_manager = AlternativeDatabaseManager(config)
            print("✅ Usando PyMySQL como alternativa")
        except Exception as e2:
            print(f"❌ PyMySQL también falló: {e2}")
            print("\n=== SOLUCIONES RECOMENDADAS ===")
            print("1. Instalar PyMySQL: pip install PyMySQL")
            print("2. Actualizar mysql-connector-python: pip install --upgrade mysql-connector-python")
            print("3. Verificar configuración de MySQL server")
            print("4. Cambiar método de autenticación en MySQL")
            return

    # Continuar con la lógica de negocio
    try:
        employee_repo = EmployeeRepository(db_manager)
        employee_service = EmployeeService(employee_repo)

        print("\n=== LISTA DE EMPLEADOS ===")
        empleados = employee_service.list_employees()

        if empleados:
            for empleado in empleados:
                print(f"ID: {empleado['id']:<3} | {empleado['nombre_completo']}")
            print(f"\nTotal de empleados: {len(empleados)}")
        else:
            print("No se encontraron empleados en la base de datos")

        # Buscar un empleado específico
        print("\n=== BÚSQUEDA DE EMPLEADO ===")
        empleado_especifico = employee_service.find_employee(1)
        if empleado_especifico:
            print(f"Empleado encontrado: {empleado_especifico['nombre_completo']}")
        else:
            print("Empleado con ID 1 no encontrado")

    except Exception as e:
        logger.error(f"Error en la aplicación: {e}")
        print(f"❌ Ocurrió un error: {e}")
        print("Consulta los logs para más detalles.")


if __name__ == "__main__":
    main()