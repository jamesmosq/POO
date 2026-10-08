"""
Ejercicio propuesto 05 - Inyección SQL
Nivel: avanzado

La función buscar_inseguro (ya escrita) arma la consulta pegando lo que
escribe el usuario. Ejecuta el archivo después de resolver el ejercicio y
mira en las pruebas lo que logra un atacante con "x' OR '1'='1".

Requisitos:
1. buscar_seguro(con, usuario): igual que buscar_inseguro (retorna la lista
   de nombres de usuario que coinciden EXACTAMENTE), pero con parámetros
   %s. Con el texto malicioso no debe encontrar nada.
2. buscar_por_prefijo(con, prefijo): retorna los usuarios que EMPIEZAN por
   el prefijo (en cualquier orden). Problema: en LIKE, los caracteres % y _ son
   comodines. Si el usuario escribe "prueba_ej_a_", el _ no debe
   significar "cualquier carácter". Hay que escaparlos:
       - reemplaza "!" por "!!", "%" por "!%" y "_" por "!_"
       - y usa: ... WHERE usuario LIKE %s ESCAPE '!'
   El parámetro es el prefijo escapado seguido de "%".

preparar() y crear_usuario() ya están escritos.

Conceptos: inyección SQL, consultas parametrizadas, escapar comodines.
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
    hash_texto = bcrypt.hashpw(clave.encode(), bcrypt.gensalt(4)).decode()
    with closing(con.cursor()) as cursor:
        cursor.execute("INSERT INTO ej_usuarios (usuario, hash) VALUES (%s, %s)", (usuario, hash_texto))
    con.commit()


def buscar_inseguro(con, usuario):
    """NO hagas esto: es vulnerable a inyección SQL."""
    with closing(con.cursor()) as cursor:
        cursor.execute(f"SELECT usuario FROM ej_usuarios WHERE usuario = '{usuario}' ORDER BY usuario")
        return [fila[0] for fila in cursor.fetchall()]

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    preparar(con)
    try:
        for usuario in ("prueba_ej_ana", "prueba_ej_a_b", "prueba_ej_axb", "prueba_ej_luis"):
            crear_usuario(con, usuario, "Secreta123")

        ataque = "x' OR '1'='1"
        filtrados = buscar_inseguro(con, ataque)
        assert len(filtrados) >= 4, "La versión insegura deja ver todos los usuarios"

        assert buscar_seguro(con, ataque) == []
        assert buscar_seguro(con, "prueba_ej_ana") == ["prueba_ej_ana"]

        assert sorted(buscar_por_prefijo(con, "prueba_ej_a")) == ["prueba_ej_a_b", "prueba_ej_ana", "prueba_ej_axb"]
        assert sorted(buscar_por_prefijo(con, "prueba_ej_a_")) == ["prueba_ej_a_b"], "El _ debe buscarse como texto, no como comodín"
        assert buscar_por_prefijo(con, "%") == [], "El % debe buscarse como texto, no como comodín"
    finally:
        cursor = con.cursor()
        cursor.execute("DELETE FROM ej_usuarios WHERE usuario LIKE 'prueba!_ej!_%' ESCAPE '!'")
        con.commit()
        cursor.close()
        con.close()
    print("Todas las pruebas pasaron")
