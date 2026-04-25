import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Establecer semilla para reproducibilidad
np.random.seed(42)
random.seed(42)

# Número de registros a generar
n_registros = 1000


# Función para generar fechas aleatorias dentro de un rango
def random_dates(start_date, end_date, n):
    start_u = start_date.timestamp()
    end_u = end_date.timestamp()
    return pd.to_datetime([datetime.fromtimestamp(random.uniform(start_u, end_u)) for _ in range(n)])


# Generar datos demográficos y personales
def generar_datos_demograficos(n):
    edad = np.random.randint(16, 55, n)
    genero = np.random.choice(['Masculino', 'Femenino'], n)

    # Ciudades por departamento
    ciudades_por_departamento = {
        'Antioquia': ['Medellín', 'Envigado', 'Bello', 'Itagüí', 'Rionegro'],
        'Atlántico': ['Barranquilla', 'Soledad', 'Malambo'],
        'Bogotá D.C.': ['Bogotá'],
        'Valle del Cauca': ['Cali', 'Palmira', 'Buenaventura', 'Yumbo'],
        'Santander': ['Bucaramanga', 'Floridablanca', 'Girón', 'Piedecuesta'],
        'Bolívar': ['Cartagena', 'Magangué', 'Turbaco']
    }

    # Seleccionar departamentos aleatoriamente
    departamentos = list(ciudades_por_departamento.keys())
    departamento_list = np.random.choice(departamentos, n)

    # Seleccionar ciudades según el departamento
    ciudad_list = []
    for dep in departamento_list:
        ciudad_list.append(np.random.choice(ciudades_por_departamento[dep]))

    estrato = np.random.choice([1, 2, 3, 4, 5, 6], n, p=[0.15, 0.25, 0.35, 0.15, 0.07, 0.03])
    estado_civil = np.random.choice(['Soltero', 'Casado', 'Unión libre', 'Divorciado', 'Viudo'],
                                    n, p=[0.7, 0.15, 0.1, 0.04, 0.01])

    personas_cargo = np.random.choice([0, 1, 2, 3, 4, 5], n, p=[0.6, 0.2, 0.1, 0.05, 0.03, 0.02])
    situacion_laboral = np.random.choice(['No trabaja', 'Trabaja tiempo parcial', 'Trabaja tiempo completo'],
                                         n, p=[0.55, 0.3, 0.15])

    return pd.DataFrame({
        'edad': edad,
        'genero': genero,
        'departamento': departamento_list,
        'ciudad': ciudad_list,
        'estrato': estrato,
        'estado_civil': estado_civil,
        'personas_a_cargo': personas_cargo,
        'situacion_laboral': situacion_laboral
    })


# Generar datos académicos previos
def generar_datos_academicos_previos(n):
    tipo_institucion_previa = np.random.choice(['Pública', 'Privada'], n, p=[0.7, 0.3])
    nivel_educativo_previo = np.random.choice(
        ['Bachillerato', 'Técnico', 'Universitario incompleto', 'Universitario completo'],
        n, p=[0.75, 0.15, 0.08, 0.02])

    tiempo_entre_formaciones = np.random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], n,
                                                p=[0.3, 0.2, 0.15, 0.1, 0.05, 0.05, 0.05, 0.03, 0.03, 0.02, 0.02])

    # Distribucion de calificaciones con media 3.8 y desviación 0.7
    promedio_previo = np.random.normal(3.8, 0.7, n)
    # Limitar entre 0 y 5
    promedio_previo = np.clip(promedio_previo, 0, 5)
    # Redondear a 1 decimal
    promedio_previo = np.round(promedio_previo, 1)

    return pd.DataFrame({
        'tipo_institucion_previa': tipo_institucion_previa,
        'nivel_educativo_previo': nivel_educativo_previo,
        'tiempo_entre_formaciones_anos': tiempo_entre_formaciones,
        'promedio_academico_previo': promedio_previo
    })


