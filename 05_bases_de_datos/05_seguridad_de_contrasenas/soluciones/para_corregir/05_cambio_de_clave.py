"""
Solución - Ejercicio para corregir 05 - Cambio de clave

CORRECCIÓN 1: se verificaba la clave NUEVA contra el hash guardado, en
lugar de la ACTUAL. Así, quien no conoce la clave actual podía cambiarla
si escribía como "nueva" la clave vigente, y el dueño legítimo no podía.

CORRECCIÓN 2 (el UPDATE no cambiaba nada): los parámetros estaban al revés.
Se buscaba un usuario llamado como el hash, y no existía ninguno. Un UPDATE
que no encuentra filas no da error: simplemente modifica 0 filas.

CORRECCIÓN 3: faltaba con.commit(); el cambio se perdía al cerrar la
conexión.
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


def cambiar_clave(con, usuario, actual, nueva):
    with closing(con.cursor(buffered=True)) as cursor:
        cursor.execute("SELECT hash FROM ej_usuarios WHERE usuario = %s", (usuario,))
        fila = cursor.fetchone()
        if fila is None or not bcrypt.checkpw(actual.encode(), fila[0].encode()):  # CORRECCIÓN 1
            raise PermissionError("Credenciales incorrectas")
        nuevo_hash = bcrypt.hashpw(nueva.encode(), bcrypt.gensalt()).decode()
        cursor.execute("UPDATE ej_usuarios SET hash = %s WHERE usuario = %s", (nuevo_hash, usuario))  # CORRECCIÓN 2
    con.commit()  # CORRECCIÓN 3


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
def hash_guardado(usuario):
    otra = mysql.connector.connect(**CONFIG)
    cursor = otra.cursor(buffered=True)
    cursor.execute("SELECT hash FROM ej_usuarios WHERE usuario = %s", (usuario,))
    valor = cursor.fetchone()[0]
    cursor.close()
    otra.close()
    return valor


if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    preparar(con)
    try:
        crear_usuario(con, "prueba_ej_ana", "Secreta123")

        try:
            cambiar_clave(con, "prueba_ej_ana", "incorrecta", "Hackeada99")
            raise AssertionError("Con la clave actual incorrecta debe lanzar PermissionError")
        except PermissionError:
            pass

        cambiar_clave(con, "prueba_ej_ana", "Secreta123", "NuevaClave9")
        guardado = hash_guardado("prueba_ej_ana").encode()
        assert bcrypt.checkpw(b"NuevaClave9", guardado), "La clave nueva no quedó guardada"
    finally:
        con.rollback()
        cursor = con.cursor()
        cursor.execute("DELETE FROM ej_usuarios WHERE usuario LIKE 'prueba_ej_%'")
        con.commit()
        cursor.close()
        con.close()
    print("Todas las pruebas pasaron")
