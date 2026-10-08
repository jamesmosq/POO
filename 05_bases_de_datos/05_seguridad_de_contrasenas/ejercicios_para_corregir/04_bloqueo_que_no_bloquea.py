"""
Ejercicio para corregir 04 - Bloqueo que no bloquea
Nivel: intermedio
Errores a encontrar: 3

Qué debería hacer el programa:
    - Cada intento fallido suma 1 a intentos_fallidos y queda GUARDADO.
    - Al llegar a 3 intentos fallidos la cuenta se bloquea.
    - Un ingreso correcto deja intentos_fallidos en 0.
    - Una cuenta bloqueada no puede entrar.

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

MAXIMO_INTENTOS = 3


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
        cursor.execute("SELECT hash, intentos_fallidos, bloqueado FROM ej_usuarios WHERE usuario = %s", (usuario,))
        fila = cursor.fetchone()
        if fila is None:
            return False
        hash_guardado, intentos, bloqueado = fila
        if bloqueado:
            return False
        if bcrypt.checkpw(clave.encode(), hash_guardado.encode()):
            return True
        intentos += 1
        cursor.execute(
            "UPDATE ej_usuarios SET intentos_fallidos = %s, bloqueado = %s WHERE usuario = %s",
            (intentos, intentos > MAXIMO_INTENTOS, usuario),
        )
        return False


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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

        assert iniciar_sesion(con, "prueba_ej_ana", "mala") is False
        assert estado("prueba_ej_ana") == (1, False), f"Estado guardado: {estado('prueba_ej_ana')}"
        assert iniciar_sesion(con, "prueba_ej_ana", "Secreta123") is True
        assert estado("prueba_ej_ana") == (0, False), "Un ingreso correcto debe reiniciar los intentos"

        for _ in range(MAXIMO_INTENTOS):
            iniciar_sesion(con, "prueba_ej_luis", "mala")
        assert estado("prueba_ej_luis") == (3, True), f"Estado guardado: {estado('prueba_ej_luis')}"
    finally:
        con.rollback()
        cursor = con.cursor()
        cursor.execute("DELETE FROM ej_usuarios WHERE usuario LIKE 'prueba_ej_%'")
        con.commit()
        cursor.close()
        con.close()
    print("Todas las pruebas pasaron")