# Generar datos de admisión y programa
def generar_datos_programa(n):
    programas = [
        'Técnico en Sistemas',
        'Tecnología en Desarrollo de Software',
        'Técnico en Recursos Humanos',
        'Tecnología en Gestión Administrativa',
        'Técnico en Contabilización de Operaciones',
        'Tecnología en Contabilidad y Finanzas',
        'Técnico en Logística',
        'Técnico en Cocina',
        'Tecnología en Gestión Hotelera',
        'Técnico en Mantenimiento de Motocicletas',
        'Tecnología en Mantenimiento de Equipo Biomédico',
        'Técnico en Mantenimiento Eléctrico Industrial',
        'Técnico en Confección Industrial'
    ]

    programa = np.random.choice(programas, n)

    # Asignar la cantidad de matriculados por programa
    cantidad_matriculados = {}
    for prog in programas:
        if prog.startswith('Técnico'):
            cantidad_matriculados[prog] = np.random.randint(25, 40)
        else:
            cantidad_matriculados[prog] = np.random.randint(20, 35)

    matriculados_programa = [cantidad_matriculados[prog] for prog in programa]

    modalidad = np.random.choice(['Presencial', 'Virtual', 'Mixta'], n, p=[0.7, 0.2, 0.1])

    centros_formacion = [
        'Centro de Servicios Financieros',
        'Centro de Tecnologías del Transporte',
        'Centro de Gestión Industrial',
        'Centro de Electricidad, Electrónica y Telecomunicaciones',
        'Centro de Manufactura en Textil y Cuero',
        'Centro de Tecnologías para la Construcción y la Madera',
        'Centro de Desarrollo Agroempresarial'
    ]

    centro_formacion = np.random.choice(centros_formacion, n)

    jornada = np.random.choice(['Mañana', 'Tarde', 'Noche', 'Fines de semana'],
                               n, p=[0.35, 0.3, 0.3, 0.05])

    # Fechas de inicio aleatorias entre 2020 y 2023
    fecha_inicio = random_dates(datetime(2020, 1, 1), datetime(2023, 12, 31), n)

    # Duración de programa (en trimestres)
    duracion = np.where(
        [prog.startswith('Técnico') for prog in programa],
        np.random.choice([3, 4], n),  # Técnicos
        np.random.choice([6, 7], n)  # Tecnologías
    )

    primera_opcion = np.random.choice(['Sí', 'No'], n, p=[0.8, 0.2])

    motivos = [
        'Interés personal',
        'Oportunidad laboral',
        'Recomendación familiar',
        'Prestigio del programa',
        'Única opción disponible',
        'Continuidad de estudios previos'
    ]
    motivo_eleccion = np.random.choice(motivos, n)

    return pd.DataFrame({
        'programa': programa,
        'matriculados_programa': matriculados_programa,
        'modalidad': modalidad,
        'centro_formacion': centro_formacion,
        'jornada': jornada,
        'fecha_inicio': fecha_inicio,
        'duracion_trimestres': duracion,
        'primera_opcion': primera_opcion,
        'motivo_eleccion': motivo_eleccion
    })


