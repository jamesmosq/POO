def pedir_cafe(tipo):
    match tipo.lower():
        case "expreso":
            return "Expreso: Café fuerte en taza pequeña."
        case "americano":
            return "Americano: Expreso con agua caliente añadida."
        case "latte":
            return "Latte: Expreso con leche vaporizada y una capa de espuma."
        case "capuchino":
            return "Capuchino: Expreso con partes iguales de leche vaporizada y espuma."
        case _:
            return "Lo siento, no tenemos ese tipo de café."


def cafeteria():
    print("Bienvenido a la Cafetería Python")
    print("Nuestro menú: expreso, americano, latte, capuchino")

    while True:
        pedido = input("¿Qué tipo de café deseas? (o 'salir' para terminar): ")
        if pedido.lower() == 'salir':
            print("¡Gracias por tu visita!")
            break

        resultado = pedir_cafe(pedido)
        print(resultado)


cafeteria()