import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Establecer semilla para reproducibilidad
np.random.seed(42)

# Crear fechas para un año de datos
fecha_inicio = datetime(2023, 1, 1)
fechas = [fecha_inicio + timedelta(days=i) for i in range(365)]

# Crear datos para el dataset
data = {
    'Fecha': fechas,
    'Producto': np.random.choice(['Laptop', 'Smartphone', 'Tablet', 'Monitor', 'Teclado'], size=365),
    'Categoria': np.random.choice(['Electrónica', 'Accesorios', 'Informática'], size=365),
    'Region': np.random.choice(['Norte', 'Sur', 'Este', 'Oeste', 'Centro'], size=365),
    'Vendedor': np.random.choice(['Ana', 'Carlos', 'Elena', 'Roberto', 'María'], size=365),
    'Unidades': np.random.randint(1, 20, size=365),
    'Precio_Unitario': np.random.uniform(100, 1500, size=365).round(2)
}

# Crear DataFrame
df = pd.DataFrame(data)

# Calcular ventas totales
df['Ventas_Totales'] = (df['Unidades'] * df['Precio_Unitario']).round(2)

# Añadir alguna estacionalidad a las ventas
for i, fecha in enumerate(fechas):
    # Aumento en fin de semana
    if fecha.weekday() >= 5:  # 5 = sábado, 6 = domingo
        df.loc[i, 'Ventas_Totales'] *= 1.3
    # Aumento en fin de mes
    if fecha.day >= 25:
        df.loc[i, 'Ventas_Totales'] *= 1.2
    # Aumento en temporada navideña
    if fecha.month == 12 and fecha.day >= 10:
        df.loc[i, 'Ventas_Totales'] *= 1.5

# Redondear ventas
df['Ventas_Totales'] = df['Ventas_Totales'].round(2)

# Guardar en Excel
df.to_excel('ventas_dataset.xlsx', index=False)

print("Dataset creado y guardado como 'ventas_dataset.xlsx'")
