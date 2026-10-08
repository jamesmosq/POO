"""
Ejercicio para corregir 05 - Catálogo con lambdas
Nivel: avanzado
Errores a encontrar: 3

Qué debería hacer el programa:
    Los productos son tuplas (nombre, precio).

    - aplicar_descuento(productos, porcentaje): retorna una lista con los
      precios ya rebajados.
          aplicar_descuento([("A", 1000)], 10)  -> [900.0]
    - ordenar_por_precio(productos): retorna los productos de menor a mayor
      precio.
    - filtrar_baratos(productos, limite): retorna los productos con precio
      menor O IGUAL al límite.

Ojo: el programa no lanza errores. Los tres son de lógica. Revisa con
cuidado qué hace cada lambda.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


def aplicar_descuento(productos, porcentaje):
    return list(map(lambda p: p[1] * porcentaje / 100, productos))


def ordenar_por_precio(productos):
    return sorted(productos, key=lambda p: p[0])


def filtrar_baratos(productos, limite):
    return list(filter(lambda p: p[1] < limite, productos))


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    catalogo = [("Teclado", 80000), ("Mouse", 30000), ("Audífonos", 50000)]

    assert aplicar_descuento(catalogo, 10) == [72000, 27000, 45000], aplicar_descuento(catalogo, 10)
    assert ordenar_por_precio(catalogo) == [("Mouse", 30000), ("Audífonos", 50000), ("Teclado", 80000)]
    assert filtrar_baratos(catalogo, 50000) == [("Mouse", 30000), ("Audífonos", 50000)]

    print("Todas las pruebas pasaron")
