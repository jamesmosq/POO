"""
Solución - Ejercicio propuesto 04 - Política de contraseñas y cambio de clave
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


def crear_usuario(con, usuario, clave):
    """Registra un usuario con su hash. No lo modifiques."""
    hash_texto = bcrypt.hashpw(clave.encode(), bcrypt.gensalt()).decode()
    with closing(con.cursor()) as cursor:
        cursor.execute("INSERT INTO ej_usuarios (usuario, hash) VALUES (%s, %s)", (usuario, hash_texto))
    con.commit()


def validar_politica(clave):
    problemas = []
    if len(clave) < 8:
        problemas.append("Mínimo 8 caracteres")
    if not any(c.isupper() for c in clave):
        problemas.append("Al menos una mayúscula")
    if not any(c.islower() for c in clave):
        problemas.append("Al menos una minúscula")
    if not any(c.isdigit() for c in clave):
        problemas.append("Al menos un número")
    return problemas


def cambiar_clave(con, usuario, actual, nueva):
    with closing(con.cursor(buffered=True)) as cursor:
        cursor.execute("SELECT hash FROM ej_usuarios WHERE usuario = %s", (usuario,))
        fila = cursor.fetchone()
        if fila is None or not bcrypt.checkpw(actual.encode(), fila[0].encode()):
            raise PermissionError("Credenciales incorrectas")

        problemas = validar_politica(nueva)
        if problemas:
            raise ValueError("; ".join(problemas))
        if nueva == actual:
            raise ValueError("La nueva clave debe ser distinta")

        nuevo_hash = bcrypt.hashpw(nueva.encode(), bcrypt.gensalt()).decode()
        cursor.execute("UPDATE ej_usuarios SET hash = %s WHERE usuario = %s", (nuevo_hash, usuario))
    con.commit()


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
    assert validar_politica("Secreta123") == []
    assert validar_politica("abc") == ["Mínimo 8 caracteres", "Al menos una mayúscula", "Al menos un número"]
    assert validar_politica("SOLOMAYUSCULAS1") == ["Al menos una minúscula"]

    con = mysql.connector.connect(**CONFIG)
    preparar(con)
    try:
        crear_usuario(con, "prueba_ej_ana", "Secreta123")

        for usuario, actual in (("prueba_ej_ana", "incorrecta"), ("prueba_ej_nadie", "Secreta123")):
            try:
                cambiar_clave(con, usuario, actual, "NuevaClave9")
                raise AssertionError("Debe lanzar PermissionError")
            except PermissionError as error:
                assert str(error) == "Credenciales incorrectas"

        try:
            cambiar_clave(con, "prueba_ej_ana", "Secreta123", "corta")
            raise AssertionError("Debe lanzar ValueError")
        except ValueError as error:
            assert str(error) == "Mínimo 8 caracteres; Al menos una mayúscula; Al menos un número", str(error)

        try:
            cambiar_clave(con, "prueba_ej_ana", "Secreta123", "Secreta123")
            raise AssertionError("Debe lanzar ValueError")
        except ValueError as error:
            assert str(error) == "La nueva clave debe ser distinta"

        cambiar_clave(con, "prueba_ej_ana", "Secreta123", "NuevaClave9")
        guardado = hash_guardado("prueba_ej_ana").encode()
        assert bcrypt.checkpw(b"NuevaClave9", guardado), "La clave nueva debe quedar guardada"
        assert not bcrypt.checkpw(b"Secreta123", guardado)
    finally:
        cursor = con.cursor()
        cursor.execute("DELETE FROM ej_usuarios WHERE usuario LIKE 'prueba_ej_%'")
        con.commit()
        cursor.close()
        con.close()
    print("Todas las pruebas pasaron")
