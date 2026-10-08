"""
Ejercicio para corregir 05 - Procesar pedidos
Nivel: avanzado
Errores a encontrar: 3

Qué debería hacer el programa:
    - vender(inventario, producto, cantidad):
        * lanza ValueError(f"Producto desconocido: {producto}") si no existe;
        * lanza StockInsuficiente si no alcanza la cantidad, SIN modificar
          el inventario;
        * si todo está bien, descuenta la cantidad.
    - procesar(inventario, pedidos): procesa una lista de pedidos
      (producto, cantidad) y retorna el estado de cada uno:
          "ok", "sin stock" o "desconocido".

        inventario = {"pan": 5}
        procesar(inventario, [("pan", 2), ("pan", 10), ("leche", 1)])
            -> ["ok", "sin stock", "desconocido"]
        inventario -> {"pan": 3}

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class StockInsuficiente(Exception):
    pass


def vender(inventario, producto, cantidad):
    try:
        disponible = inventario[producto]
    except KeyError:
        pass
    inventario[producto] = disponible - cantidad
    if inventario[producto] < 0:
        raise StockInsuficiente(f"No hay suficiente {producto}")


def procesar(inventario, pedidos):
    estados = []
    for producto, cantidad in pedidos:
        try:
            vender(inventario, producto, cantidad)
            estados.append("ok")
        except StockInsuficiente or ValueError as error:
            if isinstance(error, StockInsuficiente):
                estados.append("sin stock")
            else:
                estados.append("desconocido")
    return estados


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    inventario = {"pan": 5}
    estados = procesar(inventario, [("pan", 2), ("pan", 10), ("leche", 1)])
    assert estados == ["ok", "sin stock", "desconocido"], estados
    assert inventario == {"pan": 3}, f"El inventario quedó así: {inventario}"

    try:
        vender({}, "arroz", 1)
        raise AssertionError("Debe lanzar ValueError")
    except ValueError as error:
        assert str(error) == "Producto desconocido: arroz"

    print("Todas las pruebas pasaron")
