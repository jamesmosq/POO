"""
Ejercicio propuesto 05 - Validar dentro del procedimiento
Nivel: avanzado

Un procedimiento puede rechazar datos inválidos lanzando un error con
SIGNAL. Python lo recibe como mysql.connector.Error, con:
    error.sqlstate  -> "45000" (código para errores definidos por el usuario)
    error.msg       -> el MESSAGE_TEXT que se escribió en el SIGNAL

Requisitos:
1. SQL_CREAR: procedimiento ej_cambiar_precio(IN p_id INT,
   IN p_precio DECIMAL(10,2)) que:
       - si el producto no existe:
             SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Producto no existe';
       - si p_precio <= 0:
             SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Precio invalido';
       - si todo está bien, actualiza el precio.
2. Crea dos excepciones propias: ProductoNoExiste y PrecioInvalido.
3. cambiar_precio(con, id_producto, precio): llama al procedimiento, hace
   commit y traduce los errores 45000 a tus excepciones según el mensaje.
   Cualquier otro error se vuelve a lanzar tal cual.

Las pruebas cambian el precio de un producto y al final lo restauran.

Conceptos: SIGNAL, sqlstate, excepciones personalizadas, traducir errores.
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
"""

# Escribe tu solución aquí



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
