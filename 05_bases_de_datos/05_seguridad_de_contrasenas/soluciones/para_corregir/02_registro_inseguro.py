"""
Solución - Ejercicio para corregir 02 - Registro inseguro

CORRECCIÓN 1 (decía que el usuario ya existía siempre): cursor.fetchone sin
paréntesis es el método, y un método siempre es "verdadero" en un if. Hay
que llamarlo: cursor.fetchone().

CORRECCIÓN 2 (la clave quedaba en texto plano): se guardaba la clave tal
cual. Si alguien obtiene una copia de la base de datos, vería todas las
claves. Se guarda el hash de bcrypt.
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


def registrar(con, usuario, clave):
    with closing(con.cursor(buffered=True)) as cursor:
        cursor.execute("SELECT id FROM ej_usuarios WHERE usuario = %s", (usuario,))
        if cursor.fetchone():  # CORRECCIÓN 1
            raise ValueError("El usuario ya existe")
        hash_texto = bcrypt.hashpw(clave.encode(), bcrypt.gensalt()).decode()  # CORRECCIÓN 2
        cursor.execute("INSERT INTO ej_usuarios (usuario, hash) VALUES (%s, %s)", (usuario, hash_texto))
        con.commit()


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    preparar(con)
    try:
        registrar(con, "prueba_ej_ana", "Secreta123")
        cursor = con.cursor(buffered=True)
        cursor.execute("SELECT hash FROM ej_usuarios WHERE usuario = 'prueba_ej_ana'")
        guardado = cursor.fetchone()[0]
        cursor.close()
        assert guardado != "Secreta123", "La clave quedó guardada en texto plano"
        assert bcrypt.checkpw(b"Secreta123", guardado.encode())

        try:
            registrar(con, "prueba_ej_ana", "OtraClave1")
            raise AssertionError("Un usuario repetido debe lanzar ValueError")
        except ValueError:
            pass
    finally:
        cursor = con.cursor()
        cursor.execute("DELETE FROM ej_usuarios WHERE usuario LIKE 'prueba_ej_%'")
        con.commit()
        cursor.close()
        con.close()
    print("Todas las pruebas pasaron")
