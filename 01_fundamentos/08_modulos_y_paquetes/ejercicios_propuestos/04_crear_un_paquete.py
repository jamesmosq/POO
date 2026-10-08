"""
Ejercicio propuesto 04 - Crear un paquete
Nivel: intermedio

Un paquete es una carpeta con módulos y un archivo __init__.py. Sirve para
organizar un proyecto grande en partes.

Requisitos. Crea en esta carpeta la siguiente estructura:

    tienda/
        __init__.py
        productos.py      -> subtotal(precio, cantidad)
                             retorna precio * cantidad
        descuentos.py     -> aplicar_descuento(valor, porcentaje)
                             retorna valor con el descuento aplicado
                             lanza ValueError si porcentaje no está entre 0 y 100

    En tienda/__init__.py importa las dos funciones para que se puedan usar
    directamente desde el paquete:
        from .productos import subtotal
        from .descuentos import aplicar_descuento

    El punto en ".productos" significa "el módulo productos de ESTE
    paquete" (importación relativa).

Después de crear el paquete, se puede usar de dos formas:
    from tienda.productos import subtotal
    import tienda; tienda.subtotal(...)

Conceptos: paquetes, __init__.py, importaciones relativas.
"""

# Este ejercicio se resuelve en la carpeta tienda/.


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import tienda
    from tienda.productos import subtotal
    from tienda.descuentos import aplicar_descuento

    assert subtotal(2500, 4) == 10000
    assert aplicar_descuento(10000, 10) == 9000
    assert tienda.subtotal(100, 3) == 300, "Expón subtotal en tienda/__init__.py"
    assert tienda.aplicar_descuento(200, 50) == 100, "Expón aplicar_descuento en tienda/__init__.py"

    try:
        aplicar_descuento(100, 150)
        raise AssertionError("Un porcentaje mayor a 100 debe lanzar ValueError")
    except ValueError:
        pass

    print("Todas las pruebas pasaron")
