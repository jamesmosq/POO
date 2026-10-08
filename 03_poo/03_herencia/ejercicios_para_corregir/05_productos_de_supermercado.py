"""
Ejercicio para corregir 05 - Productos de supermercado
Nivel: avanzado
Errores a encontrar: 3

Qué debería hacer el programa:
    Producto -> ProductoBasico -> Perecedero

    - Producto: precio_final() aplica el IVA del atributo de clase IVA (19).
    - ProductoBasico: los productos de la canasta básica pagan IVA de 5;
      solo cambia el atributo IVA, el cálculo es el mismo.
    - Perecedero(nombre, precio, dias_para_vencer): si le quedan 2 días o
      menos, tiene 50 % de descuento sobre el precio final de su padre.

        Producto("TV", 1000).precio_final()             -> 1190.0
        ProductoBasico("Arroz", 1000).precio_final()    -> 1050.0
        Perecedero("Leche", 1000, 5).precio_final()     -> 1050.0
        Perecedero("Leche", 1000, 2).precio_final()     -> 525.0

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class Producto:
    IVA = 19

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def precio_final(self):
        return self.precio * (1 + Producto.IVA / 100)


class ProductoBasico(Producto):
    IVA = 5


class Perecedero(ProductoBasico):
    def __init__(self, nombre, precio, dias_para_vencer):
        super().__init__(nombre)
        self.precio = precio
        self.dias_para_vencer = dias_para_vencer

    def precio_final(self):
        precio = super().precio_final()
        if self.dias_para_vencer < 2:
            return precio * 0.5
        return precio


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert round(Producto("TV", 1000).precio_final(), 2) == 1190.0
    assert round(Perecedero("Leche", 1000, 5).precio_final(), 2) == 1050.0, Perecedero("Leche", 1000, 5).precio_final()
    assert round(ProductoBasico("Arroz", 1000).precio_final(), 2) == 1050.0
    assert round(Perecedero("Leche", 1000, 2).precio_final(), 2) == 525.0, "Con 2 días ya aplica el descuento"
    assert round(Perecedero("Yogur", 1000, 1).precio_final(), 2) == 525.0

    print("Todas las pruebas pasaron")
