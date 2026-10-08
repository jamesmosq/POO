"""
Ejercicio para corregir 03 - Inventario como contenedor
Nivel: intermedio
Errores a encontrar: 2

Qué debería hacer el programa:
    inv = Inventario(); inv.agregar("pan"); inv.agregar("leche")
    len(inv)        -> 2
    "pan" in inv    -> True
    for p in inv    -> recorre "pan", "leche"

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class Inventario:
    def __init__(self):
        self._productos = []

    def agregar(self, producto):
        self._productos.append(producto)

    def __len__(self):
        return f"{len(self._productos)} productos"

    def __contains__(self, producto):
        return producto in self._productos

    def __iter__(self):
        return self._productos


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    inv = Inventario()
    inv.agregar("pan")
    inv.agregar("leche")

    assert len(inv) == 2
    assert "pan" in inv
    assert [p for p in inv] == ["pan", "leche"]

    print("Todas las pruebas pasaron")
