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
X = datos.drop(
    ['id_estudiante', 'estado_final', 'desertor', 'momento_desercion', 'razon_desercion', 'probabilidad_desercion'],
    axis=1)
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

# ----- MEJORA 1: Usar SMOTE para balancear clases -----
print("\nAplicando SMOTE para balancear las clases...")
# Preprocesar los datos antes de aplicar SMOTE
X_train_prep = preprocessor.fit_transform(X_train)
smote = SMOTE(random_state=42)
X_train_smote, y_train_smote = smote.fit_resample(X_train_prep, y_train)
print(f"Tamaño del conjunto de entrenamiento original: {X_train.shape[0]}")
print(f"Tamaño del conjunto de entrenamiento balanceado: {X_train_smote.shape[0]}")
print(f"Distribución de clases original: {pd.Series(y_train).value_counts().to_dict()}")
print(f"Distribución de clases balanceada: {pd.Series(y_train_smote).value_counts().to_dict()}")

# ----- MEJORA 2: Probar múltiples modelos -----
print("\nEntrenando y comparando múltiples modelos con datos balanceados...")

# No incluimos el preprocesador en estos modelos ya que los datos ya están preprocesados
modelos = {
    "Random Forest Balanceado": RandomForestClassifier(
        n_estimators=100,
        class_weight='balanced',
        random_state=42
    ),
    "Gradient Boosting": GradientBoostingClassifier(
        n_estimators=100,
        random_state=42
    ),
    "Regresión Logística": LogisticRegression(
        max_iter=1000,
        class_weight='balanced',
        random_state=42
    )
}

# Comparar modelos
resultados_modelos = {}

for nombre, modelo in modelos.items():
    print(f"\nEntrenando modelo: {nombre}")
    modelo.fit(X_train_smote, y_train_smote)

    # Predicciones en el conjunto de prueba preprocesado
    X_test_prep = preprocessor.transform(X_test)
    y_pred = modelo.predict(X_test_prep)
    y_prob = modelo.predict_proba(X_test_prep)[:, 1]

    # Métricas
    accuracy = (y_pred == y_test).mean()
    roc_auc = roc_auc_score(y_test, y_prob)

    resultados_modelos[nombre] = {
        'accuracy': accuracy,
        'roc_auc': roc_auc,
        'modelo': modelo,
        'predicciones': y_pred,
        'probabilidades': y_prob
    }

    print(f"Accuracy: {accuracy:.4f}")
    print(f"ROC AUC: {roc_auc:.4f}")

    # Matriz de confusión
    cm = confusion_matrix(y_test, y_pred)
    cm_df = pd.DataFrame(cm,
                         index=['Real: No Desertor', 'Real: Desertor'],
                         columns=['Predicho: No Desertor', 'Predicho: Desertor'])
    print("\nMatriz de confusión:")
    print(tabulate(cm_df, headers='keys', tablefmt='grid'))

    # Reporte de clasificación
    print("\nReporte de clasificación:")
    report = classification_report(y_test, y_pred, output_dict=True)
    report_df = pd.DataFrame(report).transpose()
    print(tabulate(report_df.round(3), headers='keys', tablefmt='grid'))

# Seleccionar el mejor modelo basado en ROC AUC
mejor_modelo_nombre = max(resultados_modelos, key=lambda x: resultados_modelos[x]['roc_auc'])
mejor_modelo = resultados_modelos[mejor_modelo_nombre]['modelo']
mejor_predicciones = resultados_modelos[mejor_modelo_nombre]['predicciones']
mejor_probabilidades = resultados_modelos[mejor_modelo_nombre]['probabilidades']

print(f"\nMejor modelo basado en ROC AUC: {mejor_modelo_nombre}")
print(f"ROC AUC: {resultados_modelos[mejor_modelo_nombre]['roc_auc']:.4f}")

