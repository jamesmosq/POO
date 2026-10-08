"""
Ejercicio para corregir 03 - Login que falla
Nivel: intermedio
Errores a encontrar: 2

Qué debería hacer el programa:
    iniciar_sesion(con, usuario, clave) retorna True si la clave es
    correcta y False en cualquier otro caso, incluido un usuario que no
    existe (sin lanzar errores).

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
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
    return bcrypt.checkpw(fila[0].encode(), clave.encode())


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
