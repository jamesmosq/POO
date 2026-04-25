import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Cargar el dataset
df = pd.read_excel('ventas_dataset.xlsx')

# 1. EXPLORACIÓN INICIAL DE DATOS
print("Primeras 5 filas del dataset:")
print(df.head())

print("\nInformación del dataset:")
print(df.info())

print("\nEstadísticas descriptivas:")
print(df.describe())

# 2. ANÁLISIS DE VENTAS POR CATEGORÍA
ventas_por_categoria = df.groupby('Categoria')['Ventas_Totales'].sum().sort_values(ascending=False)
print("\nVentas totales por categoría:")
print(ventas_por_categoria)

plt.figure(figsize=(10, 6))
ventas_por_categoria.plot(kind='bar', color='skyblue')
plt.title('Ventas Totales por Categoría')
plt.xlabel('Categoría')
plt.ylabel('Ventas Totales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('ventas_por_categoria.png')

# 3. ANÁLISIS DE VENTAS POR PRODUCTO
ventas_por_producto = df.groupby('Producto')['Ventas_Totales'].sum().sort_values(ascending=False)
print("\nVentas totales por producto:")
print(ventas_por_producto)

plt.figure(figsize=(10, 6))
ventas_por_producto.plot(kind='bar', color='lightgreen')
plt.title('Ventas Totales por Producto')
plt.xlabel('Producto')
plt.ylabel('Ventas Totales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('ventas_por_producto.png')

# 4. ANÁLISIS DE VENTAS POR REGIÓN
ventas_por_region = df.groupby('Region')['Ventas_Totales'].sum().sort_values(ascending=False)
print("\nVentas totales por región:")
print(ventas_por_region)

plt.figure(figsize=(10, 6))
plt.pie(ventas_por_region, labels=ventas_por_region.index, autopct='%1.1f%%', startangle=90, shadow=True)
plt.axis('equal')
plt.title('Distribución de Ventas por Región')
plt.tight_layout()
plt.savefig('ventas_por_region.png')

# 5. ANÁLISIS DE VENTAS POR VENDEDOR
ventas_por_vendedor = df.groupby('Vendedor')['Ventas_Totales'].sum().sort_values(ascending=False)
print("\nVentas totales por vendedor:")
print(ventas_por_vendedor)

plt.figure(figsize=(10, 6))
ventas_por_vendedor.plot(kind='bar', color='salmon')
plt.title('Ventas Totales por Vendedor')
plt.xlabel('Vendedor')
plt.ylabel('Ventas Totales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('ventas_por_vendedor.png')

# 6. ANÁLISIS DE TENDENCIA DE VENTAS POR MES
df['Mes'] = pd.DatetimeIndex(df['Fecha']).month
df['Nombre_Mes'] = pd.DatetimeIndex(df['Fecha']).month_name()

ventas_por_mes = df.groupby(['Mes', 'Nombre_Mes'])['Ventas_Totales'].sum().reset_index()
ventas_por_mes = ventas_por_mes.sort_values('Mes')

print("\nVentas totales por mes:")
print(ventas_por_mes[['Nombre_Mes', 'Ventas_Totales']])

plt.figure(figsize=(12, 6))
plt.plot(ventas_por_mes['Nombre_Mes'], ventas_por_mes['Ventas_Totales'], marker='o', linestyle='-', color='purple')
plt.title('Tendencia de Ventas Mensuales')
plt.xlabel('Mes')
plt.ylabel('Ventas Totales')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('tendencia_ventas_mensuales.png')

# 7. CORRELACIÓN ENTRE UNIDADES VENDIDAS Y PRECIO UNITARIO
plt.figure(figsize=(10, 6))
plt.scatter(df['Precio_Unitario'], df['Unidades'], alpha=0.5)
plt.title('Relación entre Precio Unitario y Unidades Vendidas')
plt.xlabel('Precio Unitario')
plt.ylabel('Unidades Vendidas')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('correlacion_precio_unidades.png')

# 8. ANÁLISIS DE CALOR (HEATMAP) DE VENTAS POR DÍA DE LA SEMANA Y MES
df['DiaSemana'] = pd.DatetimeIndex(df['Fecha']).day_name()
orden_dias = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df['DiaSemana'] = pd.Categorical(df['DiaSemana'], categories=orden_dias, ordered=True)

ventas_dia_mes = df.groupby(['DiaSemana', 'Mes'])['Ventas_Totales'].mean().unstack()
ventas_dia_mes = ventas_dia_mes.reindex(orden_dias)

plt.figure(figsize=(12, 8))
sns.heatmap(ventas_dia_mes, cmap='YlGnBu', annot=True, fmt='.0f')
plt.title('Promedio de Ventas por Día de la Semana y Mes')
plt.ylabel('Día de la Semana')
plt.xlabel('Mes')
plt.tight_layout()
plt.savefig('heatmap_ventas.png')

# 9. PRODUCTOS MÁS VENDIDOS POR REGIÓN
productos_por_region = df.groupby(['Region', 'Producto'])['Unidades'].sum().reset_index()
top_productos_por_region = productos_por_region.sort_values(['Region', 'Unidades'], ascending=[True, False])
top_productos_por_region = top_productos_por_region.groupby('Region').head(2)

print("\nProductos más vendidos por región:")
print(top_productos_por_region)

# 10. ANÁLISIS DE DISTRIBUCIÓN DE PRECIOS
plt.figure(figsize=(10, 6))
sns.histplot(df['Precio_Unitario'], bins=20, kde=True)
plt.title('Distribución de Precios Unitarios')
plt.xlabel('Precio Unitario')
plt.ylabel('Frecuencia')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('distribucion_precios.png')

print("\nAnálisis completado y gráficos guardados.")