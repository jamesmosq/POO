"""
Ejercicio propuesto 03 - Inicio de sesión con bloqueo
Nivel: intermedio

Requisitos. Escribe iniciar_sesion(con, usuario, clave), que retorne True
o False:
1. Si el usuario no existe -> False. No lances un error distinto ni des un
   mensaje diferente: decir "ese usuario no existe" le ayuda a un atacante
   a descubrir qué usuarios son válidos.
2. Si la cuenta está bloqueada -> False, aunque la clave sea correcta.
3. Si la clave es incorrecta: suma 1 a intentos_fallidos; al llegar a
   MAXIMO_INTENTOS (3) marca la cuenta como bloqueada. Retorna False.
4. Si la clave es correcta: deja intentos_fallidos en 0 y retorna True.
5. Cada cambio en la tabla se confirma con commit.

preparar() crea la tabla y crear_usuario() registra usuarios de prueba;
los dos ya están escritos.

Conceptos: autenticación, bloqueo por intentos, no filtrar información.
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

# Escribe tu solución aquí



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
