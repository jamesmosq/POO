"""
Solución - Ejercicio propuesto 02 - Registrar usuarios
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


def registrar(con, usuario, clave):
    usuario = usuario.strip().lower()
    if not usuario:
        raise ValueError("El usuario es obligatorio")
    if len(clave) < 8:
        raise ValueError("La clave debe tener al menos 8 caracteres")
    hash_texto = bcrypt.hashpw(clave.encode(), bcrypt.gensalt()).decode()
    with closing(con.cursor()) as cursor:
        try:
            cursor.execute("INSERT INTO ej_usuarios (usuario, hash) VALUES (%s, %s)", (usuario, hash_texto))
        except mysql.connector.IntegrityError as error:
            if error.errno == 1062:  # entrada duplicada en una columna UNIQUE
                raise ValueError("El usuario ya existe")
            raise
        con.commit()
        return cursor.lastrowid


# ----------------------------------------------------------------------
# Pruebas
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
