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

# Análisis estadístico: Chi-cuadrado para verificar relación entre estrato y deserción
from scipy.stats import chi2_contingency

# Crear tabla de contingencia entre estrato y deserción
tabla_contingencia = pd.crosstab(datos['estrato'], datos['desertor'])
chi2, p_valor, _, _ = chi2_contingency(tabla_contingencia)

print("\nResultado de prueba Chi-cuadrado:")
print(f"Chi2 = {chi2:.2f}, p-valor = {p_valor:.4f}")
if p_valor < 0.05:
    print("Hay una relación estadísticamente significativa entre estrato y deserción (p<0.05)")
else:
    print("No hay evidencia estadística de relación entre estrato y deserción (p>0.05)")