# Importar bibliotecas
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from tabulate import tabulate
from imblearn.over_sampling import SMOTE

# Cargar datos (ruta específica a tu archivo)
datos = pd.read_csv('C:/Users/jmosquerarei/PycharmProjects/POO_III/DS/SENAP/datos_desercion_sena_ficticios.csv')

# Verificar las columnas disponibles
print("Columnas disponibles en el dataset:")
print(tabulate([[col] for col in datos.columns.tolist()], headers=["Nombre de columna"], tablefmt="grid"))

# Crear la columna 'desertor' basada en 'estado_final'
datos['desertor'] = datos['estado_final'].apply(lambda x: 1 if x == 'Desertor' else 0)

# Mostrar distribución de la variable objetivo
print("\nDistribución de la variable objetivo:")
estado_counts = datos['estado_final'].value_counts().reset_index()
estado_counts.columns = ['Estado', 'Cantidad']
print(tabulate(estado_counts, headers='keys', tablefmt='grid'))

print("\nDistribución de la variable binaria 'desertor':")
desertor_counts = datos['desertor'].value_counts().reset_index()
desertor_counts.columns = ['Desertor', 'Cantidad']
desertor_counts['Desertor'] = desertor_counts['Desertor'].map({1: 'Sí', 0: 'No'})
print(tabulate(desertor_counts, headers='keys', tablefmt='grid'))
print(f"Porcentaje de desertores: {datos['desertor'].mean() * 100:.2f}%")

# Preparar datos
X = datos.drop(['id_estudiante', 'estado_final', 'desertor', 'momento_desercion', 'razon_desercion', 'probabilidad_desercion'], axis=1)
y = datos['desertor']  # 1 = desertor, 0 = no desertor

# Identificar tipos de columnas
numericas = X.select_dtypes(include=['int64', 'float64']).columns
categoricas = X.select_dtypes(include=['object']).columns

print("\nCaracterísticas numéricas:")
print(tabulate([[col] for col in numericas.tolist()], headers=["Variable numérica"], tablefmt="grid"))

print("\nCaracterísticas categóricas:")
print(tabulate([[col] for col in categoricas.tolist()], headers=["Variable categórica"], tablefmt="grid"))

# Crear transformadores para preprocesamiento
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numericas),
        ('cat', categorical_transformer, categoricas)
    ])

# Dividir en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
# Después de cargar los datos y antes de entrenar el modelo, añadir esto:

# Análisis de deserción por estrato socioeconómico
print("\n=== ANÁLISIS DE DESERCIÓN POR ESTRATO SOCIOECONÓMICO ===")
desercion_por_estrato = datos.groupby('estrato')['desertor'].agg(['count', 'sum', 'mean'])
desercion_por_estrato.columns = ['Total estudiantes', 'Desertores', 'Tasa de deserción']
desercion_por_estrato['Tasa de deserción'] = desercion_por_estrato['Tasa de deserción'] * 100
desercion_por_estrato = desercion_por_estrato.reset_index()
desercion_por_estrato = desercion_por_estrato.sort_values('estrato')

print(tabulate(desercion_por_estrato,
               headers=['Estrato', 'Total estudiantes', 'Desertores', 'Tasa de deserción (%)'],
               tablefmt='grid',
               floatfmt=".2f"))

# Opcional: Crear una visualización gráfica (necesita matplotlib)
try:
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 6))
    plt.bar(desercion_por_estrato['estrato'], desercion_por_estrato['Tasa de deserción'])
    plt.xlabel('Estrato socioeconómico')
    plt.ylabel('Tasa de deserción (%)')
    plt.title('Tasa de deserción por estrato socioeconómico')
    plt.xticks(desercion_por_estrato['estrato'])
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Agregar etiquetas de valor sobre cada barra
    for i, v in enumerate(desercion_por_estrato['Tasa de deserción']):
        plt.text(i + 1, v + 1, f"{v:.1f}%", ha='center')

    # Guardar gráfico
    plt.savefig('C:/Users/jmosquerarei/PycharmProjects/POO_III/DS/SENAP/desercion_por_estrato.png')
    print("\nGráfico guardado como 'desercion_por_estrato.png'")
    plt.close()
except ImportError:
    print("\nNo se pudo crear visualización. Matplotlib no está instalado.")