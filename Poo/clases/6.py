def mostrar_menu():
    """Muestra el menú principal del sistema"""
    print("\n=== SISTEMA DE GESTIÓN DE INVENTARIO ===")
    print("1. Ver todos los productos")
    print("2. Buscar producto")
    print("3. Añadir producto")
    print("4. Modificar producto")
    print("5. Eliminar producto")
    print("6. Estadísticas del inventario")
    print("7. Salir")
    return input("Seleccione una opción (1-7): ")


def ver_productos(inventario):
    """Muestra todos los productos del inventario"""
    if not inventario:
        print("El inventario está vacío.")
        return

    print("\n=== LISTA DE PRODUCTOS ===")
    print("CÓDIGO | NOMBRE | PRECIO | CANTIDAD")
    print("-" * 50)
    for codigo, producto in inventario.items():
        print(f"{codigo} | {producto['nombre']} | ${producto['precio']} | {producto['cantidad']}")


def buscar_producto(inventario):
    """Busca un producto por código o nombre"""
    termino = input("Ingrese código o nombre del producto: ")

    # Buscar por código (exacto)
    if termino in inventario:
        producto = inventario[termino]
        print(f"\nProducto encontrado:")
        print(f"Código: {termino}")
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: ${producto['precio']}")
        print(f"Cantidad: {producto['cantidad']}")
        return

    # Buscar por nombre (parcial)
    resultados = []
    for codigo, producto in inventario.items():
        if termino.lower() in producto['nombre'].lower():
            resultados.append((codigo, producto))

    if resultados:
        print(f"\nSe encontraron {len(resultados)} productos:")
        for codigo, producto in resultados:
            print(f"{codigo} | {producto['nombre']} | ${producto['precio']} | {producto['cantidad']}")
    else:
        print("No se encontró ningún producto con ese código o nombre.")


def añadir_producto(inventario):
    """Añade un nuevo producto al inventario"""
    codigo = input("Ingrese el código del producto: ")

    # Verificar si ya existe
    if codigo in inventario:
        print("Error: Ya existe un producto con ese código.")
        return

    nombre = input("Ingrese el nombre del producto: ")

    # Validar precio
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: $"))
            if precio < 0:
                print("El precio no puede ser negativo.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número válido para el precio.")

    # Validar cantidad
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad disponible: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número entero para la cantidad.")

    # Añadir al inventario
    inventario[codigo] = {
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    }

    print(f"Producto '{nombre}' añadido correctamente.")


def modificar_producto(inventario):
    """Modifica un producto existente"""
    codigo = input("Ingrese el código del producto a modificar: ")

    if codigo not in inventario:
        print("Error: No existe un producto con ese código.")
        return

    producto = inventario[codigo]
    print(f"\nModificando producto: {producto['nombre']}")

    # Nombre (opcional)
    nuevo_nombre = input(f"Nuevo nombre [{producto['nombre']}] (deje en blanco para mantener): ")
    if nuevo_nombre:
        producto['nombre'] = nuevo_nombre

    # Precio (opcional)
    while True:
        nuevo_precio = input(f"Nuevo precio [${producto['precio']}] (deje en blanco para mantener): ")
        if not nuevo_precio:
            break
        try:
            nuevo_precio = float(nuevo_precio)
            if nuevo_precio < 0:
                print("El precio no puede ser negativo.")
                continue
            producto['precio'] = nuevo_precio
            break
        except ValueError:
            print("Por favor, ingrese un número válido para el precio.")

    # Cantidad (opcional)
    while True:
        nueva_cantidad = input(f"Nueva cantidad [{producto['cantidad']}] (deje en blanco para mantener): ")
        if not nueva_cantidad:
            break
        try:
            nueva_cantidad = int(nueva_cantidad)
            if nueva_cantidad < 0:
                print("La cantidad no puede ser negativa.")
                continue
            producto['cantidad'] = nueva_cantidad
            break
        except ValueError:
            print("Por favor, ingrese un número entero para la cantidad.")

    print("Producto modificado correctamente.")


def eliminar_producto(inventario):
    """Elimina un producto del inventario"""
    codigo = input("Ingrese el código del producto a eliminar: ")

    if codigo not in inventario:
        print("Error: No existe un producto con ese código.")
        return

    nombre = inventario[codigo]['nombre']
    confirmacion = input(f"¿Está seguro de eliminar '{nombre}'? (s/n): ")

    if confirmacion.lower() == 's':
        del inventario[codigo]
        print(f"Producto '{nombre}' eliminado correctamente.")
    else:
        print("Operación cancelada.")


def mostrar_estadisticas(inventario):
    """Muestra estadísticas del inventario"""
    if not inventario:
        print("El inventario está vacío.")
        return

    total_productos = len(inventario)
    total_items = sum(producto['cantidad'] for producto in inventario.values())
    valor_total = sum(producto['precio'] * producto['cantidad'] for producto in inventario.values())

    precio_min = min(producto['precio'] for producto in inventario.values())
    precio_max = max(producto['precio'] for producto in inventario.values())

    print("\n=== ESTADÍSTICAS DEL INVENTARIO ===")
    print(f"Total de productos diferentes: {total_productos}")
    print(f"Total de items en inventario: {total_items}")
    print(f"Valor total del inventario: ${valor_total:.2f}")
    print(f"Producto más barato: ${precio_min:.2f}")
    print(f"Producto más caro: ${precio_max:.2f}")

    # Productos con stock bajo (menos de 5 unidades)
    stock_bajo = [(codigo, producto) for codigo, producto in inventario.items() if producto['cantidad'] < 5]
    if stock_bajo:
        print("\nProductos con stock bajo (menos de 5 unidades):")
        for codigo, producto in stock_bajo:
            print(f"- {producto['nombre']}: {producto['cantidad']} unidades")


def main():
    """Función principal del sistema"""
    # Inicializar con algunos productos de ejemplo
    inventario = {
        "P001": {"nombre": "Teclado", "precio": 45.99, "cantidad": 10},
        "P002": {"nombre": "Mouse", "precio": 19.99, "cantidad": 15},
        "P003": {"nombre": "Monitor", "precio": 159.99, "cantidad": 5},
        "P004": {"nombre": "Auriculares", "precio": 29.99, "cantidad": 8}
    }

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            ver_productos(inventario)
        elif opcion == "2":
            buscar_producto(inventario)
        elif opcion == "3":
            añadir_producto(inventario)
        elif opcion == "4":
            modificar_producto(inventario)
        elif opcion == "5":
            eliminar_producto(inventario)
        elif opcion == "6":
            mostrar_estadisticas(inventario)
        elif opcion == "7":
            print("¡Gracias por usar el Sistema de Gestión de Inventario!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 7.")


if __name__ == "__main__":
    main()