# Generar datos socioeconómicos
def generar_datos_socioeconomicos(n, estrato):
    # Ingresos según estrato
    ingresos_por_estrato = {
        1: np.random.randint(800000, 1200000, n),
        2: np.random.randint(1000000, 1800000, n),
        3: np.random.randint(1500000, 2800000, n),
        4: np.random.randint(2500000, 4500000, n),
        5: np.random.randint(4000000, 8000000, n),
        6: np.random.randint(7000000, 15000000, n)
    }

    ingresos = [ingresos_por_estrato[e][i] for i, e in enumerate(estrato)]

    dependencia_economica = np.random.choice(
        ['Independiente', 'Depende de padres', 'Depende de pareja', 'Depende de otros familiares'],
        n, p=[0.3, 0.6, 0.08, 0.02])

    # Probabilidad de acceso a internet según estrato
    prob_internet = {
        1: 0.6,
        2: 0.75,
        3: 0.9,
        4: 0.95,
        5: 0.99,
        6: 0.99
    }

    acceso_internet = [np.random.choice(['Sí', 'No'], 1, p=[prob_internet[e], 1 - prob_internet[e]])[0] for e in
                       estrato]

    # Probabilidad de tener computador según estrato
    prob_pc = {
        1: 0.4,
        2: 0.6,
        3: 0.8,
        4: 0.9,
        5: 0.98,
        6: 0.99
    }

    computador_propio = [np.random.choice(['Sí', 'No'], 1, p=[prob_pc[e], 1 - prob_pc[e]])[0] for e in estrato]

    transporte = np.random.choice(['Público', 'Propio', 'A pie', 'Bicicleta', 'Moto'],
                                  n, p=[0.6, 0.15, 0.1, 0.05, 0.1])

    tiempo_desplazamiento = np.random.choice(['Menos de 30 min', '30-60 min', '60-90 min', 'Más de 90 min'],
                                             n, p=[0.3, 0.4, 0.2, 0.1])

    return pd.DataFrame({
        'ingresos_familiares': ingresos,
        'dependencia_economica': dependencia_economica,
        'acceso_internet': acceso_internet,
        'computador_propio': computador_propio,
        'medio_transporte': transporte,
        'tiempo_desplazamiento': tiempo_desplazamiento
    })


# Generar datos de rendimiento y participación
def generar_datos_rendimiento(n):
    # Asistencia (porcentaje)
    asistencia = np.random.normal(85, 15, n)
    asistencia = np.clip(asistencia, 0, 100)
    asistencia = np.round(asistencia, 1)

    # Calificaciones
    calificaciones = np.random.normal(3.8, 0.8, n)
    calificaciones = np.clip(calificaciones, 0, 5)
    calificaciones = np.round(calificaciones, 1)

    # Tiempo de conexión para componentes virtuales (horas semanales)
    tiempo_conexion = np.random.normal(5, 3, n)
    tiempo_conexion = np.clip(tiempo_conexion, 0, 20)
    tiempo_conexion = np.round(tiempo_conexion, 1)

    participacion_actividades = np.random.choice(['Ninguna', 'Baja', 'Media', 'Alta'],
                                                 n, p=[0.2, 0.3, 0.4, 0.1])

    uso_biblioteca = np.random.choice(['Nunca', 'Ocasional', 'Frecuente', 'Muy frecuente'],
                                      n, p=[0.4, 0.3, 0.2, 0.1])

    entrega_evidencias = np.random.choice(
        ['Siempre a tiempo', 'Mayormente a tiempo', 'Con retrasos frecuentes', 'Incompletas'],
        n, p=[0.5, 0.3, 0.15, 0.05])

    return pd.DataFrame({
        'porcentaje_asistencia': asistencia,
        'promedio_calificaciones': calificaciones,
        'horas_conexion_semanal': tiempo_conexion,
        'participacion_actividades': participacion_actividades,
        'uso_biblioteca': uso_biblioteca,
        'entrega_evidencias': entrega_evidencias
    })


# Generar datos de comportamiento
def generar_datos_comportamiento(n):
    sanciones = np.random.choice(['Ninguna', 'Advertencia', 'Sanción leve', 'Sanción grave'],
                                 n, p=[0.9, 0.06, 0.03, 0.01])

    solicitudes_aplazamiento = np.random.choice([0, 1, 2, 3], n, p=[0.85, 0.1, 0.04, 0.01])

    participacion_bienestar = np.random.choice(['Ninguna', 'Baja', 'Media', 'Alta'],
                                               n, p=[0.6, 0.2, 0.15, 0.05])

    uso_consejeria = np.random.choice(['Nunca', 'Una vez', 'Ocasional', 'Frecuente'],
                                      n, p=[0.7, 0.15, 0.1, 0.05])

    return pd.DataFrame({
        'sanciones_disciplinarias': sanciones,
        'solicitudes_aplazamiento': solicitudes_aplazamiento,
        'participacion_bienestar': participacion_bienestar,
        'uso_servicios_consejeria': uso_consejeria
    })


