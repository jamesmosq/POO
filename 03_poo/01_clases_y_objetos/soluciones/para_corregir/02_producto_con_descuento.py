"""
Solución - Ejercicio para corregir 02 - Producto con descuento

CORRECCIÓN 1 (AttributeError: 'Producto' object has no attribute
'precio'): "precio = precio" solo asigna una variable local que desaparece
al terminar __init__. Para guardarlo en el objeto se escribe self.precio.

CORRECCIÓN 2 (NameError: name 'descuento' is not defined): dentro de la
clase, los otros métodos se llaman a través del objeto: self.descuento().
"""

class Producto:
    def __init__(self, nombre, precio, porcentaje_descuento=0):
        self.nombre = nombre
        self.precio = precio  # CORRECCIÓN 1
        self.porcentaje_descuento = porcentaje_descuento

    def descuento(self):
        return self.precio * self.porcentaje_descuento / 100

    def precio_final(self):
        return self.precio - self.descuento()  # CORRECCIÓN 2


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    cafe = Producto("Café", 10000, 20)
    assert cafe.precio == 10000
    assert cafe.descuento() == 2000
    assert cafe.precio_final() == 8000

    print("Todas las pruebas pasaron")
