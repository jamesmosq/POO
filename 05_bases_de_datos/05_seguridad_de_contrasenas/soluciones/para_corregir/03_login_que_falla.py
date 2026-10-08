"""
Solución - Ejercicio para corregir 03 - Login que falla

CORRECCIÓN 1 (ValueError: Invalid salt): los argumentos de checkpw estaban
al revés. Primero va la clave escrita y después el hash guardado:
bcrypt.checkpw(clave, hash).

CORRECCIÓN 2 (TypeError: 'NoneType' object is not subscriptable): si el
usuario no existe, fetchone() retorna None. Hay que retornar False en ese
caso, igual que con una clave incorrecta.
"""

import os
from contextlib import closing

import bcrypt
import mysql.connector

CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "base1234"),
    "database": os.getenv("DB_NAME", "northwind"),
}


def preparar(con):
    """Crea la tabla que usa este ejercicio. Este código está bien."""
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


def crear_usuario(con, usuario, clave):
    """Registra un usuario con su hash. Este código está bien."""
    hash_texto = bcrypt.hashpw(clave.encode(), bcrypt.gensalt()).decode()
    with closing(con.cursor()) as cursor:
        cursor.execute("INSERT INTO ej_usuarios (usuario, hash) VALUES (%s, %s)", (usuario, hash_texto))
    con.commit()


def iniciar_sesion(con, usuario, clave):
    with closing(con.cursor(buffered=True)) as cursor:
        cursor.execute("SELECT hash FROM ej_usuarios WHERE usuario = %s", (usuario,))
        fila = cursor.fetchone()
    if fila is None:  # CORRECCIÓN 2
        return False
    return bcrypt.checkpw(clave.encode(), fila[0].encode())  # CORRECCIÓN 1


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    preparar(con)
    try:
        crear_usuario(con, "prueba_ej_ana", "Secreta123")
        assert iniciar_sesion(con, "prueba_ej_ana", "Secreta123") is True
        assert iniciar_sesion(con, "prueba_ej_ana", "mala") is False
        assert iniciar_sesion(con, "prueba_ej_nadie", "Secreta123") is False
    finally:
        cursor = con.cursor()
        cursor.execute("DELETE FROM ej_usuarios WHERE usuario LIKE 'prueba_ej_%'")
        con.commit()
        cursor.close()
        con.close()
    print("Todas las pruebas pasaron")
