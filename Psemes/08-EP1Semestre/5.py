from datetime import datetime


def obtener_precio_base():
    while True:
        try:
            precio = float(input("Ingrese el precio base de la motocicleta: $"))
            if precio > 0:
                return precio
            else:
                print("El precio debe ser mayor que cero.")
        except ValueError:
            print("Por favor, ingrese un número válido.")


def obtener_marca():
    marcas = ["Honda", "Yamaha", "Suzuki", "Otra"]
    print("Marcas disponibles:")
    for i, marca in enumerate(marcas, 1):
        print(f"{i}. {marca}")

    while True:
        try:
            seleccion = int(input("Seleccione el número de la marca: "))
            if 1 <= seleccion <= len(marcas):
                return marcas[seleccion - 1]
            else:
                print("Por favor, seleccione un número válido.")
        except ValueError:
            print("Por favor, ingrese un número.")


def calcular_descuento_marca(marca, precio_base):
    descuentos = {"Honda": 0.05, "Yamaha": 0.08, "Suzuki": 0.10, "Otra": 0.02}
    return precio_base * descuentos[marca]


def calcular_descuento_dia(dia_semana, es_feriado):
    if es_feriado:
        return 0.25
    elif dia_semana == 1:  # Martes
        return 0.12
    elif dia_semana == 5:  # Sábado
        return 0.18
    else:
        return 0


def calcular_precio_final(precio_base, descuento_marca, descuento_dia):
    descuento_total = descuento_marca + descuento_dia
    if descuento_total > 0.30:  # Límite máximo de descuento del 30%
        descuento_total = 0.30
    return precio_base * (1 - descuento_total)


def main():
    precio_base = obtener_precio_base()
    marca = obtener_marca()

    hoy = datetime.now()
    dia_semana = hoy.weekday()
    es_feriado = input("¿Es día feriado? (s/n): ").lower() == 's'

    descuento_marca = calcular_descuento_marca(marca, precio_base)
    descuento_dia = calcular_descuento_dia(dia_semana, es_feriado)
    precio_final = calcular_precio_final(precio_base, descuento_marca, descuento_dia)

    print("\nResumen de la venta:")
    print(f"Marca: {marca}")
    print(f"Precio base: ${precio_base:.2f}")
    print(f"Descuento por marca: ${descuento_marca:.2f} ({(descuento_marca / precio_base * 100):.1f}%)")
    print(
        f"Descuento por día: ${precio_base * calcular_descuento_dia(dia_semana, es_feriado):.2f} ({calcular_descuento_dia(dia_semana, es_feriado) * 100:.1f}%)")
    print(f"Precio final: ${precio_final:.2f}")

    ahorro_total = precio_base - precio_final
    print(f"Ahorro total: ${ahorro_total:.2f} ({(ahorro_total / precio_base * 100):.1f}%)")

    # Mostrar precios para otros días de la semana
    print("\nPrecios para otros días:")
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    for i, dia in enumerate(dias):
        precio_dia = calcular_precio_final(precio_base, descuento_marca, calcular_descuento_dia(i, False))
        print(f"{dia}: ${precio_dia:.2f}")

    print(
        f"\nPrecio en día feriado: ${calcular_precio_final(precio_base, descuento_marca, calcular_descuento_dia(0, True)):.2f}")


if __name__ == "__main__":
    main()