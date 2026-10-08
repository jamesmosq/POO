"""
Solución - Ejercicio propuesto 03 - Inicio de sesión con bloqueo
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

MAXIMO_INTENTOS = 3


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


def crear_usuario(con, usuario, clave):
    """Registra un usuario con su hash. No lo modifiques."""
    hash_texto = bcrypt.hashpw(clave.encode(), bcrypt.gensalt()).decode()
    with closing(con.cursor()) as cursor:
        cursor.execute("INSERT INTO ej_usuarios (usuario, hash) VALUES (%s, %s)", (usuario, hash_texto))
    con.commit()


def iniciar_sesion(con, usuario, clave):
    with closing(con.cursor(buffered=True)) as cursor:
        cursor.execute(
            "SELECT hash, intentos_fallidos, bloqueado FROM ej_usuarios WHERE usuario = %s",
            (usuario,),
        )
        fila = cursor.fetchone()
        if fila is None:
            return False  # misma respuesta que una clave incorrecta
        hash_guardado, intentos, bloqueado = fila
        if bloqueado:
            return False

        if bcrypt.checkpw(clave.encode(), hash_guardado.encode()):
            cursor.execute("UPDATE ej_usuarios SET intentos_fallidos = 0 WHERE usuario = %s", (usuario,))
            con.commit()
            return True

        intentos += 1
        cursor.execute(
            "UPDATE ej_usuarios SET intentos_fallidos = %s, bloqueado = %s WHERE usuario = %s",
            (intentos, intentos >= MAXIMO_INTENTOS, usuario),
        )
        con.commit()
        return False


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
def estado(usuario):
    otra = mysql.connector.connect(**CONFIG)
    cursor = otra.cursor(buffered=True)
    cursor.execute("SELECT intentos_fallidos, bloqueado FROM ej_usuarios WHERE usuario = %s", (usuario,))
    fila = cursor.fetchone()
    cursor.close()
    otra.close()
    return int(fila[0]), bool(fila[1])


if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    preparar(con)
    try:
        crear_usuario(con, "prueba_ej_ana", "Secreta123")
        crear_usuario(con, "prueba_ej_luis", "Secreta123")

        assert iniciar_sesion(con, "prueba_ej_ana", "Secreta123") is True
        assert iniciar_sesion(con, "prueba_ej_nadie", "Secreta123") is False

        assert iniciar_sesion(con, "prueba_ej_ana", "mala") is False
        assert estado("prueba_ej_ana") == (1, False), "Los intentos fallidos deben guardarse (commit)"
        assert iniciar_sesion(con, "prueba_ej_ana", "Secreta123") is True
        assert estado("prueba_ej_ana") == (0, False), "Un ingreso correcto reinicia los intentos"

        for _ in range(MAXIMO_INTENTOS):
            assert iniciar_sesion(con, "prueba_ej_luis", "mala") is False
        assert estado("prueba_ej_luis") == (3, True), estado("prueba_ej_luis")
        assert iniciar_sesion(con, "prueba_ej_luis", "Secreta123") is False, "Una cuenta bloqueada no puede entrar"
    finally:
        cursor = con.cursor()
        cursor.execute("DELETE FROM ej_usuarios WHERE usuario LIKE 'prueba_ej_%'")
        con.commit()
        cursor.close()
        con.close()
    print("Todas las pruebas pasaron")
