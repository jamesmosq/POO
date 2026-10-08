"""
Solución - Ejercicio para corregir 05 - Productos de supermercado

CORRECCIÓN 1 (TypeError: Producto.__init__() missing 1 required positional
argument: 'precio'): super().__init__ debe recibir todos los parámetros que
necesita el padre. Así, además, no hace falta asignar self.precio en la
hija.

CORRECCIÓN 2 (la canasta básica pagaba 19 %): Producto.IVA siempre lee el
atributo de Producto, aunque el objeto sea de una clase hija que lo cambió.
self.IVA busca primero en la clase del objeto, y así ProductoBasico usa 5.

CORRECCIÓN 3 (con 2 días no había descuento): "2 días o menos" es <= 2.
"""

class Producto:
    IVA = 19

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def precio_final(self):
        return self.precio * (1 + self.IVA / 100)  # CORRECCIÓN 2


class ProductoBasico(Producto):
    IVA = 5


class Perecedero(ProductoBasico):
    def __init__(self, nombre, precio, dias_para_vencer):
        super().__init__(nombre, precio)  # CORRECCIÓN 1
        self.dias_para_vencer = dias_para_vencer

    def precio_final(self):
        precio = super().precio_final()
        if self.dias_para_vencer <= 2:  # CORRECCIÓN 3
            return precio * 0.5
        return precio


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert round(Producto("TV", 1000).precio_final(), 2) == 1190.0
    assert round(Perecedero("Leche", 1000, 5).precio_final(), 2) == 1050.0, Perecedero("Leche", 1000, 5).precio_final()
    assert round(ProductoBasico("Arroz", 1000).precio_final(), 2) == 1050.0
    assert round(Perecedero("Leche", 1000, 2).precio_final(), 2) == 525.0, "Con 2 días ya aplica el descuento"
    assert round(Perecedero("Yogur", 1000, 1).precio_final(), 2) == 525.0

    print("Todas las pruebas pasaron")
