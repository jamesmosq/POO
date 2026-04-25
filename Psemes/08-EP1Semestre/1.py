def calcular_descuento(num_articulos, precio_total):
    if num_articulos >= 5:
        return 0.2  # 20% de descuento
    elif num_articulos >= 3:
        return 0.1  # 10% de descuento
    else:
        return 0


def aplicar_descuento(precio, descuento):
    return precio * (1 - descuento)


def determinar_metodo_pago(num_articulos):
    if num_articulos < 3:
        return "efectivo"
    else:
        return "tarjeta"


def procesar_compra():
    total_compra = 0
    num_articulos = 0
    continuar_comprando = True

    while continuar_comprando:
        precio = float(input("Ingrese el precio del artículo: $"))
        cantidad = int(input("Ingrese la cantidad de este artículo: "))

        total_compra += precio * cantidad
        num_articulos += cantidad

        respuesta = input("¿Desea agregar más artículos? (s/n): ").lower()
        continuar_comprando = respuesta == 's'

    descuento = calcular_descuento(num_articulos, total_compra)
    precio_final = aplicar_descuento(total_compra, descuento)
    metodo_pago = determinar_metodo_pago(num_articulos)

    print(f"\nResumen de la compra:")
    print(f"Número total de artículos: {num_articulos}")
    print(f"Total antes del descuento: ${total_compra:.2f}")
    print(f"Descuento aplicado: {descuento * 100}%")
    print(f"Total después del descuento: ${precio_final:.2f}")
    print(f"Método de pago recomendado: {metodo_pago}")

    if metodo_pago == "tarjeta":
        print("Se aplicará un cargo adicional del 2% por pago con tarjeta.")
        precio_final *= 1.02
        print(f"Total final con cargo de tarjeta: ${precio_final:.2f}")


procesar_compra()