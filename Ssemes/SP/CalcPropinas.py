def calcular_propina(total_cuenta, calidad_servicio):
    match calidad_servicio.lower():
        case "excelente":
            return total_cuenta * 0.20
        case "bueno":
            return total_cuenta * 0.15
        case "regular":
            return total_cuenta * 0.10
        case _:
            return 0

def obte_entra_usua():
    total_cuenta = float(input("Ingrese el total de la cuenta: $"))
    calidad_servicio = input("Califique el servicio (excelente/bueno/regular): ")
    return total_cuenta, calidad_servicio

def mostrar_resultado(propina):
    print(f"La propina sugerida es: ${propina:.2f}")

def calculadora_propinas():
    total_cuenta, calidad_servicio = obte_entra_usua()
    propina = calcular_propina(total_cuenta, calidad_servicio)
    mostrar_resultado(propina)

# Ejecutar el programa
calculadora_propinas()