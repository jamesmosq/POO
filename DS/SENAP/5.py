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

# Análisis de deserción por estrato socioeconómico y ciudad
print("\n=== ANÁLISIS DE DESERCIÓN POR ESTRATO Y CIUDAD ===")

# 1. Tasa de deserción por estrato
print("\nTasa de deserción por estrato socioeconómico:")
desercion_por_estrato = datos.groupby('estrato')['desertor'].agg(['count', 'sum', 'mean'])
desercion_por_estrato.columns = ['Total estudiantes', 'Desertores', 'Tasa de deserción']
desercion_por_estrato['Tasa de deserción'] = desercion_por_estrato['Tasa de deserción'] * 100
desercion_por_estrato = desercion_por_estrato.reset_index()
desercion_por_estrato = desercion_por_estrato.sort_values('estrato')

print(tabulate(desercion_por_estrato,
               headers=['Estrato', 'Total estudiantes', 'Desertores', 'Tasa de deserción (%)'],
               tablefmt='grid',
               floatfmt=".2f"))

# 2. Tasa de deserción por ciudad (top 10 ciudades con más estudiantes)
print("\nTasa de deserción por ciudad (Top 10 ciudades con más estudiantes):")
ciudad_counts = datos['ciudad'].value_counts().head(10).index
desercion_por_ciudad = datos[datos['ciudad'].isin(ciudad_counts)].groupby('ciudad')['desertor'].agg(
    ['count', 'sum', 'mean'])
desercion_por_ciudad.columns = ['Total estudiantes', 'Desertores', 'Tasa de deserción']
desercion_por_ciudad['Tasa de deserción'] = desercion_por_ciudad['Tasa de deserción'] * 100
# CORRECCIÓN: Usar 'Total estudiantes' en lugar de 'count'
desercion_por_ciudad = desercion_por_ciudad.sort_values('Total estudiantes', ascending=False).reset_index()

print(tabulate(desercion_por_ciudad,
               headers=['Ciudad', 'Total estudiantes', 'Desertores', 'Tasa de deserción (%)'],
               tablefmt='grid',
               floatfmt=".2f"))
# 3. Análisis combinado de estrato y ciudad (para las 5 ciudades principales)
print("\nAnálisis combinado de estrato y ciudad (5 ciudades principales):")
top_ciudades = datos['ciudad'].value_counts().head(5).index
datos_top_ciudades = datos[datos['ciudad'].isin(top_ciudades)]

for ciudad in top_ciudades:
    print(f"\nCiudad: {ciudad}")
    datos_ciudad = datos[datos['ciudad'] == ciudad]
    desercion_ciudad_estrato = datos_ciudad.groupby('estrato')['desertor'].agg(['count', 'sum', 'mean'])
    desercion_ciudad_estrato.columns = ['Total estudiantes', 'Desertores', 'Tasa de deserción']
    desercion_ciudad_estrato['Tasa de deserción'] = desercion_ciudad_estrato['Tasa de deserción'] * 100
    desercion_ciudad_estrato = desercion_ciudad_estrato.reset_index()

    if not desercion_ciudad_estrato.empty:
        print(tabulate(desercion_ciudad_estrato,
                       headers=['Estrato', 'Total estudiantes', 'Desertores', 'Tasa de deserción (%)'],
                       tablefmt='grid',
                       floatfmt=".2f"))
    else:
        print("No hay datos suficientes para esta ciudad.")

# 4. Mapa de calor (opcional, requiere matplotlib y seaborn)
try:
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Crear una tabla pivote de estrato vs ciudad para tasa de deserción
    print("\nCreando mapa de calor de tasas de deserción por estrato y ciudad...")

    # Filtrar para incluir solo ciudades con suficientes datos por estrato (al menos 5 estudiantes)
    ciudades_con_datos = []
    for ciudad in datos['ciudad'].value_counts().head(10).index:
        ciudad_datos = datos[datos['ciudad'] == ciudad]
        if len(ciudad_datos.groupby('estrato').filter(lambda x: len(x) >= 5)) > 0:
            ciudades_con_datos.append(ciudad)

    if len(ciudades_con_datos) > 0:
        datos_heatmap = datos[datos['ciudad'].isin(ciudades_con_datos)]
        desercion_pivot = datos_heatmap.pivot_table(
            values='desertor',
            index='ciudad',
            columns='estrato',
            aggfunc='mean'
        ) * 100  # Convertir a porcentaje

        plt.figure(figsize=(12, 8))
        sns.heatmap(desercion_pivot, annot=True, cmap="YlOrRd", fmt=".1f", linewidths=.5)
        plt.title('Tasa de deserción (%) por Ciudad y Estrato')
        plt.tight_layout()
        plt.savefig('C:/Users/jmosquerarei/PycharmProjects/POO_III/DS/SENAP/desercion_ciudad_estrato_heatmap.png')
        print("Mapa de calor guardado como 'desercion_ciudad_estrato_heatmap.png'")
        plt.close()
    else:
        print("No hay suficientes datos para crear un mapa de calor significativo.")
except ImportError:
    print("No se pudo crear visualización. Matplotlib y/o Seaborn no están instalados.")

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
if "Random Forest" in mejor_modelo_nombre:
    print("\nImportancia de características (top 15):")
    importancias = mejor_modelo.feature_importances_
    indices = np.argsort(importancias)[::-1]

    # Obtener nombres de características para datos preprocesados
    # Esto es más complejo con datos preprocesados por SMOTE
    # Usamos una aproximación simplificada
    feature_names = []

    # Añadir nombres de características numéricas
    feature_names.extend(numericas)

    # Intentar obtener nombres de características categóricas codificadas
    try:
        onehot_features = preprocessor.named_transformers_['cat'].named_steps['onehot'].get_feature_names_out(
            categoricas)
        feature_names.extend(onehot_features)
    except:
        # En caso de error, usar nombres genéricos
        for i in range(X_train_smote.shape[1] - len(numericas)):
            feature_names.append(f"Feature_{len(numericas) + i}")

    # Mostrar top 15 características o todas si hay menos
    top_features = []
    for i in range(min(15, len(indices))):
        if i < len(feature_names):
            idx = indices[i]
            if idx < len(feature_names):
                top_features.append([feature_names[idx], importancias[idx]])
            else:
                top_features.append([f"Feature_{idx}", importancias[idx]])

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