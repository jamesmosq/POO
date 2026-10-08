"""
Ejercicio para corregir 02 - Producto con descuento
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    Producto("Café", 10000, 20).precio_final() aplica el descuento del 20 %
    y retorna 8000.0.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class Producto:
    def __init__(self, nombre, precio, porcentaje_descuento=0):
        self.nombre = nombre
        precio = precio
        self.porcentaje_descuento = porcentaje_descuento

    def descuento(self):
        return self.precio * self.porcentaje_descuento / 100

    def precio_final(self):
        return self.precio - descuento()


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    cafe = Producto("Café", 10000, 20)
    assert cafe.precio == 10000
    assert cafe.descuento() == 2000
    assert cafe.precio_final() == 8000

    print("Todas las pruebas pasaron")