# Generar datos de seguimiento
def generar_datos_seguimiento(n):
    alertas_previas = np.random.choice([0, 1, 2, 3, 4], n, p=[0.7, 0.15, 0.08, 0.05, 0.02])

    intervenciones = np.random.choice([0, 1, 2, 3], n, p=[0.75, 0.15, 0.08, 0.02])

    cambios_horario = np.random.choice([0, 1, 2], n, p=[0.8, 0.15, 0.05])

    dificultades = np.random.choice(
        ['Ninguna reportada', 'Económicas', 'Salud', 'Académicas', 'Familiares', 'Laborales', 'Múltiples'],
        n, p=[0.6, 0.1, 0.05, 0.1, 0.05, 0.05, 0.05])

    return pd.DataFrame({
        'alertas_tempranas_previas': alertas_previas,
        'intervenciones_realizadas': intervenciones,
        'cambios_horario_solicitados': cambios_horario,
        'dificultades_reportadas': dificultades
    })


# Generar variable objetivo (estado final)
def generar_variable_objetivo(df_demo, df_acad, df_prog, df_socio, df_rend, df_comp, df_seg):
    n = len(df_demo)

    # Crear un modelo simple para determinar la probabilidad de deserción
    prob_desercion = np.zeros(n)

    # Factores que aumentan probabilidad de deserción
    prob_desercion += (df_demo['edad'] > 40) * 0.1
    prob_desercion += (df_demo['personas_a_cargo'] > 2) * 0.15
    prob_desercion += (df_demo['situacion_laboral'] == 'Trabaja tiempo completo') * 0.2

    prob_desercion += (df_acad['promedio_academico_previo'] < 3.0) * 0.15

    prob_desercion += (df_prog['modalidad'] == 'Virtual') * 0.1
    prob_desercion += (df_prog['jornada'] == 'Noche') * 0.05
    prob_desercion += (df_prog['primera_opcion'] == 'No') * 0.1

    prob_desercion += (df_socio['acceso_internet'] == 'No') * 0.2
    prob_desercion += (df_socio['tiempo_desplazamiento'] == 'Más de 90 min') * 0.15

    prob_desercion += (df_rend['porcentaje_asistencia'] < 70) * 0.3
    prob_desercion += (df_rend['promedio_calificaciones'] < 3.0) * 0.25
    prob_desercion += (df_rend['entrega_evidencias'] == 'Incompletas') * 0.2

    prob_desercion += (df_comp['sanciones_disciplinarias'] == 'Sanción grave') * 0.2
    prob_desercion += (df_comp['solicitudes_aplazamiento'] > 1) * 0.15

    prob_desercion += (df_seg['alertas_tempranas_previas'] > 2) * 0.25
    prob_desercion += (df_seg['dificultades_reportadas'] == 'Múltiples') * 0.2

    # Normalizar probabilidades entre 0.1 y 0.7
    prob_desercion = 0.1 + 0.6 * (prob_desercion - np.min(prob_desercion)) / (
                np.max(prob_desercion) - np.min(prob_desercion))

    # Determinar estado final basado en probabilidad
    estado_final = []
    momento_desercion = []
    razon_desercion = []

    for i in range(n):
        if np.random.random() < prob_desercion[i]:
            estado_final.append('Desertor')
            # Momento de deserción
            if df_rend['porcentaje_asistencia'][i] < 30:
                momento_desercion.append('Primer trimestre')
            elif df_rend['porcentaje_asistencia'][i] < 60:
                momento_desercion.append('Segundo trimestre')
            else:
                momento_desercion.append('Etapa final')

            # Razón de deserción
            razones = ['Problemas económicos', 'Bajo rendimiento académico',
                       'Incompatibilidad laboral', 'Problemas personales/familiares',
                       'Expectativas no satisfechas', 'Problemas de salud', 'Sin información']

            # Asignar razones más probables según el perfil
            if df_socio['ingresos_familiares'][i] < 1000000:
                razon_desercion.append('Problemas económicos')
            elif df_rend['promedio_calificaciones'][i] < 3.0:
                razon_desercion.append('Bajo rendimiento académico')
            elif df_demo['situacion_laboral'][i] == 'Trabaja tiempo completo':
                razon_desercion.append('Incompatibilidad laboral')
            elif df_seg['dificultades_reportadas'][i] in ['Familiares', 'Múltiples']:
                razon_desercion.append('Problemas personales/familiares')
            elif df_prog['primera_opcion'][i] == 'No':
                razon_desercion.append('Expectativas no satisfechas')
            elif df_seg['dificultades_reportadas'][i] == 'Salud':
                razon_desercion.append('Problemas de salud')
            else:
                razon_desercion.append(np.random.choice(razones))
        else:
            estado_final.append('Graduado' if np.random.random() < 0.9 else 'En curso')
            momento_desercion.append('No aplica')
            razon_desercion.append('No aplica')

    return pd.DataFrame({
        'estado_final': estado_final,
        'momento_desercion': momento_desercion,
        'razon_desercion': razon_desercion,
        'probabilidad_desercion': np.round(prob_desercion, 3)  # Solo para referencia
    })


