def calcular_salario(horas_trabajadas, tarifa_por_hora, antiguedad, ventas_realizadas):
    salario_base = horas_trabajadas * tarifa_por_hora

    # Cálculo de horas extras
    if horas_trabajadas > 40:
        horas_extras = horas_trabajadas - 40
        salario_extra = horas_extras * (tarifa_por_hora * 1.5)
        salario_base = (40 * tarifa_por_hora) + salario_extra

    # Bonificación por antigüedad
    if antiguedad >= 5:
        bono_antiguedad = salario_base * 0.05
    else:
        bono_antiguedad = 0

    # Comisión por ventas
    if ventas_realizadas > 1000:
        comision = ventas_realizadas * 0.02
    else:
        comision = 0

    salario_bruto = salario_base + bono_antiguedad + comision

    # Cálculo de descuentos
    if salario_bruto <= 1000:
        descuento = salario_bruto * 0.10
    elif 1000 < salario_bruto <= 2000:
        descuento = 1000 * 0.10 + (salario_bruto - 1000) * 0.05
    else:
        descuento = 1000 * 0.10 + 1000 * 0.05 + (salario_bruto - 2000) * 0.03

    salario_neto = salario_bruto - descuento

    return salario_base, bono_antiguedad, comision, descuento, salario_neto


# Solicitar datos al usuario
horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
tarifa_por_hora = float(input("Ingrese la tarifa por hora: "))
antiguedad = int(input("Ingrese los años de antigüedad: "))
ventas_realizadas = float(input("Ingrese el total de ventas realizadas: "))

# Calcular y mostrar resultados
salario_base, bono_antiguedad, comision, descuento, salario_neto = calcular_salario(horas_trabajadas, tarifa_por_hora,
                                                                                    antiguedad, ventas_realizadas)

print("\nResumen de salario:")
print(f"Salario base: ${salario_base:.2f}")
print(f"Bono por antigüedad: ${bono_antiguedad:.2f}")
print(f"Comisión por ventas: ${comision:.2f}")
print(f"Descuentos: ${descuento:.2f}")
print(f"Salario neto: ${salario_neto:.2f}")