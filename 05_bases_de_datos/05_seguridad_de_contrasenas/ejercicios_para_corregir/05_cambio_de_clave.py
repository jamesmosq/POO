"""
Ejercicio para corregir 05 - Cambio de clave
Nivel: avanzado
Errores a encontrar: 3

Qué debería hacer el programa:
    cambiar_clave(con, usuario, actual, nueva):
        - exige que la clave ACTUAL sea correcta (si no, PermissionError);
        - guarda el hash de la clave nueva y lo deja GUARDADO.

Ojo: este código no lanza errores en el caso feliz. Revisa con cuidado qué
clave se verifica, qué valores recibe el UPDATE y si el cambio se confirma.

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


def cambiar_clave(con, usuario, actual, nueva):
    with closing(con.cursor(buffered=True)) as cursor:
        cursor.execute("SELECT hash FROM ej_usuarios WHERE usuario = %s", (usuario,))
        fila = cursor.fetchone()
        if fila is None or not bcrypt.checkpw(nueva.encode(), fila[0].encode()):
            raise PermissionError("Credenciales incorrectas")
        nuevo_hash = bcrypt.hashpw(nueva.encode(), bcrypt.gensalt()).decode()
        cursor.execute("UPDATE ej_usuarios SET hash = %s WHERE usuario = %s", (usuario, nuevo_hash))


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