# Generar todos los conjuntos de datos
df_demograficos = generar_datos_demograficos(n_registros)
df_academicos = generar_datos_academicos_previos(n_registros)
df_programa = generar_datos_programa(n_registros)
df_socioeconomicos = generar_datos_socioeconomicos(n_registros, df_demograficos['estrato'])
df_rendimiento = generar_datos_rendimiento(n_registros)
df_comportamiento = generar_datos_comportamiento(n_registros)
df_seguimiento = generar_datos_seguimiento(n_registros)

# Generar variable objetivo
df_objetivo = generar_variable_objetivo(
    df_demograficos,
    df_academicos,
    df_programa,
    df_socioeconomicos,
    df_rendimiento,
    df_comportamiento,
    df_seguimiento
)

# Combinar todos los dataframes
df_completo = pd.concat([
    df_demograficos,
    df_academicos,
    df_programa,
    df_socioeconomicos,
    df_rendimiento,
    df_comportamiento,
    df_seguimiento,
    df_objetivo
], axis=1)

# Añadir un ID único para cada estudiante
df_completo['id_estudiante'] = [f'EST{i:06d}' for i in range(1, n_registros + 1)]

# Reorganizar columnas para que id_estudiante sea la primera
cols = df_completo.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_completo = df_completo[cols]

# Guardar a CSV
df_completo.to_csv('datos_desercion_sena_ficticios.csv', index=False)

print(f"Archivo generado con {n_registros} registros.")

# Estadísticas básicas sobre deserción
total_desertores = (df_completo['estado_final'] == 'Desertor').sum()
tasa_desercion = total_desertores / n_registros * 100

print(f"\nEstadísticas de deserción:")
print(f"Total de estudiantes: {n_registros}")
print(f"Total de desertores: {total_desertores}")
print(f"Tasa de deserción: {tasa_desercion:.2f}%")

print("\nDistribución por momento de deserción:")
print(df_completo[df_completo['estado_final'] == 'Desertor']['momento_desercion'].value_counts())

print("\nDistribución por razón de deserción:")
print(df_completo[df_completo['estado_final'] == 'Desertor']['razon_desercion'].value_counts())

# Mostrar algunas filas del dataset generado
print("\nPrimeras 5 filas del dataset generado:")
print(df_completo.head(5))