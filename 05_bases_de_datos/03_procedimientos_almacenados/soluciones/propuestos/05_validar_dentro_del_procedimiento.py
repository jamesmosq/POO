"""
Solución - Ejercicio propuesto 05 - Validar dentro del procedimiento
"""

import os
from contextlib import closing

import mysql.connector

CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "base1234"),
    "database": os.getenv("DB_NAME", "northwind"),
}

SQL_CREAR = """
CREATE PROCEDURE ej_cambiar_precio(IN p_id INT, IN p_precio DECIMAL(10,2))
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Products WHERE ProductID = p_id) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Producto no existe';
    END IF;
    IF p_precio <= 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Precio invalido';
    END IF;
    UPDATE Products SET Price = p_precio WHERE ProductID = p_id;
END
"""


class ProductoNoExiste(Exception):
    pass


class PrecioInvalido(Exception):
    pass


ERRORES = {"Producto no existe": ProductoNoExiste, "Precio invalido": PrecioInvalido}


def crear_procedimiento(con):
    with closing(con.cursor()) as cursor:
        cursor.execute("DROP PROCEDURE IF EXISTS ej_cambiar_precio")
        cursor.execute(SQL_CREAR)


def cambiar_precio(con, id_producto, precio):
    with closing(con.cursor()) as cursor:
        try:
            cursor.callproc("ej_cambiar_precio", [id_producto, precio])
        except mysql.connector.Error as error:
            # SIGNAL llega con sqlstate "45000"; el número de error (errno) es otro.
            if error.sqlstate == "45000" and error.msg in ERRORES:
                raise ERRORES[error.msg](error.msg)
            raise
    con.commit()


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
def precio_actual(id_producto):
    otra = mysql.connector.connect(**CONFIG)
    cursor = otra.cursor(buffered=True)
    cursor.execute("SELECT Price FROM Products WHERE ProductID = %s", (id_producto,))
    precio = float(cursor.fetchone()[0])
    cursor.close()
    otra.close()
    return precio


if __name__ == "__main__":
    con = mysql.connector.connect(**CONFIG)
    crear_procedimiento(con)
    ref = con.cursor(buffered=True)
    ref.execute("SELECT MIN(ProductID) FROM Products")
    id_producto = ref.fetchone()[0]
    ref.close()
    original = precio_actual(id_producto)

    try:
        cambiar_precio(con, id_producto, 99)
        assert precio_actual(id_producto) == 99, "El cambio debe quedar guardado (commit)"

        try:
            cambiar_precio(con, -1, 10)
            raise AssertionError("Debe lanzar ProductoNoExiste")
        except ProductoNoExiste:
            pass

        try:
            cambiar_precio(con, id_producto, 0)
            raise AssertionError("Debe lanzar PrecioInvalido")
        except PrecioInvalido:
            pass
        assert precio_actual(id_producto) == 99
    finally:
        cursor = con.cursor()
        cursor.execute("UPDATE Products SET Price = %s WHERE ProductID = %s", (original, id_producto))
        con.commit()
        cursor.close()
        con.close()

    print("Todas las pruebas pasaron")
