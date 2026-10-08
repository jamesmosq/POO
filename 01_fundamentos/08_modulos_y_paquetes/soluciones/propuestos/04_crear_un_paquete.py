"""
Solución - Ejercicio propuesto 04 - Crear un paquete

La solución está en la carpeta tienda/ de esta misma carpeta.
"""

# Este ejercicio se resuelve en la carpeta tienda/.


# ----------------------------------------------------------------------
# Pruebas
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
