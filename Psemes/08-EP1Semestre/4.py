import statistics


def obtener_calificaciones():
    calificaciones = []
    num_calificaciones = 3
    for i in range(num_calificaciones):
        while True:
            try:
                calificacion = float(input(f"Ingrese la calificación {i + 1} (0-10): "))
                if 0 <= calificacion <= 10:
                    calificaciones.append(calificacion)
                    break
                else:
                    print("La calificación debe estar entre 0 y 10.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
    return calificaciones


def analizar_calificaciones(calificaciones):
    promedio = statistics.mean(calificaciones)
    mediana = statistics.median(calificaciones)
    desviacion_estandar = statistics.stdev(calificaciones)
    maximo = max(calificaciones)
    minimo = min(calificaciones)

    return promedio, mediana, desviacion_estandar, maximo, minimo


def determinar_estado(promedio):
    if promedio >= 9:
        return "Excelente"
    elif promedio >= 7:
        return "Bueno"
    elif promedio >= 5:
        return "Aprobado"
    else:
        return "Reprobado"


def generar_recomendacion(estado, desviacion_estandar):
    if estado == "Excelente":
        return "¡Felicidades! Mantén tu excelente desempeño."
    elif estado == "Bueno":
        return "Buen trabajo. Considera enfocarte en mejorar tus áreas más débiles."
    elif estado == "Aprobado":
        if desviacion_estandar > 2:
            return "Aprobado, pero tus calificaciones son inconsistentes. Trabaja en mantener un rendimiento estable."
        else:
            return "Aprobado. Enfócate en mejorar gradualmente tu rendimiento."
    else:
        return "Necesitas mejorar significativamente. Considera buscar ayuda adicional o tutoría."


def main():
    calificaciones = obtener_calificaciones()
    promedio, mediana, desviacion_estandar, maximo, minimo = analizar_calificaciones(calificaciones)
    estado = determinar_estado(promedio)
    recomendacion = generar_recomendacion(estado, desviacion_estandar)

    print("\nAnálisis de calificaciones:")
    print(f"Calificaciones: {calificaciones}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Mediana: {mediana}")
    print(f"Desviación estándar: {desviacion_estandar:.2f}")
    print(f"Calificación más alta: {maximo}")
    print(f"Calificación más baja: {minimo}")
    print(f"Estado: {estado}")
    print(f"Recomendación: {recomendacion}")


main()