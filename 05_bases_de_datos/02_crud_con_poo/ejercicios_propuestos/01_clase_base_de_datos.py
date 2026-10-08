"""
Ejercicio propuesto 01 - Clase BaseDeDatos
Nivel: básico

En lugar de repetir la conexión y los cursores en cada función, se
encapsulan en una clase.

Requisitos. Crea la clase BaseDeDatos(config):
1. conectar(): abre la conexión y la guarda en self.con.
2. cerrar(): cierra la conexión si está abierta.
3. __enter__ y __exit__ para usarla con with:
       with BaseDeDatos(CONFIG) as db:
           ...
   __enter__ conecta y retorna self; __exit__ cierra la conexión. __exit__
   NO debe retornar True (eso escondería los errores que ocurran dentro
   del with).
4. consultar(sql, parametros=()): retorna una lista de diccionarios.
5. ejecutar(sql, parametros=()): para INSERT, UPDATE y DELETE. Hace commit
   y retorna la cantidad de filas afectadas (cursor.rowcount). Guarda en
   self.ultimo_id el cursor.lastrowid.

Conceptos: encapsular la conexión, context managers, commit.
"""
import os
from contextlib import closing

import mysql.connector

CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "northwind"),
}

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
def limpiar_datos_de_prueba():
    con = mysql.connector.connect(**CONFIG)
    cursor = con.cursor()
    cursor.execute("DELETE FROM Shippers WHERE ShipperName LIKE 'PRUEBA_EJ_%'")
    con.commit()
    cursor.close()
    con.close()


if __name__ == "__main__":
    try:
        with BaseDeDatos(CONFIG) as db:
            assert db.con.is_connected()
            filas = db.ejecutar("INSERT INTO Shippers (ShipperName, Phone) VALUES (%s, %s)", ("PRUEBA_EJ_Uno", "555"))
            assert filas == 1
            nuevo_id = db.ultimo_id
            assert isinstance(nuevo_id, int) and nuevo_id > 0

            encontrados = db.consultar("SELECT ShipperID, ShipperName FROM Shippers WHERE ShipperID = %s", (nuevo_id,))
            assert encontrados == [{"ShipperID": nuevo_id, "ShipperName": "PRUEBA_EJ_Uno"}]

        assert not db.con.is_connected(), "Al salir del with la conexión debe cerrarse"

        otra = mysql.connector.connect(**CONFIG)
        cursor = otra.cursor(buffered=True)
        cursor.execute("SELECT COUNT(*) FROM Shippers WHERE ShipperID = %s", (nuevo_id,))
        assert cursor.fetchone()[0] == 1, "ejecutar() debe hacer commit"
        cursor.close()
        otra.close()

        try:
            with BaseDeDatos(CONFIG) as db:
                db.consultar("SELECT * FROM TablaQueNoExiste")
            raise AssertionError("El error de la consulta no debe quedar escondido")
        except mysql.connector.Error:
            pass
    finally:
        limpiar_datos_de_prueba()

    print("Todas las pruebas pasaron")
