import datetime

# Obtener la fecha y hora actual
ahora = datetime.datetime.now()
print(ahora)

# Crear una fecha específica
fecha = datetime.date(2024, 9, 28)
print(fecha)

# Diferencia entre fechas
fecha1 = datetime.date(2024, 1, 1)
fecha2 = datetime.date(2024, 12, 31)
diferencia = fecha2 - fecha1
print(diferencia.days)  # 365 días