# ----- MEJORA 3: Análisis de importancia de características para Random Forest -----
if isinstance(mejor_modelo, RandomForestClassifier):
    print("\nImportancia de características (top 15):")
    importancias = mejor_modelo.feature_importances_
    indices = np.argsort(importancias)[::-1]

    # Crear nombres de características para datos preprocesados
    n_numericas = len(numericas)
    nombres_caracteristicas = list(numericas)

    # Obtener nombres de características codificadas con one-hot
    encoder = preprocessor.named_transformers_['cat'].named_steps['onehot']
    nombres_categoricas_codificadas = encoder.get_feature_names_out(categoricas)
    nombres_caracteristicas.extend(nombres_categoricas_codificadas)

    # Mostrar top 15 características
    top_features = []
    for i in range(min(15, len(nombres_caracteristicas))):
        if i < len(indices):
            top_features.append([nombres_caracteristicas[indices[i]], importancias[indices[i]]])

    print(tabulate(top_features, headers=['Característica', 'Importancia'], tablefmt='grid'))

# Guardar resultados de predicción en un nuevo DataFrame
resultados = datos[['id_estudiante', 'estado_final']].copy()
resultados.loc[:, 'probabilidad_predicha'] = 0.0  # Inicializar columna correctamente
resultados.loc[:, 'desercion_predicha'] = 0  # Inicializar columna correctamente

# Obtener predicciones para todo el conjunto de datos
X_full_prep = preprocessor.transform(X)
resultados.loc[:, 'probabilidad_predicha'] = mejor_modelo.predict_proba(X_full_prep)[:, 1]
resultados.loc[:, 'desercion_predicha'] = mejor_modelo.predict(X_full_prep)

# Identificar estudiantes con alta probabilidad de deserción
umbral_alto_riesgo = np.percentile(resultados['probabilidad_predicha'], 90)
resultados.loc[:, 'nivel_riesgo'] = 'Bajo'
resultados.loc[resultados['probabilidad_predicha'] >= umbral_alto_riesgo, 'nivel_riesgo'] = 'Alto'
resultados.loc[(resultados['probabilidad_predicha'] >= 0.5) &
               (resultados['probabilidad_predicha'] < umbral_alto_riesgo), 'nivel_riesgo'] = 'Medio'

print("\nDistribución de niveles de riesgo:")
risk_counts = resultados['nivel_riesgo'].value_counts().reset_index()
risk_counts.columns = ['Nivel de Riesgo', 'Cantidad']
print(tabulate(risk_counts, headers='keys', tablefmt='grid'))

# Guardar resultados
resultados.to_csv('C:/Users/jmosquerarei/PycharmProjects/POO_III/DS/SENAP/predicciones_desercion_mejorado.csv',
                  index=False)
print("\nResultados guardados en 'predicciones_desercion_mejorado.csv'")

# Mostrar algunos ejemplos de estudiantes con alto riesgo
print("\nEjemplos de estudiantes con alto riesgo de deserción:")
estudiantes_alto_riesgo = resultados[resultados['nivel_riesgo'] == 'Alto'].sort_values(by='probabilidad_predicha',
                                                                                       ascending=False).head(5)
# Usar .loc para evitar SettingWithCopyWarning
estudiantes_alto_riesgo_display = estudiantes_alto_riesgo[
    ['id_estudiante', 'probabilidad_predicha', 'estado_final']].copy()
estudiantes_alto_riesgo_display.loc[:, 'probabilidad_predicha'] = estudiantes_alto_riesgo_display[
    'probabilidad_predicha'].round(3)
print(tabulate(estudiantes_alto_riesgo_display, headers='keys', showindex=False, tablefmt='grid'))

# Mostrar ejemplos de falsos negativos (estudiantes que desertaron pero el modelo no predijo)
print("\nEjemplos de falsos negativos (desertores no identificados por el modelo):")
falsos_negativos = resultados[(resultados['estado_final'] == 'Desertor') &
                              (resultados['desercion_predicha'] == 0)].sort_values(by='probabilidad_predicha')
if len(falsos_negativos) > 0:
    falsos_neg_df = falsos_negativos[['id_estudiante', 'probabilidad_predicha', 'estado_final']].head(5).copy()
    falsos_neg_df.loc[:, 'probabilidad_predicha'] = falsos_neg_df['probabilidad_predicha'].round(3)
    print(tabulate(falsos_neg_df, headers='keys', showindex=False, tablefmt='grid'))
else:
    print("No se encontraron falsos negativos en este conjunto de datos.")