"""
Ejercicio para corregir 05 - Errores del procedimiento
Nivel: avanzado
Errores a encontrar: 3

Qué debería hacer el programa:
    El procedimiento ej_ajustar_precio(p_id, p_precio) valida con
    SIGNAL y actualiza el precio. cambiar_precio(con, id, precio):
        - deja el cambio GUARDADO en la base de datos;
        - traduce el error 'Producto no existe' a ProductoNoExiste;
        - traduce el error 'Precio invalido' a PrecioInvalido.

Pista: imprime error.errno, error.sqlstate y error.msg dentro del except
para ver qué trae realmente el error.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
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


class ProductoNoExiste(Exception):
    pass


class PrecioInvalido(Exception):
    pass


def preparar(con):
    """Crea el procedimiento que usa este ejercicio. Este código está bien."""
    with closing(con.cursor()) as cursor:
        cursor.execute("DROP PROCEDURE IF EXISTS ej_ajustar_precio")
        cursor.execute("""
            CREATE PROCEDURE ej_ajustar_precio(IN p_id INT, IN p_precio DECIMAL(10,2))
            BEGIN
                IF NOT EXISTS (SELECT 1 FROM Products WHERE ProductID = p_id) THEN
                    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Producto no existe';
                END IF;
                IF p_precio <= 0 THEN
                    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Precio invalido';
                END IF;
                UPDATE Products SET Price = p_precio WHERE ProductID = p_id;
            END
        """)


def cambiar_precio(con, id_producto, precio):
    with closing(con.cursor()) as cursor:
        try:
            cursor.callproc("ej_ajustar_precio", [id_producto, precio])
        except mysql.connector.Error as error:
            if error.errno == 45000:
                if error.msg == "Producto no existe":
                    raise PrecioInvalido(error.msg)
                if error.msg == "Precio invalido":
                    raise ProductoNoExiste(error.msg)
            raise


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
    preparar(con)
    ref = con.cursor(buffered=True)
    ref.execute("SELECT MIN(ProductID) FROM Products")
    id_producto = ref.fetchone()[0]
    ref.close()
    original = precio_actual(id_producto)

    try:
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

        cambiar_precio(con, id_producto, 77)
        assert precio_actual(id_producto) == 77, "El cambio no quedó guardado"
    finally:
        con.rollback()
        cursor = con.cursor()
        cursor.execute("UPDATE Products SET Price = %s WHERE ProductID = %s", (original, id_producto))
        con.commit()
        cursor.close()
        con.close()

    print("Todas las pruebas pasaron")
