"""
Ejercicio propuesto 02 - Registrar usuarios
Nivel: intermedio

La función preparar() (ya escrita) crea en tu base de datos la tabla
ej_usuarios si no existe:
    id, usuario (único), hash, intentos_fallidos, bloqueado

Requisitos. Escribe registrar(con, usuario, clave):
1. Normaliza el usuario: sin espacios a los lados y en minúscula.
2. Lanza ValueError si el usuario queda vacío o si la clave tiene menos de
   8 caracteres.
3. Guarda el hash de bcrypt (nunca la clave) y hace commit.
4. Si el usuario ya existe, lanza ValueError("El usuario ya existe").
   Puedes consultarlo antes, o atrapar el error de la base de datos: la
   columna es UNIQUE, y un duplicado lanza mysql.connector.IntegrityError
   (errno 1062).
5. Retorna el id del usuario nuevo.

Conceptos: registrar usuarios de forma segura, UNIQUE, IntegrityError.
"""
import os
from contextlib import closing

import bcrypt
import mysql.connector

CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "northwind"),
}


def preparar(con):
    """Crea la tabla que usa este ejercicio. No lo modifiques."""
    with closing(con.cursor()) as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ej_usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                usuario VARCHAR(50) NOT NULL UNIQUE,
                hash VARCHAR(100) NOT NULL,
                intentos_fallidos INT NOT NULL DEFAULT 0,
                bloqueado BOOLEAN NOT NULL DEFAULT FALSE
            )
        """)

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
def lanza_value_error(funcion, *argumentos):
    try:
        funcion(*argumentos)
    except ValueError:
        return True
    return False


if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    preparar(con)
    try:
        nuevo = registrar(con, "  Prueba_EJ_Ana ", "Secreta123")
        cursor = con.cursor(buffered=True)
        cursor.execute("SELECT id, usuario, hash FROM ej_usuarios WHERE id = %s", (nuevo,))
        id_usuario, usuario, guardado = cursor.fetchone()
        cursor.close()
        assert usuario == "prueba_ej_ana"
        assert guardado != "Secreta123" and "Secreta123" not in guardado, "Nunca se guarda la clave"
        assert bcrypt.checkpw(b"Secreta123", guardado.encode()), "Se debe guardar un hash de bcrypt"

        assert lanza_value_error(registrar, con, "PRUEBA_EJ_ANA", "OtraClave99"), "El usuario ya existe"
        assert lanza_value_error(registrar, con, "prueba_ej_luis", "corta")
        assert lanza_value_error(registrar, con, "   ", "Secreta123")
    finally:
        cursor = con.cursor()
        cursor.execute("DELETE FROM ej_usuarios WHERE usuario LIKE 'prueba_ej_%'")
        con.commit()
        cursor.close()
        con.close()
    print("Todas las pruebas pasaron")
